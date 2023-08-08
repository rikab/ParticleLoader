# Top Dataset Downloader (v0.0.2)

Scripts to download and format the Top Tagging benchmark dataset as described in [1707.08966](https://arxiv.org/abs/1707.08966) and [1902.09914](https://arxiv.org/abs/1902.09914). The dataset is hosted [here](https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6). If you use this dataset, *please cite the original papers*.

The dataset consists of hadronic $t\bar{t}$ and QCD dijets generated using PYTHIA 8.2.15 at $\sqrt{s} = 14$ TeV. Multi-parton interactions and pileup are not included. A simulation of the ATLAS detector is performed using DELPHES. 

Jets are defined using the AK8 ("Fat Jet") algorithm in FastJet. For each event, only the leading jet is included in the dataset. Cuts are then applied: $p_{T,J} \in [550, 650]$ GeV and $|\eta_J| < 2$. For top jets, a top parton and its decay partons are additionally reuquired to be within $\Delta R = 0.8$ of the jet axis. For each jet, the 4-momentum of the leading 200 constituents are stored, zero-padded.

There are three files: ```train.h5```, ```test.h5```, and ```val.h5```, with 600k, 200k, and 200k jets respectively, for each class (top and QCD).

This code is based heavily off of the [energyflow package](https://github.com/pkomiske/EnergyFlow/).

## Usage

To load the dataset ```dataset``` (either "train", "test", or "val) from the directory ```dir```, use 

```
X_train, Y_train = load(cache_dir=dir, dataset=dataset, num_data = 250000)
```

If ```dir``` does not already contain the downloaded and formatted files, they will be downloaded and re-formatted to a numpy-readable format suitable for ML purposes.

The array ```X``` is an $N\times 200 \times 4$ numpy array of particles, and ```Y```is an $N \times 1$ array of integers: 0 for QCD, and 1 for top jets.

See ```example.ipynb``` for example usage.

## Installation

### From this repository locally

In your Python environment from the top level of this repository run

```
python -m pip install .
```

### From GitHub

In your Python environment run

```
python -m pip install "toploader @ git+https://github.com/rikab/TopDatasetDownloader.git"
``````

## Dependencies

The following python packages are required by the data formatter:

* numpy
* pandas
* urllib3
* tqdm


## Changelog

- v0.0.2: 8 August 2023. Pip-installable.
- v0.0.1: 31 July 2023. Initial release.

