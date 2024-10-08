from particleloader.Datasets.Dataset import Dataset



DROPBOX_URLS = {
                '[generator:pythia]': [
                "https://www.dropbox.com/scl/fi/9c621ejmppd1fs07j8v26/qcd_jets.npy?rlkey=fbqj25by8la998ynl4nomvk9l&st=qgmojxie&dl=1",
                ],

}




hashes = {'[generator:pythia]': ['4a14e9a6959ee60d4705b3300322154a132bd350acf2b29fa09e276354acd0ae']}

qcd_jets = Dataset(
    name = 'SPECTER_qcd_jets',
    description = 'QCD jets in Pythia [Used in SPECTER paper]',
    NUM_PER_FILE = 100000,
    NUM_FILES = 1,
    options = {"generator" : ["pythia",],},
    sources = ['dropbox'],
    shapes = ['(200, 4)'],
)



qcd_jets.add_url('dropbox', DROPBOX_URLS)


# print(qcd_jets.download_all("dropbox"))

qcd_jets.add_hash(hashes)
