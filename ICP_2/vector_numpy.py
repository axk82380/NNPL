import numpy as np

# created a random vector of size 20 with float values between 1 and 20
random_vector = np.random.uniform(low=1, high=20, size=20)
print(random_vector)
# reshape the array to 4 by 5 using reshape method
mat45 = random_vector.reshape(4, 5)
print(mat45)
# replace the max in each row by 0 using where method
mat45 = np.where(mat45 == np.amax(mat45, axis=1, keepdims=True), 0, mat45)
print(mat45)