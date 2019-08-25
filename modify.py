import pandas as pd

#roo        = "./roo_data.csv"
roo1       = "./roo1.csv"
df = pd.read_csv(roo1)

#df.drop(['Salary Range Expected','Interested Type of Books'], axis=1, inplace=True)

print(df.shape)

data_dum = pd.get_dummies(df, drop_first=False)
print(data_dum.shape)   #(20000, 127)

with open(roo1, 'w', encoding='utf-8') as f:
    data_dum.to_csv(f, index=False)

