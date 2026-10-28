import numpy as np
from model import kinetic_energy

assert np.isclose(kinetic_energy(1), 0.0)
assert np.isclose(kinetic_energy(1000), 510.489)

print("All tests passed.")
