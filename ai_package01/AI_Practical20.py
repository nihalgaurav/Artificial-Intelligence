import numpy as np
print("Transcendental functions : ", "-"* 50)

a = np.arange(0, 6)

print(np.sin(a))

print(np.log(a))

print(np.exp(a))

# shape mismatch error

a = np.arange(4)

print(a + np.array([1, 2])) #error
