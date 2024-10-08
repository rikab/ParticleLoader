import numpy as np

def center_and_normalize_zyphi(events):

    X = events[:,:,:3]

    for x in X:

        energies = x[:,0]
        etas = x[:,1]
        phis = x[:, 2]

        # translate such that the phi of the hardest particle is 0
        max_phi_index = np.argmax(energies)
        phis = phis - phis[max_phi_index]


        # # # Wrap the phis to be between -pi and pi
        phis = (phis ) % (2 * np.pi)
        phis_above_pi = phis > np.pi
        phis[phis_above_pi] = phis[phis_above_pi] - 2 * np.pi
        phis_below_minus_pi = phis < - np.pi
        phis[phis_below_minus_pi] = phis[phis_below_minus_pi] + 2 * np.pi
        # # phis = (phis ) % (2 * np.pi)

        x[:,0] = energies / np.sum(energies)
        x[:,1] = etas - np.average(etas, weights=energies)
        x[:,2] = phis - np.average(phis, weights=energies)


        # # # Wrap the phis to be between -pi and pi
        for i in range(10):

            phis = x[:,2]
            phis = (phis ) % (2 * np.pi)
            phis_above_pi = phis > np.pi
            phis[phis_above_pi] = phis[phis_above_pi] - 2 * np.pi
            phis_below_minus_pi = phis < - np.pi
            phis[phis_below_minus_pi] = phis[phis_below_minus_pi] + 2 * np.pi
            x[:,2] = phis - np.average(phis, weights=energies)

    return X


def normalize_4vectors(events):

    # Normalize such that each event has an energy of 1
    events[:, :, 1] /= np.sum(events[:, :, 0], axis=-1)[:, None]
    events[:, :, 2] /= np.sum(events[:, :, 0], axis=-1)[:, None]
    events[:, :, 3] /= np.sum(events[:, :, 0], axis=-1)[:, None]
    events[:, :, 0] /= np.sum(events[:, :, 0], axis=-1)[:, None]

    return events