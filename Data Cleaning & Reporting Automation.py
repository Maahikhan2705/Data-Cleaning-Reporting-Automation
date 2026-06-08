import pandas as pd

# 1. Load the dataset with explicit UTF-8 encoding to prevent Windows reading errors
file_path = "my_file (1).csv"
df = pd.read_csv(file_path, encoding="utf-8")

# Normalize column names by replacing non-breaking spaces (\xa0) with regular spaces
df.columns = df.columns.str.replace(r"\xa0", " ", regex=True)


# 2. Clean and Standardize Special Characters (Fixes the '' display issue)
if "Artist" in df.columns:
    # Convert 'é' to standard 'e'
    df["Artist"] = df["Artist"].str.replace("é", "e", regex=False)

if "Year(s)" in df.columns:
    # Convert the long en-dash '–' to a standard regular hyphen '-'
    df["Year(s)"] = df["Year(s)"].str.replace("–", "-", regex=False)


# 3. Clean the Numeric Columns
def clean_money_column(column_name):
    if column_name in df.columns:
        # Remove '$', commas, spaces, and everything after a bracket '['
        df[column_name] = (
            df[column_name]
            .astype(str)
            .str.replace(r"\s+|\$|,", "", regex=True)
            .str.split("[")
            .str[0]
        )
        # Convert to numeric, turning errors (like empty fields) into NaN
        df[column_name] = pd.to_numeric(df[column_name], errors="coerce")


clean_money_column("Actual gross")
clean_money_column("Adjusted gross (in 2022 dollars)")
clean_money_column("Average gross")


# 4. Clean Text Columns (Removes status symbols like † or ‡ and footnotes)
def clean_text_column(column_name):
    if column_name in df.columns:
        df[column_name] = (
            df[column_name]
            .astype(str)
            .str.replace(r"[†‡]", "", regex=True)
            .str.split("[")
            .str[0]
            .str.strip()
        )


clean_text_column("Artist")
clean_text_column("Tour title")

print("--- Cleaned Data Overview ---")
# Will now print cleanly as 'Beyonce' and standard text
print(df[["Artist", "Tour title", "Year(s)", "Actual gross", "Shows"]].head())


# 5. Quick Analysis Examples
print("\n--- Quick Insights ---")

# Top 3 highest actual grossing tours
top_tours = df.nlargest(3, "Actual gross")[
    ["Artist", "Tour title", "Actual gross"]
]
print("Top 3 Highest Grossing Tours:")
print(top_tours.to_string(index=False))

# Total actual gross by artist
artist_totals = (
    df.groupby("Artist")["Actual gross"].sum().sort_values(ascending=False)
)
print("\nTotal Gross by Artist (Top 3):")
print(artist_totals.head(3))