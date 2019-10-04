import pandas as pd

roo        = "../Data/roo_data.csv"
roo1       = "../Data/roo1.csv"
df = pd.read_csv(roo)
#talenttests taken? olympiads Type of company want to settle in? Percentage in Electronics Subjects Interested subjects 
df.drop(['Salary Range Expected','Interested Type of Books','talenttests taken?','olympiads','Type of company want to settle in?','Percentage in Electronics Subjects','Interested subjects'], axis=1, inplace=True)

print(df.shape)

data_dum = pd.get_dummies(df, drop_first=False)
print(data_dum.shape)   #(20000, 127)

with open(roo1, 'w', encoding='utf-8') as f:
    data_dum.to_csv(f, index=False)

