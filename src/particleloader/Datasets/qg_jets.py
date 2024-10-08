from particleloader.Datasets.Dataset import Dataset


ZENODO_URLS = {
    '[generator:pythia][with_bc:False]': [  'https://zenodo.org/record/3164691/files/QG_jets.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_1.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_2.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_3.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_4.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_5.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_6.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_7.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_8.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_9.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_10.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_11.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_12.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_13.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_14.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_15.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_16.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_17.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_18.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_19.npz?download=1',],

    '[generator:pythia][with_bc:True]': [   'https://zenodo.org/record/3164691/files/QG_jets_withbc_0.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_1.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_2.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_3.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_3.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_4.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_5.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_6.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_7.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_8.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_9.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_10.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_12.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_13.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_14.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_15.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_16.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_17.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_18.npz?download=1',
                                            'https://zenodo.org/record/3164691/files/QG_jets_withbc_19.npz?download=1',],


    '[generator:herwig][with_bc:False]': [  'https://zenodo.org/record/3066475/files/QG_jets_herwig_0.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_1.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_2.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_3.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_4.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_5.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_6.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_7.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_8.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_9.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_10.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_11.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_12.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_13.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_14.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_15.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_16.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_17.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_18.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_19.npz?download=1',],
                                            
    '[generator:herwig][with_bc:True]': [   'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_0.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_1.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_2.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_3.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_4.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_5.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_6.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_7.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_8.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_9.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_10.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_11.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_12.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_13.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_14.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_15.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_16.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_17.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_18.npz?download=1',
                                            'https://zenodo.org/record/3066475/files/QG_jets_herwig_withbc_19.npz?download=1',]
}


