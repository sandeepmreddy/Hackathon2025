import pandas as pd

# Load the CSV file
file_path = "AnamolyCase1.csv"
df = pd.read_csv(file_path)

# Print all column names to identify the exact headers
print("Available columns:", df.columns.tolist())

# Try to match columns using partial names
ihub_col = [col for col in df.columns if "Ihub" in col]
gl_col = [col for col in df.columns if "GL" in col]
acct_col = [col for col in df.columns if "Account" in col]

# Read and display the selected columns and their difference
if ihub_col and gl_col and acct_col:
    ihub_col_name = ihub_col[0]
    gl_col_name = gl_col[0]
    acct_col_name = acct_col[0]

    # Convert to numeric in case of string values with commas or spaces
    df[ihub_col_name] = pd.to_numeric(df[ihub_col_name], errors='coerce')
    df[gl_col_name] = pd.to_numeric(df[gl_col_name], errors='coerce')

    # Calculate the difference
    df['Difference'] = df[ihub_col_name] - df[gl_col_name]

    # Display the result with account number
    selected_columns = df[[acct_col_name, ihub_col_name, gl_col_name, 'Difference']]
    print("Selected Columns with Account Number and Difference:")
    print(selected_columns.head())
else:
    print("Could not find expected columns.")
