from qiskit_nature.drivers.second_quantization.pyscfd import PySCFDriver
from qiskit_nature.drivers import UnitsType
from qiskit_nature.problems.second_quantization.electronic import ElectronicStructureProblem
from qiskit_nature.mappers.second_quantization import ParityMapper, BravyiKitaevMapper, JordanWignerMapper
from qiskit_nature.converters.second_quantization import QubitConverter
import numpy as np


def print_pauli_op(dist):
    driver = PySCFDriver(atom='H .0 .0 .0; H .0 .0 ' + str(dist),
                        unit=UnitsType.ANGSTROM,
                        basis='sto3g')
    problem = ElectronicStructureProblem(driver)
    second_q_ops = problem.second_q_ops()
    main_op = second_q_ops[0]
    num_particles = problem.num_particles
    num_spin_orbitals = problem.num_spin_orbitals
    mapper = ParityMapper()
    converter = QubitConverter(mapper=mapper, two_qubit_reduction=True)
    qubit_op = converter.convert(main_op, num_particles=num_particles)
    print("Pauli strings are: \n", qubit_op)
    return 0

if __name__ == '__main__':
    print_pauli_op(0.7)
    
# Different options for Mapper: ParityMapper, BravyiKitaevMapper, JordanWignerMapper
# Different options for basis: '321g','sto6g','431g'