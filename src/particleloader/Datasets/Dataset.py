import itertools
import os
import sys

import hashlib
import json

import numpy as np
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

# Dataset class

class Dataset:

    def __init__(self, 
                    name,
                    description,
                    NUM_PER_FILE,
                    NUM_FILES,
                    options,
                    sources,
                    shapes,
                    npz_keys = None,
    ):  
        
        self.name = name
        self.description = description
        self.NUM_PER_FILE = NUM_PER_FILE
        self.NUM_FILES = NUM_FILES
        self.options = options
        self.sources = sources
        self.shapes = shapes
        self.npz_keys = npz_keys

        self.MAX_DATASET_SIZE = self.NUM_PER_FILE * self.NUM_FILES

        self.option_combinations = self.construct_all_option_combinations()
        self.option_combination_strings = [self.construct_options_string(**option_combination) for option_combination in self.option_combinations]

        # URLS is a nested dictionary with the following structure: {source: {option: urls}}
        self.URLS = {}
        for source in sources:
            self.URLS[source] = {}

            option_combinations = self.construct_all_option_combinations()

            for option_combination in option_combinations:
                self.URLS[source][self.construct_options_string(**option_combination)] = []
                
    
    # Add a URL to the URLS dictionary
    def add_url(self, source, urls):

        # Check if source is valid
        if source not in self.sources:
            raise Exception(f"Invalid source {source} for dataset {self.name}. Valid sources are {self.sources}")

        # Check if urls are valid: dictionary with same structure as URLS[source]
        if urls.keys() != self.URLS[source].keys():
            raise Exception(f"Invalid urls for dataset {self.name}. URLs must have the same structure as the URLS dictionary")
        
        # Check if urls are valid: list of urls of length NUM_FILES
        for option in urls:
            if len(urls[option]) != self.NUM_FILES:
                raise Exception(f"Invalid urls for dataset {self.name}. URLs must have length {self.NUM_FILES}")
            
        # Add urls to URLS dictionary
        for option in urls:
            self.URLS[source][option] = urls[option]

    def add_hash(self, hash_dict):

        # Check if hash_dict is valid: dictionary with same structure as URLS[source]
        if hash_dict.keys() != self.URLS[self.sources[0]].keys():
            raise Exception(f"Invalid hash_dict for dataset {self.name}. Hashes must have the same structure as the URLS dictionary")

        self.hashes = hash_dict



    
    # TEST FUNCTION FOR HASH GENERATION AND DEBUGGING ONLY
    def download_all(self, source, cache_dir = "~/.ParticleLoader"):

        # handle '~' in path
        datadir_base = os.path.expanduser(cache_dir)

        hash_dir = {}

        for (o, option_combination) in enumerate(self.option_combinations):

            option_combination_string = self.option_combination_strings[o]

            # Construct subdirectory name from options
            subdir = ''
            for key in option_combination:
                subdir += f"{key}:{option_combination[key]}/"
            datadir = os.path.join(datadir_base, self.name, subdir)
            if not os.path.exists(datadir):
                os.makedirs(datadir)

            hashes = []

            for i in range(self.NUM_FILES):

                # Construct Path
                url = self.URLS[source][option_combination_string][i]
                filename = url.split('/')[-1].split('?')[0]
                fpath = os.path.join(datadir, filename)

                print('Downloading {} from {} to {}'.format(filename, url, datadir))
                error_msg = 'URL fetch failure on {}: {} -- {}'

                # Download
                try:
                    try:
                        urlretrieve(url, fpath)
                    except URLError as e:
                        raise Exception(error_msg.format(url, e.errno, e.reason))
                    except HTTPError as e:
                        raise Exception(error_msg.format(url, e.code, e.msg))
                except (Exception, KeyboardInterrupt):
                    if os.path.exists(fpath):
                        os.remove(fpath)
                    raise

                # Compute hash
                h = str(_hash_file(fpath))
                hashes.append(h)

            hash_dir[option_combination_string] = hashes

        # Save as JSON
        json.dump( hash_dir, open( f"hashes/{self.name}_hashes.json", 'w' ) )
        
        return hash_dir


    def load(self, num_samples, cache_dir = "~/.ParticleLoader", **options):


        # Check if num_samples is valid
        if num_samples > self.MAX_DATASET_SIZE:
            raise Exception(f"num_samples {num_samples} exceeds the maximum dataset size of {self.MAX_DATASET_SIZE}")
        
        # Load Options, set defaults
        for key in self.options:
            if key not in options:
                options[key] = self.options[key][0]

            # Check if options are valid
            if options[key] not in self.options[key]:
                raise Exception(f"Invalid option {options[key]} for option {key} for dataset {self.name}. Valid options are {self.options[key]}")
        options_string = self.construct_options_string(**options)    
        
        # Construct subdirectory name from options
        subdir = ''
        for key in options:
            subdir += f"{key}:{options[key]}/"
        datadir = os.path.join(cache_dir, self.name, subdir)
        if not os.path.exists(datadir):
            os.makedirs(datadir)

        
        # Calculate how many files should be loaded
        num_files = int(np.ceil(num_samples/self.NUM_PER_FILE)) if num_samples > -1 else self.MAX_NUM_FILES

        # Set up data format
        data = []
        if self.npz_keys is not None:
            for key in self.npz_keys:
                data.append([])
        else:
            data.append([])

        # Loop over files
        for i in range(num_files):

            # Loop over sources
            for s, source in enumerate(self.sources):

                url = self.URLS[source][options_string][i]
                filename = url.split('/')[-1].split('?')[0]
                hash = self.hashes[options_string][i]

                # Attempt to load data
                try:
                    fpath = fetch(filename, url, datadir, hash)
                    break

                except Exception as e:

                    print(e)

                    # If this was the last source, raise the exception
                    if s == len(self.sources) - 1:
                        raise Exception(f"Error loading {filename} from any source")

                    else:
                        print(f"Error loading {filename} from source {source}, trying next source...")

            # We found the data, now load it
            try:
                with np.load(fpath) as f:
                    if self.npz_keys is not None:
                        for j, key in enumerate(self.npz_keys):
                            data[j].append(f[key])
                    else:
                            data[0].append(f)
            except Exception as e:
                f = np.load(fpath)
                data[0].append(f)

        # Concatenate data
        return_data = []
        for (d, shape) in enumerate(self.shapes):
            Xs = data[d]

            # Most common case: X, y pairs
            if len(shape) == 2:
                X = np.vstack([_pad_events_axis1(x[...,:shape[-2], :shape[-1]], shape[-2]) for x in Xs])
                return_data.append(X[:num_samples])
            else:
                X = np.concatenate(Xs, axis = 0)
                return_data.append(X[:num_samples])

        if len(return_data) == 1:
            return return_data[0]

        return return_data            

    # Construct a representation of dataset options for use in file naming and dictionary keys
    def construct_options_string(self, **options):

        # Check if options are valid
        for key in options:
            if key not in self.options:
                raise Exception(f"Invalid option {key} for dataset {self.name}. Valid options are {self.options.keys()}")

        # Check if option choices are valid
        for key in options:
            if options[key] not in self.options[key]:
                raise Exception(f"Invalid option choice {options[key]} for option {key} for dataset {self.name}. Valid choices are {self.options[key]}")


        # Construct options string
        options_string = ''
        for key in options:
            options_string += f"[{key}:{options[key]}]"

        return options_string

    def construct_all_option_combinations(self):

        all_options = []
        for option in self.options:
            all_options.append(self.options[option])


        array = list(itertools.product(*all_options))   

        # Convert to list of dictionaries
        options_list = []
        for a in array:
            options_dict = {}
            for i, key in enumerate(self.options):
                options_dict[key] = a[i]
            options_list.append(options_dict)

        return options_list

    def __str__(self):
        str = ''
        str += f"Dataset: {self.name}\n"
        str += f"Description: {self.description}\n"
        str += f"NUM_PER_FILE: {self.NUM_PER_FILE}\n"
        str += f"NUM_FILES: {self.NUM_FILES}\n"
        str += f"Options: {self.options}\n"
        str += f"Sources: {self.sources}\n"
        str += f"Shapes: {self.shapes}\n"
        return str
    


