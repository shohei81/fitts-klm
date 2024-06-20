import numpy as np

w = 50
d = 100

ID = np.log2((d / w) + 1)

MT = 167.48 + ID * 185.42

print(f"ID: {ID}")
print(f"MT: {MT}")