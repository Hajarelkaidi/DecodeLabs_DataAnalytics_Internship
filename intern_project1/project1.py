import pandas as pd 
import numpy as np

# ******** Data Understanding ********
# ====== step 1: Load dataset ======
data = pd.read_excel("Dataset for Data Analytics.xlsx")

# ====== step 2: Data display ======
print(data.head())
print(data.describe())
data.info()

# ====== step 3: Missing Values ======
        # Number of missing values: 
missing_values = data.isnull().sum()
print("The numbers of missing values are:\n",missing_values)
        # Percentage of missing values:
per_missing_values = data.isnull().mean() * 100
print("\nThe percentages of the missing values are:\n",per_missing_values)

# ******** Data Cleaning ********
# ====== step 4: Handling Missing Values ======
