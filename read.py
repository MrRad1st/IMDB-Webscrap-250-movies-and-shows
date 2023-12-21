import pandas as pd

# Replace 'your_movie_dataset.xlsx' with the actual path to your Excel file
excel_path = 'your_movie_dataset.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_path)

# Print the entire DataFrame
print(df)
