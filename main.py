import pandas as pd
from fastapi import FastAPI
app = FastAPI()
df=pd.read_csv("db.csv")
@app.get("/{locality}")
def get_representative(locality: str):
    v=df["constituency"]
    for i in range(len(v)):
        if v[i]==locality:
             return {"Name":df["Name"][i],"Phone No":df["Contact No"][i],"E-mail":df["E-mail ID"][i]}
            break