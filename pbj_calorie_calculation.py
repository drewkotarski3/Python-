import pandas as pd
import os

data_file = "pbj_trial_5.csv"

# Check if the data file exists
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    # If the file doesn't exist, create a new DataFrame with the desired columns
    df = pd.DataFrame(columns=["Bread weight", "PB weight", "Jelly weight",
                               "Bread calorie", "PB calorie", "Jelly calorie", 'Total calorie'])

def calculate_product(bread_weight, pb_weight, jelly_weight):
    # Calculate the differences and calories in one step
    pb_weight_x = pb_weight - bread_weight
    jelly_weight_x = jelly_weight - (pb_weight_x + bread_weight)
    bread_calorie = (bread_weight / 39) * 110
    pb_calorie = (pb_weight_x / 32) * 190
    jelly_calorie = (jelly_weight_x / 20) * 50
    total_calorie = bread_calorie + pb_calorie + jelly_calorie

    return [bread_weight, pb_weight_x, jelly_weight_x, bread_calorie, pb_calorie, jelly_calorie, total_calorie]

# Collect user input
bread_weight = int(input("Bread weight: "))
pb_weight = int(input("PB weight: "))
jelly_weight = int(input("Jelly weight: "))

# Calculate and store the results
result = calculate_product(bread_weight, pb_weight, jelly_weight)

# Create a new row in the DataFrame
new_row = pd.DataFrame({"Bread weight": [result[0]], "PB weight": [result[1]], "Jelly weight": [result[2]],
                        "Bread calorie": [result[3]], "PB calorie": [result[4]], "Jelly calorie": [result[5]],
                        "Total calorie": [result[6]]})

# Concatenate the new row to the existing DataFrame
df = pd.concat([df, new_row], ignore_index=True)

# Save the updated DataFrame to the data file
df.to_csv(data_file, index=False)
print(df)
