import pandas as pd 

def get_hotel(hotel_name = "Days Inn Barstow"):
    df = pd.read_csv("src/Data/7282_1.csv") 
    df = df.loc[(df.categories == "Hotels")  & (df.name == hotel_name) ]
    return df

def get_all_hotel_names():
    df = pd.read_csv("src/Data/7282_1.csv") 
    df = df.loc[(df.categories == "Hotels")]
    names = df.name.unique()
    return list(names)
