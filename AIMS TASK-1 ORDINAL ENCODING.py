import pandas as pd
import numpy as np
data={"Name":["Vedant","Rudransh","Ishaan","Sahil","Aarav","Darshan","Daksh"],
      "Age":[18,18,21,17,25,24,23],
      "food":["popcorn","pizza","burger","pasta","pasta","pizza","burger"]}
df=pd.DataFrame(data)
object_columns=df.select_dtypes(include="object")
for col in object_columns:
    df[col+" encoded"]=df[col].astype('category').cat.codes
print(df)