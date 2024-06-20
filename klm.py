
import pandas as pd
import numpy as np

# Use the correct file path for the uploaded CSV file
file_path = "/Users/shoheiyoshida/fitts-klm/buttons.csv"

# Read the CSV file starting from the correct row
buttons_df = pd.read_csv(file_path, skiprows=3, header=None, names=['buttons', 'x', 'y'])

# Print column names for debugging
print("Column names:", buttons_df.columns)

# Function to calculate distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Get the coordinates of the start button
start_button = buttons_df[buttons_df['buttons'] == 'START']
start_x = start_button['x'].values[0]
start_y = start_button['y'].values[0]

# List of number buttons, operation buttons, and the equal button
number_buttons = buttons_df[buttons_df['buttons'].str.isdigit()]
operation_buttons = buttons_df[buttons_df['buttons'].isin(['+', '-', '*', '/'])]
equal_button = buttons_df[buttons_df['buttons'] == '=']

# Calculate the average distance from the start button to number buttons
distances_start_to_numbers = number_buttons.apply(
    lambda row: calculate_distance(start_x, start_y, row['x'], row['y']), axis=1)
average_distance_start_to_numbers = distances_start_to_numbers.mean()

# Calculate the average distance from number button to number button
distances_number_to_number = []
for i, row1 in number_buttons.iterrows():
    for j, row2 in number_buttons.iterrows():
        if i != j:
            distances_number_to_number.append(calculate_distance(row1['x'], row1['y'], row2['x'], row2['y']))
average_distance_number_to_number = np.mean(distances_number_to_number)

# Calculate the average distance from number button to operation buttons
distances_number_to_operation = []
for i, number_row in number_buttons.iterrows():
    for j, operation_row in operation_buttons.iterrows():
        distances_number_to_operation.append(calculate_distance(number_row['x'], number_row['y'], operation_row['x'], operation_row['y']))
average_distance_number_to_operation = np.mean(distances_number_to_operation)

# Calculate the average distance from number buttons to the equal button
distances_number_to_equal = number_buttons.apply(
    lambda row: calculate_distance(row['x'], row['y'], equal_button['x'].values[0], equal_button['y'].values[0]), axis=1)
average_distance_number_to_equal = distances_number_to_equal.mean()

# Display the results
print(f"平均距離 (スタートボタンから数字ボタン): {average_distance_start_to_numbers}")
print(f"平均距離 (数字ボタンから数字ボタン): {average_distance_number_to_number}")
print(f"平均距離 (数字ボタンから演算記号ボタン): {average_distance_number_to_operation}")
print(f"平均距離 (数字ボタンから=ボタン): {average_distance_number_to_equal}")

ID_1 = np.log2((average_distance_start_to_numbers / 50) + 1)
ID_2 = np.log2((average_distance_number_to_number / 50) + 1)
ID_3 = np.log2((average_distance_number_to_operation / 50) + 1)
ID_4 = np.log2((average_distance_number_to_equal / 50) + 1)

print(f"ID_1: {ID_1}")
print(f"ID_2: {ID_2}")
print(f"ID_3: {ID_3}")
print(f"ID_4: {ID_4}")

MT_1 = 167.48 + ID_1 * 185.42
MT_2 = 167.48 + ID_2 * 185.42
MT_3 = 167.48 + ID_3 * 185.42
MT_4 = 167.48 + ID_4 * 185.42
sum_MT = MT_1 + MT_2 + MT_3*2 + MT_4

print(f"MT_1: {MT_1}")
print(f"MT_2: {MT_2}")
print(f"MT_3: {MT_3}")
print(f"MT_4: {MT_4}")
print(f"合計MT: {sum_MT}")