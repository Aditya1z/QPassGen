# QPassGen

A sophisticated password generator that leverages quantum computing principles through IBM's Qiskit framework to create cryptographically secure passwords.

## Project Overview

QPassGen utilizes quantum superposition and measurement principles to generate truly random passwords. By implementing quantum circuits with Qiskit, this project provides:
- Real-time quantum state visualization
- Comprehensive password strength analysis
- Entropy calculation
- Brute-force resistance estimation

## Features

- Quantum circuit-based random number generation
- Advanced password strength assessment
- Quantum state distribution visualization
- Security metrics calculation
- Configurable password parameters
- Entropy-based security analysis

## Technical Requirements

- Python 3.10
- Qiskit
- Qiskit-aer
- NumPy
- Matplotlib
- String (Python standard library)
- Random (Python standard library)

## Installation

1. Clone the repository:
```bash
https://github.com/Aditya1z/QPassGen.git
cd quantum-password-generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the password generator:
```python
python qpassgen.py
```

The program will:
1. Generate a quantum circuit
2. Create quantum state distribution
3. Generate a secure password
4. Provide security analysis

## Sample Output

```
Generated Password: k%9_zy(9C#L,

Password Analysis:
Length: 12
Has Uppercase: True
Has Lowercase: True
Has Numbers: True
Has Special: True
Password Entropy: 78.66 bits
Crack Time: 1.51e+07 years at 1B attempts/sec
```

## Implementation Details

The project implements:
- 4-qubit quantum circuit
- Hadamard gates for superposition
- Quantum measurement
- State vector analysis
- Password strength metrics
- Entropy calculation
- Crack-time estimation

## Security Features

- Quantum randomness
- Character set diversity
- Entropy assessment
- Brute-force resistance
- Special character inclusion
- Mixed case implementation

## Visualization

The project includes visualization of:
- Quantum state distribution
- Probability analysis
- State vector representation
- Security metrics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Aditya Raj

## Acknowledgments

- IBM Qiskit team for the quantum computing framework
- Quantum computing community for inspiration and support
