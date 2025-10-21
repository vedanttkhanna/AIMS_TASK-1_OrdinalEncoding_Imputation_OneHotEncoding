import pandas as pd
import numpy as np
data={"Name":["Vedant","Rudransh","Ishaan","Sahil","Aarav","Darshan","Daksh"],
      "Age":[18,18,21,17,25,24,23],
      "food":["popcorn","pizza","burger","pasta","pasta","pizza","burger"]}
df=pd.DataFrame(data)
unique_food=df["food"].unique()
for food in unique_food:
    df[food]=(df["food"]==food).astype(int)
df.drop(columns="food",inplace=True)
print(df)
