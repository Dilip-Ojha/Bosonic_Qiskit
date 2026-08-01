# Jaynes-Cummings: H = ω·â†â + (Ω/2)·σz + g(â†σ⁻ + âσ⁺)
# Simulates a two-level atom coupled to a cavity mode

from qiskit import QuantumRegister
from bosonic_qiskit import CVCircuit, QumodeRegister
import numpy as np
cutoff = 10
qmr = QumodeRegister(1, cutoff)
qr  = QuantumRegister(1)  # the two-level atom (qubit)
circ = CVCircuit(qmr, qr)

# Initialize: cavity in |1⟩, atom in |e⟩ (excited)
circ.cv_initialize([0,1]+[0]*(cutoff-2), qmr[0])
circ.x(qr[0])  # put atom in |1⟩

# Jaynes-Cummings interaction for time t
# In bosonic-qiskit, use the Jaynes-Cummings gate
g = 0.1  # coupling strength
t = np.pi / (2 * g * np.sqrt(1))  # π-pulse time for |1⟩→|0⟩
circ.cv_jc(g, t, qubit=qr[0], qumode=qmr[0])

# Collapse: excitation transfers cavity→atom then back
print(circ.draw())
