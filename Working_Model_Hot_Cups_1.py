import pandas as pd
import os

data_file = "hot_cups.csv"

# Check if the data file exists
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    # If the file doesn't exist, create a new DataFrame with the desired columns
    df = pd.DataFrame(columns=["Date", "Day of Week", "Total Venti Hot Cups",
                               "Total Grande Hot Cups", "Total Tall Hot Cups", "Total Short Hot Cups"])

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
VHS = int(input("How many Venti Hot Sleeves: "))      
GHS = int(input("How many Grande Hot Sleeves: "))
THS = int(input("How many Tall Hot Sleeves: "))
SHS = int(input("How many Short Hot Sleeves: "))
VHB = int(input("How many Venti Hot Boxes: "))
GHB = int(input("How many Grande Hot Boxes: "))
THB = int(input("How many Tall Hot Boxes: "))
SHB = int(input("How many Short Hot Boxes: "))

# Calculate the amounts
VHS_amount = VHS * 43
GHS_amount = GHS * 46
THS_amount = THS * 44
SHS_amount = SHS * 55
VHB_amount = VHB * 645
GHB_amount = GHB * 920
THB_amount = THB * 1100
SHB_amount = SHB * 660

# Calculate the total counts
VH_total = VHS + VHB
GH_total = GHS + GHB
TH_total = THS + THB
SH_total = SHS + SHB

# Create a new DataFrame for the user input
new_row = pd.DataFrame({"Date": [date], "Day of Week": [dow],
                        "Total Venti Hot Cups": [VH_total],
                        "Total Grande Hot Cups": [GH_total],
                        "Total Tall Hot Cups": [TH_total],
                        "Total Short Hot Cups": [SH_total]})

# Concatenate the new row to the existing DataFrame
df = pd.concat([df, new_row], ignore_index=True)

# Save the updated DataFrame back to the data file
df.to_csv(data_file, index=False)
print(df)
