import pandas as pd

tr = "../Data/train.csv"
ts = "../Data/test.csv"
train = pd.read_csv(tr)
test = pd.read_csv(ts)

train.drop(['interested in games_no','interested in games_yes'], axis=1, inplace=True)
test.drop(['interested in games_no','interested in games_yes'], axis=1, inplace=True)

with open(tr, 'w', encoding='utf-8') as f:
    train.to_csv(f, index=False)

with open(ts, 'w', encoding='utf-8') as f:
    test.to_csv(f, index=False)
