import bosonic_qiskit as c2qa
from qiskit import QuantumRegister, ClassicalRegister

# 1 qumode (with cutoff 2^6 = 64 levels)
qmr = c2qa.QumodeRegister(num_qumodes=1, num_qubits_per_qumode=6)

# 1 qubit
qbr = QuantumRegister(1)

# classical bit
cr = ClassicalRegister(1)

# circuit
circuit = c2qa.CVCircuit(qmr, qbr, cr)