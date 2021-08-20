import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)

#Excersice 1

df.head()

#solution: "Avatar"

#Excersice 2

df['profitable'] = df.revenue > df.budget
df['profitable'] = df['profitable'].astype(int)

regression_target = 'revenue'
classification_target = 'profitable'
df['profitable'].value_counts()

#answer is 2585

#Excersice 3

df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(how="any")
df.shape

# answer is 1406

#Excersice 4


list_genres = df.genres.apply(lambda x: x.split(","))
genres = []
for row in list_genres:
    row = [genre.strip() for genre in row]
    for genre in row:
        if genre not in genres:
            genres.append(genre)

for genre in genres:
    df[genre] = df['genres'].str.contains(genre).astype(int)

df[genres].head()

# answer is 20

#Excersice 5

continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
plotting_variables = ['budget', 'popularity', regression_target]

axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
                                  color=(0, 0, 0), hist_kwds={"color": (0, 0, 0)}, facecolor=(1, 0, 0))

#Excersice 6
plt.show()

print(df[outcomes_and_continuous_covariates].skew())

# answer is "popularity"

#Excersice 6

for covariate in ['budget', 'popularity', 'runtime', 'vote_count', 'revenue']:
    df[covariate] = df[covariate].apply(lambda x: np.log10(1 + x))

print(df[outcomes_and_continuous_covariates].skew())

# answer is 0.530

#Excersice 7

df.to_csv("movies_clean.csv")


