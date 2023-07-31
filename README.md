# Top Dataset Downloader (v0.0.1)

Scripts to download and format the Top Tagging benchmark dataset as described in [1707.08966](https://arxiv.org/abs/1707.08966) and [1902.09914](https://arxiv.org/abs/1902.09914). The dataset is hosted [here](https://syncandshare.desy.de/index.php/s/llbX3zpLhazgPJ6). If you use this dataset, *please cite the original papers*.

The dataset consists of hadronic $t\bar{t}$ and QCD dijets generated using PYTHIA 8.2.15 at $\sqrt{s} = 14$ TeV. Multi-parton interactions and pileup are not included. A simulation of the ATLAS detector is performed using DELPHES. 

Jets are defined using the AK8 ("Fat Jet") algorithm in FastJet. For each event, only the leading jet is included in the dataset. Cuts are then applied: $p_{T,J} \in [550, 650]$ GeV and $|\eta_J| < 2$. For top jets, a top parton and its decay partons are additionally reuquired to be within $\Delta R = 0.8$ of the jet axis. For each jet, the 4-momentum of the leading 200 constituents are stored, zero-padded.

There are three files: ```train.h5```, ```test.h5```, and ```val.h5```, with 600k, 200k, and 600k jets respectively, for each class (top and QCD).

## Usage

To download the files to a directory ```dir```, use 

```
bash download.sh dir
```

If ```dir``` already contains ```train.h5```, ```test.h5```, or ```val.h5```, they will not be redownloaded.



