from particleloader.Datasets.Dataset import Dataset



DROPBOX_URLS = {
                '[generator:pythia]': [
                "https://www.dropbox.com/scl/fi/6kvdyoork4ih5wv0605xp/top_jets.npy?rlkey=26anxr6t2comfsc6g001hlsbq&st=fy4g1uk6&dl=1",
                ],

}




hashes = {'[generator:pythia]': ['d9a73fe3d9b75bef36b22bfe93bed2379266076172f2bb7a06d621af4842578d']}

top_jets = Dataset(
    name = 'SPECTER_top_jets',
    description = 'Top jets in Pythia [Used in SPECTER paper]',
    NUM_PER_FILE = 100000,
    NUM_FILES = 1,
    options = {"generator" : ["pythia",],},
    sources = ['dropbox'],
    shapes = ['(200, 4)'],
)



top_jets.add_url('dropbox', DROPBOX_URLS)


# print(top_jets.download_all("dropbox"))

top_jets.add_hash(hashes)
