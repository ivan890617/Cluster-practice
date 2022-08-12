# -*- coding: UTF-8 -*-

from enum import Enum
from fastapi import FastAPI, File, UploadFile
from pandas import DataFrame
from fastapi.responses import FileResponse
import joblib
import json
import pandas as pd
import time
import numpy as np

app = FastAPI()


def data_fetch_by_num(datajson,senior_num):
    # JSON file
    # Reading from file
    data = json.loads(datajson)
    # print(data['find']['air_sensor001']['1651379360'])
    # df = pd.read_json(data['find']['air_sensor001'], orient ='index')
    df = pd.DataFrame.from_dict(data['find']['air_sensor0' + senior_num], orient='index')
    time_list = []
    for i in range((len(df.index.values))):
        YmdHMS = time.strftime('%Y-%m-%d  %H:%M:00', time.gmtime(int(df.index.values[i])))
        time_list.append(YmdHMS)
    df['Datetime'] = time_list
    return df

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/2Dkmeans/")
def add(eco2: int, pm25: int):
    scalereco2 = joblib.load('scalereco2')
    eco2num = scalereco2.transform([[eco2]])

    scalerpm25 = joblib.load('scalerpm25')
    pm25num = scalerpm25.transform([[pm25]])


    datascale = {'eco2': [eco2num],
            'pm25': [pm25num]}
    dfscale = DataFrame(datascale)
    km = joblib.load('2Dcluster.pkl')
    label = km.predict(dfscale)

    return {"label": label[0].tolist()}


@app.post("/predict/")
async def predict_api(file: UploadFile = File(...)):
    datajson = await file.read()
    df = data_fetch_by_num(datajson,str(1).zfill(2))
    for i in range(2, 41, 1):
        df2 = data_fetch_by_num(datajson,str(i).zfill(2))
        df = df.append(df2, ignore_index=True)
    df.to_csv("datacsv.csv")

    data = pd.read_csv("datacsv.csv")
    data_sort = data.drop(columns='Unnamed: 0')
    data_sort = data_sort.drop(columns='csq')

    df = data_sort
    scalereco2 = joblib.load('scalereco2')
    df['eco2_scale'] = scalereco2.transform(data_sort[['eco2']].values)

    scalerpm25 = joblib.load('scalerpm25')
    df['pm25_scale'] = scalerpm25.transform(data_sort[['pm25']].values)

    df_scale = df[['eco2_scale', 'pm25_scale']]
    km = joblib.load('2Dcluster.pkl')
    cluster = km.predict(df_scale)
    df['label'] = cluster
    df['Datetime'] = data_sort['Datetime']
    df.to_csv("label.csv")

    return {"Finish"}


#http://127.0.0.1:8000/2Dkmeans/?eco2=3853&pm25=6

#http://127.0.0.1:8000/docs