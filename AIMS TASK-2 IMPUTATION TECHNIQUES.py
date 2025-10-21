import pandas as pd
import numpy as np
data={"name":["Vedant","Rudransh","Ishaan","Sahil","Aarav","Darshan","Daksh"],
      "age":[18,18,None,17,None,24,23],
      "food":["popcorn","pizza","burger","pasta","pasta","pizza","burger"]}
df=pd.DataFrame(data)
df["age"]=df["age"].fillna(df["age"].mean())
print(df.to_string(index=False))
