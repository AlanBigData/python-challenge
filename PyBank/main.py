# Pybank mainfile

# Modules
import pandas as pd

# Define all of the variables for calculated values
df = pd.read_csv(r'Resources\budget_data.csv')

# Calculate the total number of months using pandas df
total_months = len(df)

# Sum the total in the P/L column
total_profit_loss = "{:,}".format(df["Profit/Losses"].sum())

# Differnce of P/L
df["Monthly Change"] = df["Profit/Losses"].diff()

# Greatest increase with dat and formatted
greatest_increase_date = df.loc[df["Monthly Change"].idxmax(), "Date"]
greatest_increase = "{:,}".format(int(df["Profit/Losses"].max()))

# Greates decrease with date and formatted
greatest_decrease_date = df.loc[df["Monthly Change"].idxmin(), "Date"]
greatest_decrease = "{:,}".format(int(df["Profit/Losses"].min()))

# Average Changes with the mean function
average_change = "{:,}".format(int(df["Monthly Change"].mean()))
# print(df.head())

print(f'''Financial Analysis 
---------------------------------------------
Total Months: {total_months}
Total Profit/Losses: ${total_profit_loss}
Average Change: {average_change}
Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}
Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}       
''')

# Create path to write file to analyis folder
path = (r'Analysis\financial_analysis.txt')
with open(path, "w") as file:

    # Write file to analysis folder
    file.write(f''' Financial Analysis 
---------------------------------------------
Total Months: {total_months}
Total Profit/Losses: ${total_profit_loss}
Average Change: {average_change}
Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}
Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}       
''')
