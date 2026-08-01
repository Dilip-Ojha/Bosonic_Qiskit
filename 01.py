import bosonic_qiskit as c2qa
from bosonic_qiskit import CVCircuit, QumodeRegister
from qiskit import QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

# 1. Create registers
qmr = QumodeRegister(num_qumodes=1, num_qubits_per_qumode=3)  # 1 mode, max 4 bosons
qr  = QuantumRegister(1)                         # 1 ancilla qubit
cr  = ClassicalRegister(1)                        # 1 classical bit

# 2. Build CVCircuit (extends QuantumCircuit)
circ = CVCircuit(qmr, qr, cr)

# 3. Initialize qumode in Fock state |2⟩ using cv_initialize
circ.cv_initialize([0, 0, 1, 0, 0], qmr[0])  # |2⟩ state
# 4. Apply a displacement gate D(alpha)
#circ.cv_d(alpha=1.0, qumode=qmr[0])

# 5. Measure the qumode (Fock basis measurement)
circ.measure(qr[0], cr[0])

# 6. Simulate
simulator = AerSimulator()
result = simulator.run(circ, shots=1024).result()
counts = result.get_counts()
print(counts)