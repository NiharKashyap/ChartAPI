from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv('spotify.csv')
df.fillna(0, inplace=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}


class Line_Chart(BaseModel):
    column_name : list

@app.post("/charts/line")
def get_data_chart(chart_data : Line_Chart):
    dates = list(df[chart_data.column_name[0]])
    values  = list(df[chart_data.column_name[1]])
    return {'date':dates, 'values': values}


@app.post("/charts/bar")
def get_data_bar(chart_data : Line_Chart):
    dates = list(df[chart_data.column_name[0]])
    values  = list(df[chart_data.column_name[1]])
    return {'date':dates, 'values': sum(values)}