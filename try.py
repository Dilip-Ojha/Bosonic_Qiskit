import bosonic_qiskit as c2qa
import numpy as np
from bosonic_qiskit import CVCircuit, QumodeRegister
from qiskit_aer import AerSimulator

# 1. Use a sane number of qubits. 
# 5 qubits = 32 levels, which easily handles alpha=2.0
num_qubits = 5
qmr = QumodeRegister(1, num_qubits)
circ = CVCircuit(qmr)

# 2. Create the coherent state using a displacement gate.
# This is physically identical to "initializing" a coherent state.
circ.cv_d(2.0, qmr[0])

# 3. Apply Kerr nonlinearity
circ.cv_kerr(np.pi/4, qmr[0])

# 4. Simulate
sim = AerSimulator(method='statevector')
result = sim.run(circ).result()
sv = result.get_statevector()

# 5. Plotting (Using the correct 'utils' path)
# If this fails, try: print(dir(c2qa.utils)) to check the exact name
try:
    c2qa.utils.plot_wigner(sv, qmr[0], xmax=5)
except AttributeError:
    print("Could not find plot_wigner. Check c2qa.utils contents.")