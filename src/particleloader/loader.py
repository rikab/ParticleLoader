from particleloader.Datasets import loader_dict
import numpy as np


def load(dataset_name, num_samples, cache_dir = "~/.ParticleLoader", **options):

    dataset = loader_dict[dataset_name]
    x = dataset.load(num_samples, cache_dir, **options)

    return x


def center_normalize_pt_eta_phi(X):
    '''
    Center and normalize the pt, eta, and phi of the jets.

    Args:
        X (np.array): Array of shape (N, Particles, 3-4) where N is the number of samples, Particles is the number of particles in each sample, and 3-4 is the pt, eta, phi, and possibly mass of each particle.
    '''



    # Sort the particles by pt
    X = X[np.argsort(X[:,:,0], axis=1)]

    # Center phi such that the highest pt particle is at phi = 0
    X[:,:,2] = X[:,:,2] - X[:,-1,2][:,None]

    # Normalize so the sum of pt is 1
    X[:,:,0] = X[:,:,0] / np.sum(X[:,:,0], axis=1)[:,None]

    # Center eta and phi such that the energy weighted average is 0
    X[:,:,1] = X[:,:,1] - np.average(X[:,:,1], weights=X[:,:,0], axis=1)[:,None]
    X[:,:,2] = X[:,:,2] - np.average(X[:,:,2], weights=X[:,:,0], axis=1)[:,None]

    return X

    



