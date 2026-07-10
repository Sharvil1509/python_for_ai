import numpy as np

# Random integer
print("Random Integer:")
print(np.random.randint(1, 10))

# Random 1D array
print("\nRandom Array:")
print(np.random.randint(1, 100, size=5))

# Random 2D array
print("\nRandom Matrix:")
print(np.random.randint(1, 10, size=(3, 4)))

# Using seed
print("\nUsing Seed:")
np.random.seed(42)
print(np.random.randint(1, 100, size=5))

np.random.seed(42)
print(np.random.randint(1, 100, size=5))