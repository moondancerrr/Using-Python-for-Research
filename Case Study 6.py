data_filepath ='https://s3.amazonaws.com/assets.datacamp.com/production/course_974/datasets/'
# Exercise 1
from collections import Counter
import numpy as np
def marginal_prob(chars):
    return Counter(favorite_colors.values())


def chance_homophily(chars):
    mp = marginal_prob(chars)
    total = 0
    for i in mp.values():
        total += (i / sum(mp.values())) ** 2
    return total


favorite_colors = {
    "ankit": "red",
    "xiaoyu": "blue",
    "mary": "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)
#answer is 0.5555555555555556

#Exercise 2

import pandas as pd

df = pd.read_stata(data_filepath + "individual_characteristics.dta")
df1 = df[df.village == 1]
df2 = df[df.village == 2]
print(df1)

#answer is 3

# Exercise 3
sex1 = dict(zip(df1.pid.values, df1.resp_gend))
caste1 = dict(zip(df1.pid.values, df1.caste))
religion1 = dict(zip(df1.pid.values, df1.religion))

# same thing for df2
sex2 = dict(zip(df2.pid.values, df2.resp_gend))
caste2 = dict(zip(df2.pid.values, df2.caste))
religion2 = dict(zip(df2.pid.values, df2.religion))
#answer is OBC

# Exercise 4
sex1 = df1.set_index("pid")["resp_gend"].to_dict()
caste1 = df1.set_index("pid")["caste"].to_dict()
religion1 = df1.set_index("pid")["religion"].to_dict()

sex2 = df2.set_index("pid")["resp_gend"].to_dict()
caste2 = df2.set_index("pid")["caste"].to_dict()
religion2 = df2.set_index("pid")["religion"].to_dict()

print("Village 1 observed proportion of same sex:", homophily(G1, sex1, pid1))
print("Village 1 observed proportion of same caste:", homophily(G1, caste1, pid1))
print("Village 1 observed proportion of same religion:", homophily(G1, religion1, pid1))

print("Village 2 observed proportion of same sex:", homophily(G2, sex2, pid2))
print("Village 2 observed proportion of same caste:", homophily(G2, caste2, pid2))
print("Village 2 observed proportion of same religion:", homophily(G2, religion2, pid2))

print("Village 1 chance of same sex:", chance_homophily(sex1))
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))

print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))
print("Village 1 chance of same sex:", chance_homophily(sex1))
print("Village 1 chance of same caste:", chance_homophily(caste1))
print("Village 1 chance of same religion:", chance_homophily(religion1))
print("Village 2 chance of same sex:", chance_homophily(sex2))
print("Village 2 chance of same caste:", chance_homophily(caste2))
print("Village 2 chance of same religion:", chance_homophily(religion2))

#answer is Village 2, religion


