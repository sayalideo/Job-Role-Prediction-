import pandas as pd

tr = "../Data/train.csv"
ts = "../Data/test.csv"
train = pd.read_csv(tr)
test = pd.read_csv(ts)

train.drop(['Logical quotient rating','Hours working per day','workshops_cloud computing','workshops_data science','workshops_database security','workshops_game development','workshops_hacking','workshops_system designing','workshops_testing','workshops_web technologies'], axis=1, inplace=True)
test.drop(['Logical quotient rating','Hours working per day','workshops_cloud computing','workshops_data science','workshops_database security','workshops_game development','workshops_hacking','workshops_system designing','workshops_testing','workshops_web technologies'], axis=1, inplace=True)

with open(tr, 'w', encoding='utf-8') as f:
    train.to_csv(f, index=False)

with open(ts, 'w', encoding='utf-8') as f:
    test.to_csv(f, index=False)
