import numpy as np
import pandas as pd

file_path = "/Users/shoheiyoshida/fitts-klm/log.csv"

# Read the CSV file starting from the correct row
buttons_df = pd.read_csv(file_path, header=None, names=['buttons', 'time', 'distance'])

# Extract the 'distance' column
distance = buttons_df['distance']
width = 50

# Calculate Index of Difficulty (ID) using Fitts' law
ID = np.log2((distance / width) + 1)

# Calculate Movement Time MT
MT = 167.48 + ID * 185.42

# Print the average Movement Time
average_MT = sum(MT)/8
print(average_MT) 