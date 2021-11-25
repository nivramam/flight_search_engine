import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, model_selection
import pandas as pd

# print(df.head())

def handle_cat_data(df):
    columns = df.columns.values
    for column in columns:
        if column!="City":
            text_digit_vals = {}
            def convert_to_int(val):
                return text_digit_vals[val]

            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                column_contents = df[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x+=1

                df[column] = list(map(convert_to_int, df[column]))
    return df

# df = pd.read_excel('D:\\Nivedhithaa\\Ninth Semester\\lab\\irrLab\\irPackage\\formsproject\\AQI_Bulletin_20211124_converted_by_abcdpdf.xlsx', engine='openpyxl')
# #print(df.head())
# df.drop(['Prominent Pollutant','Based on Number of Monitoring Stations'], 1, inplace=True)
# for k in list(df):
#     df[k] = pd.to_numeric(df[k], errors='ignore')
# df.fillna(0, inplace=True)

# df = handle_cat_data(df)
# print(df.head(20))
# sorted_df = df.sort_values(by='Air Quality')
# print(sorted_df.head(20))