hashes = {
    '[generator:pythia][with_bc:False]': [
                '3f27a02eab06e8b83ccc9d25638021e6e24c9361341730961f9d560dee12c257',
                '648e49cd59b5353e0064e7b1a3388d9c2f4a454d3ca67afaa8d0344c836ecb35',
                '09f7b16fa7edb312c0f652bb8504de45f082c4193df65204d693155017272fe9',
                '7dc9a50bb38e9f6fc1f11db18f9bd04f72823c944851746b848dee0bba808537',
                '3e6217aad8e0502f5ce3b6371c61396dfc48a6cf4f26ee377cc7b991b1d2b543',
                'b5b7d742b2599bcbe1d7a639895bca64c28da513dc3620b0e5bbb5801f8c88fd',
                '7d31bc48c15983401e0dbe8fd5ee938c3809d9ee3c909f4adab6daf8b73c14f1',
                'cec0d7b2afa9d955543c597f9b7f3b3767812a68b2401ec870caf3a2ceb98401',
                'e984620f57abe06fc5d0b063f9f84ba54bd3e8c295d2b2419a7b1c6175079ed4',
                '6e3b69196995d6eb3b8e7af874e2b9f93d904624f7a7a73b8ff39f151e3bd189',
                'fa3d386f230b806058ff17e5bd77326ff4bf01d72aa5eb3325c1df2a8825927c',
                'acd49ab7bea8f72ecf699a9a898bccacc8730474259d68406656a5a43d407fb0',
                '2edd55b8bc30c686a0637855e1ba068586eb97041e8114d5540d96db2a7a2e17',
                '7276a8a0e573f9795a47f9d5addc10d2af903c2a0ffa5c848a720ccae93daa90',
                '2068ecfa912e94cd3ce7273b7c77af0bbd5ec57940997e7483b56f03434a6869',
                '41a732ce6321dd593214225b03fb87329607ccae768c705e3896ffecc28bfcca',
                '9d68caeb18f3ccf127b9032f52e63ee011c4381293a3a503f894e5c0741ae215',
                '086053ca611bb04d97fa0b6509b4ffb6955421b067c7b277498f0e5188879331',
                'cdc595f5fedef7db9411a9f93f2786f110073b4d17a523700f625846588b1e44',
                'd07781139320ae134ce4824bc0cefa43fd5003cd97cdf3aed90d4fb12fad8a1d',
            ],
    '[generator:pythia][with_bc:True]': [
                '27978b5dfe38f860f9899a4213f115579766ece0f6b3cd1cc043f57483521f9c',
                'bec3a147167ac19f243d74c5c47097a716cee6f6af4edc16fd0b50003ec48bd7',
                '878e415001682fda5493f15f2aaa29bce3d60b5dd882f85d85f66f2e8c5ddf9d',
                'e6f48b8fa5dfb3fa914db5dbcabe6d972d803571aa5586babececa86007d0064',
                'e11f885b97b7e859792b3f0a748f15e89c8e8788d68d1256931c948b745945e1',
                '9598efe81b4d1f5f56049508da23957fd5c90590a242f7e58255aaa44d23c192',
                '1de06fccea886445cc4250aba8e3c10990ccb24d4ae6416c6f1f40811117c13e',
                'df6d44f5c37e5c1bf6a8c7cbfb9633413348c908b5f0c657ec32e8dde781ca95',
                'fa6a01f90cdf3394b77bdec7e1931b2dfa4d6670ad8fbc0266eb14c352456e93',
                'e8c7545edb1bc52a0ea0b6cf8541a3ab825970c337458e5c43402c13939e949d',
                '147a6f80eb191577092c3bc404c90ab5538e2887b23f27d6e91e3643c5a18119',
                'c1068b3ac7d0f94ec928538a451d9e20feb7b0281deb083661f8fc6bffa7c4f1',
                '78545b1517f099b0001f6dafe046a9d39a93d13e29db812f6fa415301bfa590d',
                '8d90ffc18358dfb234359804da6a37bb188fa45c9e24468b0cc91f24ba6e0a1d',
                '4ccdf00ef7948721bfe41cd61cb3eac2025e4869b226c9f22524cf2adb9ed2a0',
                'ca09495a8b5b27435d8523aaca6f3af6795a9a61c17d758be2c1c5560e5423f1',
                '00318c05ef530f7b2e867f4b1b9900e9535add46455f6fc39ad4777ff9c71e00',
                'a23c05633f18b1a047102943f550c8bb5cfc62135a2d543ccc7cdef333996f5c',
                '0883dcd7feebef2f6419ca084b9ecc0c28c5ada68eb56f6062a943d3fe4bad81',
                'e60a6c2bac382f51147b8587119b589b134f39724fec598e28193c9b03f70fa5',
            ],
       

    '[generator:herwig][with_bc:False]': [
                '0527349778c0ab2f7da268975fb9e7c0705c88d60f2c478401d941b9913f4d44',
                '65ef3b4cced4e2618c2bf8f3c66ef707dbd7a9740825f93549732d64e60d7ea8',
                'f13dab1937e40d0c05b97e9813fb4dda5156a8f6b4e41a89cc13821d02a60f58',
                '7b55e26262f2c156b15014b796d0a7e7a5254a982170f45cf2d9857b1f23b5f7',
                '3a5006da4a05192636a74fc818256fce215970c626719738cae9f82e3f068646',
                '2601564aee41aa5851392d6b3d12021f978fa17199e42dde004e35d1175055ea',
                '2c1fc34e99816a0bb5a84f68fa42f6314252521f6b32384a118cdec872ea97a1',
                '4b05f17acb046ad50232987003b89a91800cc713eefd81142ffeb42259369fb2',
                '150cbe132a2ee3178ba3a93a6b1733b3498b728db91f572295b6213d287ec1f7',
                '7d74c90843c751ade4cac47f6c2505da8bcbaf8645bc3f9870bdca481ff805fd',
                'e2b9072da8436618c602fbcf2409fe9be9a46dea7cff1fcc36f1ba8fefa6842d',
                'c69f499b7ea09029da7e78dcc527feca6b1680685e3c9a481db292d5518e3f1c',
                'db25d85d3a35978c607f9b5b0b52f4140c984eb5a5ab236cbf3e6eb34ead761c',
                '9a51ddd383e32154fc504ddcb138e54f0f1bd35079fe5cfa9139839c229cd78e',
                'be0fa462ea907d36972c8573b9a2f6bcdf5cf66648fa397739d12ecb677948e5',
                '7b17400c6867243e8137bd97e0f9743682a5d8c772685a6654f42f1fa2731960',
                '4c484f6508180c0e4e4a5c90b37d1b15cc67afaa3c5998306e8e633848ce6dfc',
                'd1f9baf3a3a148080d1735130f6b18f0f598991a8d886eff3c427b2e2265fce1',
                'bb70219d78e1d92091efacbf933da632670c8318d00777e4144d9a0c782e5749',
                '94975b3d999868485780d2d9e4330273aa8f0db4b9a7f6094d360f637659a264',
            ],

    '[generator:herwig][with_bc:True]': [
                '173b2ee0c5466772997d6b9f6a8ce25531ae3666ee17e73df1807a707aefbb17',
                'd63f272b7a5be9b75ba26082eb76107e882b756a2285cab0c16ed69d77c16366',
                '59369e725de3f688b231993bc7fbca45c2c1cc1da252aee5160298e83ce303cf',
                'bf5f2e8d6ce306796dc4e3ce9e6a88faa6ddb9b482b714060a11aa257b0fe1e6',
                'db5f5dd682f6f48e1b4900e2f366eddbb4089cb14f745cd2fcc79b23ff9f8104',
                '03833b850fa2c1ad050c753b7be9e08086bbb2b55ae41dfc1921c617cc85a622',
                'a7f94530366d886ab16adbb786671782dc4001e76ffb87937e65852449fe4f9c',
                '0c1f326807a5d5d57398aec6c5816d7c9dc644fd80e56af876fa011b139cb163',
                '1f272ba63ccf9d0af72add26075e9fc6c57e4bb954a2a31a542c06d328061742',
                'd36cd5bbaf84a4b01faa807489133ad5ca283f64f1602e724684f1e1c2996be6',
                'a4e735dcf69de0e635974a5eafb14e7cfa894e2db29a342f04be8660dc8f190f',
                'c3b293be7c5cc45f65a94835d4f8c6920abe9b5c8f4baa3f10afe1dfd0112af0',
                '2a1b54e081692eae967f117f6e8867a46f5d7d7a9d7c9353342d3cb72414d62c',
                '6a7e846baccc8076563ed6bcb5349c2f07c4802ffeefed7fe3350680d49fc9a9',
                'fb203a1273e9ecf93176cb63123f4a5ae39d803322bbd666679651715e1c8617',
                'b9493efda0e3e1c4fdcb684486b1157d73a9ca9f29142125cded06d5a85b5df4',
                '1a8e6fcefb81805d7f22bffa5b45a71d9a0fcb97a490d1866865ea7196d94443',
                '2e961954b1ca4642cc2434789e61cd0e2eb8f18f8e77b120950de1c81ed94a15',
                '34129cd813aa54539837ad57e484206f20f1da0330ae5fab6b378707ea41ca25',
                '3895ad282094f3c248bdee5ff1c57247476f03accafd573b60e0ac0d0463fe0b',
            ],

}

qg_jets = Dataset(
    name = 'qg_jets',
    description = 'Quark and Gluon jets',
    NUM_PER_FILE = 100000,
    NUM_FILES = 20,
    options = {"generator" : ["pythia", "herwig"], "with_bc" : [False, True]},
    sources = ['zenodo', 'dropbox'],
    shapes = ['(200, 2)', '(1,)'],
    npz_keys=['X', 'y'],
)

qg_jets.add_url('zenodo', ZENODO_URLS)
qg_jets.add_hash(hashes)