def fetch(filename, url, dir, file_hash):

    # handle '~' in path
    datadir_base = os.path.expanduser(dir)

    # ensure that directory exists
    datadir = os.path.join(datadir_base)
    if not os.path.exists(datadir):
        os.makedirs(datadir)

    fpath = os.path.join(datadir, filename)

    # determine if file needs to be downloaded
    download = False
    if os.path.exists(fpath):
        if file_hash is not None and not _validate_file(fpath, file_hash):
            print('Local file hash does not match so we will redownload...')
            download = True
    else:
        download = True

    if download:
        print('Downloading {} from {} to {}'.format(filename, url, datadir))

        error_msg = 'URL fetch failure on {}: {} -- {}'
        try:
            try:
                urlretrieve(url, fpath)
            except URLError as e:
                raise Exception(error_msg.format(url, e.errno, e.reason))
            except HTTPError as e:
                raise Exception(error_msg.format(url, e.code, e.msg))
        except (Exception, KeyboardInterrupt):
            if os.path.exists(fpath):
                os.remove(fpath)
            raise

        if file_hash is not None:
            assert _validate_file(fpath, file_hash), 'Hash of downloaded file incorrect.'

    return fpath

# def _get_filepath(filename, url, cache_dir, cache_subdir='datasets', file_hash=None):
#     """Pulls file from the internet."""

