import pandas as pd
df = pd.read_csv(r"C:\Users\Mathi\Downloads\archive\movie_metadata.csv")
print(df)
print(df.isnull().sum())
df['duration'] = df['duration'].fillna(df['duration'].median())
df['content_rating'] = df['content_rating'].fillna(df['content_rating'].mode()[0])
df = df.dropna(subset=['gross'])   
