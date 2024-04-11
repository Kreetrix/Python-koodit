import numpy as np

# 1.
# a

print(np.degrees(2.493))
print(np.degrees(0.911))

# 2
# b
print(np.radians(137.7))
print(np.radians(62.3))

# 3
degree = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for x in degree:
    print(f'{x}° | {np.radians(x)} |')
    print("-------------------------")