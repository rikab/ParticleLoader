from particleloader.Datasets.Dataset import Dataset



DROPBOX_URLS = {
                '[generator:pythia]': [
                "https://www.dropbox.com/scl/fi/hqnajyv4op837xyd3mio6/lep_dijets.npy?rlkey=wf7ohsfpbzjthzg3ofd7lm06t&st=vxstqjkq&dl=1",
                ],

}




hashes = {'[generator:pythia]': ['de43ca31853a5cce12984c1636499f24624025584963c7d5f8636cd2407544e0']}

ee_dijets = Dataset(
    name = 'SPECTER_ee_dijets',
    description = 'LEP Z-pole ee dijets in Pythia [Used in SPECTER paper]',
    NUM_PER_FILE = 100000,
    NUM_FILES = 1,
    options = {"generator" : ["pythia",],},
    sources = ['dropbox'],
    shapes = ['(500, 4)'],
)



ee_dijets.add_url('dropbox', DROPBOX_URLS)


# print(ee_dijets.download_all("dropbox"))

ee_dijets.add_hash(hashes)
