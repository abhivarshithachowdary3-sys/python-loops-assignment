#Task 1: Create an Array and Basic Math
import numpy as np

temps_celsius = np.array([22, 25, 28, 24, 26])

temps_fahrenheit = temps_celsius * 1.8 + 32

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

avg_fahrenheit = np.round(np.mean(temps_fahrenheit), 1)
print("Average Fahrenheit:", avg_fahrenheit)

#Task 2: Array Shape and Statistics

import numpy as np

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
print("Range:", np.max(scores) - np.min(scores))

#Task 3: Performance Comparison

import numpy as np
import time

arr_np = np.arange(1, 50001)

arr_list = list(range(1, 50001))

start_np = time.time()
sum_np = np.sum(arr_np)
end_np = time.time()
time_np = end_np - start_np

start_list = time.time()
sum_list = sum(arr_list)
end_list = time.time()
time_list = end_list - start_list

print("NumPy sum:", sum_np)
print("Python sum:", sum_list)
print(f"NumPy time: {time_np:.4f} seconds")
print(f"Python time: {time_list:.4f} seconds")
print(f"NumPy is {time_list/time_np:.1f}x faster")
