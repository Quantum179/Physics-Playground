# source : https://qiskit.org/documentation/getting_started.html

import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_city

q = QuantumRegister(3, 'q')

circ = QuantumCircuit(q)

circ.h(q[0])
circ.cx(q[0], q[1])
circ.cx(q[0], q[2])

%matplotlib inline
circ.draw(output='mpl')

backend = BasicAer.get_backend('statevector_simulator')
job = execute(circ, backend)
result = job.result()

outputstate = result.get_statevector(circ, decimals=3)

plot_state_city(outputstate)


