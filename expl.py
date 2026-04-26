import numpy as np
import pandas as pd
import matplotlib.pyplot as pplot
import seaborn as sborn

from sklearn.compose import make_column_selector as selector

data = pd.read_csv('archive/student-mat.csv')
see_cols = data.columns

'''
FEATURE SELECTIONS
NUMERICAL
[ "G1", "G2" ] 
[ "absences", "Walc", "Dalc", "health", "goout", "failures", "studytime", "freetime" ]

CATEGORICAL
[ "activities", "internet", "romantic" ]
'''

missing_values = data.isnull().sum() # no missing values shown
features = data[["G1", "G2", "absences", "Walc", "Dalc", "health", "goout", "failures", "studytime", "freetime", "activities", "internet", "romantic"]]
num_data_set = features.select_dtypes(include='number')
cat_data_set = features.select_dtypes(include='object')

new_cat_data_set = pd.get_dummies(cat_data_set, drop_first=True).astype(int) # just converted the categorical columns into numerical (from [ [yes] or [no] ] to [ [1] or [0] ])
final_data = pd.concat([num_data_set, new_cat_data_set], axis=1)

g1_g2 = data[["G1", "G2"]]


pplot.figure(figsize=(8, 6))
pplot.scatter(g1_g2, data["G3"])
pplot.xlabel("{col.upper()}")
pplot.ylabel("Final Grade")
pplot.title("CHECKING... {col.upper()} VS G3")

Q1 = data["G2"].quantile(0.25)
Q3 = data["G2"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

new_g1_g2 = data[(data["G2"] >= lower) & (data["G2"] <= upper)]

pplot.scatter(new_g1_g2["G2"], data["G3"])
pplot.show()




