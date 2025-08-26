import pandas as pd
df = pd.read_csv(r"C:\Users\Mathi\Downloads\archive\movie_metadata.csv")
print(df)
df = df.drop_duplicates()
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

