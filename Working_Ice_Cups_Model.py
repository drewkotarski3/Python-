import pandas as pd
import os

data_file = "Ice_cups.csv"

# Check if the data file exists
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    # If the file doesn't exist, create a new DataFrame with the desired columns
    df = pd.DataFrame(columns=["Date", "Day of Week", "Total Venti Ice Cups",
                               "Total Grande Ice Cups", "Total Tall Ice Cups", "Total Trenta Ice Cups"])

    def get_user_input(prompt, datatype):
        while True:
            try:
                value = datatype(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Collect user input for a new row
date = input("Enter a date (YYYY-MM-DD): ")
dow = input("What day of the week is it? ")
VIS = int(input("How many Venti Ice Sleeves: "))
GIS = int(input("How many Grande Ice Sleeves: "))
TIS = int(input("How many Tall Ice Sleeves: "))
TrS = int(input("How many Trenta Ice Sleeves: "))
VIB = int(input("How many Venti Ice Boxes: "))
GIB = int(input("How many Grande Ice Boxes: "))
TIB = int(input("How many Tall Ice Boxes: "))
TrB = int(input("How many Trenta Ice Boxes: "))

# Calculate the amounts
VIS_amount = VIS * 40
GIS_amount = GIS * 50
TIS_amount = TIS * 40
TrS_amount = TrS * 27
VIB_amount = VIB * 600
GIB_amount = GIB * 1000
TIB_amount = TIB * 1000
TrB_amount = TrB * 270

# Calculate the total counts
VI_total = VIS + VIB
GI_total = GIS + GIB
TI_total = TIS + TIB
Tr_total = TrS + TrB

# Create a new DataFrame for the user input
new_row = pd.DataFrame({"Date": [date], "Day of Week": [dow],
                        "Total Venti Ice Cups": [VI_total],
                        "Total Grande Ice Cups": [GI_total],
                        "Total Tall Ice Cups": [TI_total],
                        "Total Trenta Ice Cups": [Tr_total]})

# Concatenate the new row to the existing DataFrame
df = pd.concat([df, new_row], ignore_index=True)

# Save the updated DataFrame back to the data file
df.to_csv(data_file, index=False)
print(df)
