import numpy as np
import bosonic_qiskit
from bosonic_qiskit import CVCircuit, QumodeRegister
import bosonic_qiskit.util as util
from qiskit_aer import AerSimulator

# --- Setup ---
cutoff = 20  # enough levels for α=2 coherent state (Poisson, peaks at n=4)
qmr = QumodeRegister(1, cutoff)
circ = CVCircuit(qmr)

# --- Prepare coherent state |α=2⟩ by displacing vacuum ---
circ.cv_d(alpha=2.0, qumode=qmr[0])

# Optionally apply more gates after this
# e.g. Kerr nonlinearity to evolve into a cat state over time:
#circ.cv_kerr(chi=np.pi/4, qumode=qmr[0])

# --- Simulate ---
# util.simulate() is the correct helper — handles statevector internally
result, sv = util.simulate(circ)

# --- Visualize Wigner function ---
# util.wigner() computes the phase-space distribution
xvec = np.linspace(-5, 5, 200)
W = util.wigner(sv, qmr, qmr[0], xvec, xvec)
util.plot_wigner(W, xvec, xvec)
