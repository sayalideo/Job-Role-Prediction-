import pandas as pd
roo = "../Data/roo1.csv"
df = pd.read_csv(roo)

percent = {'Suggested Job Role_Business Intelligence Analyst': 3888, 'Suggested Job Role_Database Administrator':  1743, 'Suggested Job Role_Project Manager': 4098, 'Suggested Job Role_Security Administrator': 3467, 'Suggested Job Role_Software Developer': 3967, 'Suggested Job Role_Technical Support': 2831}
title = list(df.columns)
mapp  = {}
for i in range(93,99):
    mapp[title[i]] = 0
title = title[68:]

count = {}

for job,p in percent.items():
    percent[job]=p*0.8
    count[job]=0

tr = []
ts = []

n = df.shape[0]
for x in range(n):
    row = df.iloc[x,93:]
    r = row['Suggested Job Role_Business Intelligence Analyst':]
    #print('r',r)
    
    for items in r.iteritems(): 
        if(items[1] == 1):
            role = items[0]

    # i = role.find('_')
    # role = role[i+1:]
    print('role',role)
    if(count[role] < percent[role]):
        count[role] = count[role]+1
        tr.append(df.iloc[x,:])
    else:
        ts.append(df.iloc[x,:])
    print('r',len(tr))
    print('s',len(ts))
    print('**********************************************\n\n')

tr = pd.DataFrame(tr)
ts = pd.DataFrame(ts)
with open('../Data/train.csv', 'w', encoding='utf-8') as f:
    tr.to_csv(f, index=False)

with open('../Data/test.csv', 'w', encoding='utf-8') as f:
    ts.to_csv(f, index=False)
