# Particle Dataset Downloader (v0.0.7)

A package for downloading a repository of particle physics datasets. All datasets can be accessed with a single line:

```
from particleloader import load
Data = load(DATASET_NAME, N_samples, cache_dir=dir)
``` 

See ```example.ipynb``` for detailed example usage.


## Public Datasets:

As of the latest release, the public datasets are:

* **Quark/Gluon Jets:** `qg_jets`, a dataset of quark and gluon jets with labels generated in Pythia or Herwig, with the option of including _b_ and _c_ quarks.
* **Top/QCD Jets:** `topqcd_jets`, a dataset of quark and gluon jets with labels generated in Pythia or Herwig.
* **SPECTER LEP dijets:** `SPECTER_ee_dijets`, a dataset of LEP-like e+e- collisions to hadrons generated in Pythia, as used in arxiv:2410:XXXXX
* **SPECTER QCD jets:** `SPECTER_qcd_jets`, a dataset of QCD jets generated in Pythia, as used in arxiv:2410:XXXXX
* **SPECTER Top jets:** `SPECTER_top_jets`, a dataset of top jets generated in Pythia, as used in arxiv:2410:XXXXX

It is relatively straightforward to add new datasets. If you have a dataset you would like to add, please let me know!


## Installation

### From this repository locally

In your Python environment from the top level of this repository run

```
python -m pip install .
```

### From GitHub

In your Python environment run

```
python -m pip install "particleloader @ git+https://github.com/rikab/ParticleLoader.git"
``````

## Dependencies

The following python packages are required by the data formatter:

* numpy
* urllib3


## Changelog

- v0.0.7: 8 October 2024. SPECTER Datasets.
- v0.0.6: 26 August 2024. SPECTER e+e- dijets.
- v0.0.5: 14 August 2024. Overhaul, multiple datasets (top/qcd and q/g).
- v0.0.3: 9 August 2023. Minor Bug Fixes.
- v0.0.2: 8 August 2023. Pip-installable.
- v0.0.1: 31 July 2023. Initial release.
