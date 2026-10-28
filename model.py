import numpy as np

def beam_energy(gamma):
    """Calculate electron beam energy in MeV."""
    return gamma * 0.511

print(beam_energy(1000))

def gamma_from_energy(energy):
    """Convert beam energy in MeV to gamma."""
    return energy / 0.511

def kinetic_energy(gamma):
    """Calculate electron kinetic energy in MeV."""
    return (gamma - 1) * 0.511
