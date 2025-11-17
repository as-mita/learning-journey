import pandas as pd

# Load the Excel file
df = pd.read_excel("learn_vocab.xlsx")

# Delete the 6th row (Excel-style)
df = df.drop(index=5)

# Display to verify
print(df.head(10))
