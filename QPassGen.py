from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np
import random
import string

qc = QuantumCircuit(4)
qc.h(range(4))
qc.measure_all()

simulator = AerSimulator()
result = simulator.run(qc, shots=100).result()
counts = result.get_counts()

plt.figure(figsize=(8, 6))
plt.bar(counts.keys(), counts.values(), color='blue', alpha=0.7)
plt.title('Quantum States Distribution')
plt.xlabel('States')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

sorted_bits = sorted(counts.items(), key=lambda x: -x[1])
binary_password = sorted_bits[0][0]
seed = int(binary_password, 2)
random.seed(seed)
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(chars, k=12))

print(f"\nGenerated Password: {password}")

length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

print("\nPassword Analysis:")
print(f"Length: {length}")
print(f"Has Uppercase: {has_upper}")
print(f"Has Lowercase: {has_lower}")
print(f"Has Numbers: {has_digit}")
print(f"Has Special: {has_special}")

char_space = (26 * has_upper) + (26 * has_lower) + (10 * has_digit) + (32 * has_special)
entropy = length * np.log2(char_space)
print(f"Password Entropy: {entropy:.2f} bits")

years = (2**entropy) / (1_000_000_000 * 365 * 24 * 60 * 60)
print(f"Crack Time: {years:.2e} years at 1B attempts/sec")
