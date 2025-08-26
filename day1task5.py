import pandas as pd
df = pd.read_csv(r"C:\Users\Mathi\Downloads\archive\movie_metadata.csv")
print(df)
df.to_csv("imdb_cleaned.csv", index=False)
