import pandas as pd

def format_date(df_bike):
    df = df_bike.insert(1,"International date", df_bike['date'] + "T" + df_bike['heure'] + ":00+01:00")
    print(df)
    return df
format_date(bike)
