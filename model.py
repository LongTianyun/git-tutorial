import numpy as np

def beam_energy(gamma):
    """Calculate electron beam energy in MeV."""
    return gamma * 0.511

print(beam_energy(1000))
