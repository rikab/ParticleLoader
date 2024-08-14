from particleloader.Datasets.Dataset import Dataset



DROPBOX_URLS = {
                '[generator:pythia]': [
                "https://www.dropbox.com/scl/fi/aum3n73ljsjz33lm5pnyv/top_qcd_0.npz?rlkey=1mexso8rrpd8vc8efmnnuvo89&st=ck5twtrx&dl=1",
                "https://www.dropbox.com/scl/fi/l2bq9k7oaj6m0rls0x08w/top_qcd_1.npz?rlkey=sh9nvgwvi4c3z6t5b01nebkw3&st=ydmv85mo&dl=1",
                "https://www.dropbox.com/scl/fi/e3ycn7er6w8cy7ks7ri9j/top_qcd_2.npz?rlkey=pu03t4cmvn5o0hf1ofz2rjjmb&st=opi4yo28&dl=1",
                "https://www.dropbox.com/scl/fi/a1iq44na61wknrj7hf51m/top_qcd_3.npz?rlkey=jucqw4i7jno7mcthnzs66qtll&st=tdxc8yx6&dl=1",
                "https://www.dropbox.com/scl/fi/lacfom7a73wfoyytm02bx/top_qcd_4.npz?rlkey=jnnl4f2nh3bylh7am9b6kzfu9&st=dcqwwot4&dl=1",
                "https://www.dropbox.com/scl/fi/rmaupsu9z3l1aisckkkvt/top_qcd_5.npz?rlkey=90mb9j4j6ta2potv0iupv05pm&st=8w5202wf&dl=1",
                "https://www.dropbox.com/scl/fi/37uc5gzx7usyalkrioj3d/top_qcd_6.npz?rlkey=1by99mkw4ma48hww0a4ctgfsz&st=wvapmdx2&dl=1",
                "https://www.dropbox.com/scl/fi/jdp54simulesgr1y0fo7e/top_qcd_7.npz?rlkey=uc4je74fm4x06aq7xdkxrdcnl&st=l664f8i5&dl=1",
                "https://www.dropbox.com/scl/fi/kdub3i3676x5epd2jhvup/top_qcd_8.npz?rlkey=3g573uo7ce4p5lbjtkglz7k0z&st=kn4cdtdp&dl=1",
                "https://www.dropbox.com/scl/fi/bw21ja2s3ciwj3yazgiry/top_qcd_9.npz?rlkey=5w29s82y2g8qv1rc1zf0tuhzh&st=k2i9vrjo&dl=1",
                ],

                '[generator:herwig]': [
                "https://www.dropbox.com/scl/fi/v7uzc3as40dqo728qua3o/top_qcd_0.npz?rlkey=jz7za5g4tier5miaurys0rpnx&st=vskvs6m6&dl=1",
                "https://www.dropbox.com/scl/fi/f1m5bheelzedl003gpaod/top_qcd_1.npz?rlkey=v82ty3el09h49puwa1rt78wsb&st=u7avplrq&dl=1",
                "https://www.dropbox.com/scl/fi/u23stfxto9nt2p3o6kyvc/top_qcd_2.npz?rlkey=1azuanyrxdsun1djks9lm5h1m&st=gft8tec6&dl=1",
                "https://www.dropbox.com/scl/fi/y5qzvdxw8no9nw91kxq5t/top_qcd_3.npz?rlkey=ssmcet7mdpfyh9cu0vhpwaq0j&st=l3bddsb2&dl=1",
                "https://www.dropbox.com/scl/fi/wv45rhq40iqomexrqzwzc/top_qcd_4.npz?rlkey=0awnlevcb03h36epkhs3gk25n&st=e67bc4w0&dl=1",
                "https://www.dropbox.com/scl/fi/otzwe04s2sure829ze1ix/top_qcd_5.npz?rlkey=5r36j1za6ovqbf7m41al9rwms&st=ylfp8np3&dl=1",
                "https://www.dropbox.com/scl/fi/7pc9a7ytrbxx5csw4h21g/top_qcd_6.npz?rlkey=ibf3ctoyljidqf51drwuk2kp1&st=dw8xkxld&dl=1",
                "https://www.dropbox.com/scl/fi/ab1ho82k6h5ky9brghw0s/top_qcd_7.npz?rlkey=hs9fkgioggf6tbzbaqqhhw43j&st=eiq9veos&dl=1",
                "https://www.dropbox.com/scl/fi/704i8xe3738gvjieq707y/top_qcd_8.npz?rlkey=zgw6ydo44imm8m9tewc9ajshw&st=fsj6ihki&dl=1",
                "https://www.dropbox.com/scl/fi/16tdv9xi9y6dcf6ig1pec/top_qcd_9.npz?rlkey=ikhjykqmooencz5ttndhysejp&st=y5z3zq6k&dl=1",
                ],

}

hashes = {"[generator:pythia]": ["098301f3d196c8703327244810b5c920d5284fef3316ac8cafef0ff32b1360b6", "6944207b8e53fe1a90659bb5ba32a2e0940f8df1ccc58d8c6697aa26f9114266", "6f84603f8964f4e3b8cf0adc642023c2f412330c8b052da2a67959215e4fb1d6", "c33d1f5941be961f7e015185e707a7db145c14fd0474167ceea5d81f98c9932c", "a7fbdd0b68f18e5a9e83cef7c0722cd75506f029f84a038088a35a467d6b25e1", "994dc7dd447f7ffa0ad5e0ebcf00a91dd216f16cd2c53dfdec9aef1125a4ff15", "280e0f99869157be841a7ae6f987a6cc0dc933ecad9df4ee749449b3e12fba86", "d6f4582f879cadb72875c9c32397f8cf4efc6bdd0dc3d21f487e5845f1a7ea53", "03997850312321d512d2fc6567da99780e8041c12a9ed48c1b1682b95d793ab3", "63a2e76e2d206e541e9762ed5f16b39e10be6fc6625dd6f265abbcf49ebb3ce5"], "[generator:herwig]": ["4c9a4e5e01371319b8316785e5ee6f7320ee44dfd00383b8fea6b84237aea40c", "e96cd346ea6fa40b5df0bba6791469db8f638c7c9600def669e03ea045886798", "8503dbce2b3abcd95e73969f596ec557c91253bb7a3f4950919033ce533dfda1", "aa48700ede6156719bfc8f4d0cd61962007996c52d16019d48c45157fa85c82e", "c9d199ce1eb25c930c3dcb725ab0f675f97d9d97b539354c45d50718973c3438", "459eef6c6c719edcc3fa71581b56bc8e8c0776f8369f4ae1772f30de7453e2a1", "6ad15bb09abfd842c7bfde5efcad6e3dfcc47fa2ed8d5ee14fe7eb79663fd195", "ef8faddd3ca357e5a9c642b3da34bbbcae70d6fbd6b9fbc064e340ee9618f8cb", "cf0b50c4396ea335a09b9cc0ca6c952a5a3ccbac3578a835eaa891c1b826c2aa", "9a219c8185205ecb8a266166f20a90e2d1439148561ab879f8ef46337854d3cd"]}

topqcd_jets = Dataset(
    name = 'topqcd_jets',
    description = 'Top and QCD AK10 jets',
    NUM_PER_FILE = 200000,
    NUM_FILES = 10,
    options = {"generator" : ["pythia", "herwig"],},
    sources = ['dropbox'],
    shapes = ['(200, 4)', '(1,)'],
    npz_keys=['data', 'labels'],
)

topqcd_jets.add_url('dropbox', DROPBOX_URLS)
topqcd_jets.add_hash(hashes)