#     # handle '~' in path
#     datadir_base = os.path.expanduser(cache_dir)

#     # ensure that directory exists
#     datadir = os.path.join(datadir_base, cache_subdir)
#     if not os.path.exists(datadir):
#         os.makedirs(datadir)

#     # handle case where cache is not writeable
#     if not os.access(datadir_base, os.W_OK):
#         datadir = os.path.join('/tmp', '.energyflow', cache_subdir)
#         if not os.path.exists(datadir):
#             os.makedirs(datadir)

#     fpath = os.path.join(datadir, filename)

#     # determine if file needs to be downloaded
#     download = False
#     if os.path.exists(fpath):
#         if file_hash is not None and not _validate_file(fpath, file_hash):
#             print('Local file hash does not match so we will redownload...')
#             download = True
#     else:
#         download = True

#     if download:
#         print('Downloading {} from {} to {}'.format(filename, url, datadir))

#         error_msg = 'URL fetch failure on {}: {} -- {}'
#         try:
#             try:
#                 urlretrieve(url, fpath)
#             except URLError as e:
#                 raise Exception(error_msg.format(url, e.errno, e.reason))
#             except HTTPError as e:
#                 raise Exception(error_msg.format(url, e.code, e.msg))
#         except (Exception, KeyboardInterrupt):
#             if os.path.exists(fpath):
#                 os.remove(fpath)
#             raise

#         if file_hash is not None:
#             assert _validate_file(fpath, file_hash), 'Hash of downloaded file incorrect.'

#     return fpath


def _hash_file(fpath, algorithm='sha256', chunk_size=131071):
    """Calculates a file sha256 or md5 hash.
    # Example
    ```python
        >>> from keras.data_utils import _hash_file
        >>> _hash_file('/path/to/file.zip')
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    ```
    # Arguments
        fpath: path to the file being validated
        algorithm: hash algorithm, one of 'auto', 'sha256', or 'md5'.
            The default 'auto' detects the hash algorithm in use.
        chunk_size: Bytes to read at a time, important for large files.
    # Returns
        The file hash
    """
    if (algorithm == 'sha256') or (algorithm == 'auto'):
        hasher = hashlib.sha256()
    else:
        hasher = hashlib.md5()

    with open(fpath, 'rb') as fpath_file:
        for chunk in iter(lambda: fpath_file.read(chunk_size), b''):
            hasher.update(chunk)

    return hasher.hexdigest()

def _validate_file(fpath, file_hash, algorithm='auto', chunk_size=131071):
    """Validates a file against a sha256 or md5 hash.
    # Arguments
        fpath: path to the file being validated
        file_hash:  The expected hash string of the file.
            The sha256 and md5 hash algorithms are both supported.
        algorithm: Hash algorithm, one of 'auto', 'sha256', or 'md5'.
            The default 'auto' detects the hash algorithm in use.
        chunk_size: Bytes to read at a time, important for large files.
    # Returns
        Whether the file is valid
    """
    if ((algorithm == 'sha256') or (algorithm == 'auto' and len(file_hash) == 64)):
        hasher = 'sha256'
    else:
        hasher = 'md5'

    return str(_hash_file(fpath, hasher, chunk_size)) == str(file_hash)


def _pad_events_axis1(events, axis1_shape):
    """Pads the first axis of the NumPy array `events` with zero subarrays
    such that the first dimension of the results has size `axis1_shape`.
    """

    if events.ndim != 3:
        raise ValueError('events must be a 3d numpy array')

    num_zeros = axis1_shape - events.shape[1]
    if num_zeros > 0:
        zeros = np.zeros((events.shape[0], num_zeros, events.shape[2]))
        return np.concatenate((events, zeros), axis=1)

    return events