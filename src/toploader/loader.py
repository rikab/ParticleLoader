import os
import warnings
import numpy as np
import pandas

from urllib.request import urlretrieve

tqdm_flag = True
try:
    from tqdm import tqdm
except:
    tqdm_flag = False

# File Locations
URLS = {"train": "https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=train.h5",
        "test": "https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=test.h5",
        "val": "https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6/download?path=%2F&files=val.h5",
        }

# Total number of jets
NUM_PER_FILE = 100000
NUM_TRAIN_JETS = 12*NUM_PER_FILE
NUM_VAL_JETS = 4*NUM_PER_FILE
NUM_TEST_JETS = 4*NUM_PER_FILE
MAX_NUM_FILES = {"train" : 12, "test": 4, "val" : 4}

DATASETS = ["train", "test" ,"val"]


def load(num_data = 100000, dataset = "train", cache_dir = "topdata", remove_raw_files = False):
    """Loads samples from the dataset (which in total is contained in twenty 
    files of 100k jets each). Any file that is needed that has not been cached will be 
    automatically downloaded. Downloading a file causes it to be cached for
    later use. 

    **Arguments**

    - **num_data** : _int_
        - The number of events to return. A value of `-1` means read in all
        events.
    - **dataset** : _str_
        - Specifies which dataset to load.
        Currently, the options are `'train'`, `'test'`, and `'val'`.
    - **cache_dir** : _str_
        - The directory where to store/look for the files.
    - **remove_raw_files** : _bool_
        - If set to True, will delete the raw downloaded .h5 files (1.6GB across the three files) after the numpy formatting.
        
    **Returns**

    - _3-d numpy.ndarray_, _1-d numpy.ndarray_
        - The `X` and `Y` components of the dataset as specified above.
    """

    # check for valid options
    if dataset not in DATASETS:
        raise ValueError("'dataset' must be in " + str(DATASETS))


    # get number of files we need
    num_files = int(np.ceil(num_data/NUM_PER_FILE)) if num_data > -1 else MAX_NUM_FILES[dataset]
    if num_files > MAX_NUM_FILES[dataset]:
        warnings.warn('More data requested than available. Providing the full dataset.')
        num_files = MAX_NUM_FILES[dataset]
        num_data = -1

    # Format directory and check existance
    try:
        datadir = os.path.expanduser(cache_dir)
    except:
        datadir = cache_dir
    if not os.path.exists(datadir):
        raise Exception(f"Cache directory {datadir} does not Exist!")        

    # Check if files exist -- if not, format and download
    filepaths = []
    for file_num in range(num_files):

        filename = f"{dataset}_{file_num}.npz"
        filepath = os.path.join(datadir, filename)

        file_exists = os.path.exists(filepath)

        if not file_exists:
            print(f"File {filepath} not found, formatting from downloaded data ...")
            f = download_and_format(dataset, file_num, datadir)
        else:
            f = filepath
        filepaths.append(f)
        
    # Remove files
    if remove_raw_files:
        raw_path = os.path.join(datadir, f"{dataset}.h5")
        if os.path.exists(raw_path):
            os.remove(raw_path)

    # Load jets
    Xs, Ys, = [], []
    for filepath in filepaths:
        f = np.load(filepath, allow_pickle=True) 
        Xs.append(f['x'])
        Ys.append(f['y'])


    return np.concatenate(Xs)[:num_data], np.concatenate(Ys)[:num_data]


def download_and_format(dataset, file_num, datadir):
    """Pulls file from the internet and formats into numpy arrays"""

    raw_file = f"{dataset}.h5"
    raw_path = os.path.join(datadir, raw_file)

    # If the raw file does not exist, download it
    if not os.path.exists(raw_path):
        print(f"Raw data not found at {raw_path}, downloading ...")
        urlretrieve(URLS[dataset], raw_path)
        url = URLS[dataset]
        print(f"Downloading from {url} ...")


        try:
            urlretrieve(url, raw_path)
        except (Exception, KeyboardInterrupt):
            if os.path.exists(raw_path):
                os.remove(raw_path)
            raise


    # Which events to download
    start = file_num * NUM_PER_FILE
    stop = (file_num + 1) * NUM_PER_FILE

    # Load .h5 file using pandas
    table = pandas.read_hdf(raw_path, "table", start = start, stop = stop)

    # Format 4-vectors
    X = np.zeros((table.shape[0], 200, 4) , dtype = np.float32)
    Y = table["is_signal_new"]

    for i in tqdm(range(200)):


        # pt
        X[:,i,0] = np.sqrt(np.square(table["PX_%d" % i]) + np.square(table["PY_%d" % i]))
        mask = X[:,i,0] > 0
        temp = table[table["E_%d" % i]> 0]

        X[mask,i,1] = 0.5 * np.log(  np.divide( np.add(temp["E_%d" % i] , temp["PZ_%d" % i]) , np.subtract(temp["E_%d" % i] , temp["PZ_%d" % i])  ) )
        X[mask,i,2] = np.arctan2(temp["PY_%d" % i] ,temp["PX_%d" % i])
        X[:,i,3] = np.nan_to_num(np.sqrt(np.square(table["E_%d" % i]) - np.square(table["PX_%d" % i]) - np.square(table["PY_%d" % i]) - np.square(table["PZ_%d" % i])))

    filename = f"{dataset}_{file_num}.npz"
    filepath = os.path.join(datadir, filename)
    np.savez(filepath, x=X,y=Y)
    return filepath
