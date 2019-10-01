import pandas as pd
roo = "../Data/roo1.csv"
df = pd.read_csv(roo)

percent = {'Database Developer': 580, 'Portal Administrator': 592, 'Systems Security Administrator': 561, 'Business Systems Analyst': 581, 'Software Systems Engineer': 574, 'Business Intelligence Analyst': 539, 'CRM Technical Developer': 566, 'Mobile Applications Developer': 537, 'UX Designer': 588, 
                        'Quality Assurance Associate': 564, 'Web Developer': 569, 'Information Security Analyst': 542, 'CRM Business Analyst': 583, 'Technical Support': 564, 'Project Manager': 601, 'Information Technology Manager': 590, 'Programmer Analyst': 528, 'Design & UX': 587, 'Solutions Architect': 577,
                        'Systems Analyst': 549, 'Network Security Administrator': 1111, 'Data Architect': 563, 'Software Developer': 586, 'E-Commerce Analyst': 545, 'Technical Services/Help Desk/Tech Support': 557, 'Information Technology Auditor': 557, 'Database Manager': 569, 'Applications Developer': 550, 
                        'Database Administrator': 592, 'Network Engineer': 620, 'Software Engineer': 589, 'Technical Engineer': 556, 'Network Security Engineer': 629, 'Software Quality Assurance (QA) / Testing': 570}


title = list(df.columns)
mapp  = {}
for i in range(93,127):
    mapp[title[i]] = 0
title = title[93:]

count = {}

for job,p in percent.items():
    percent[job]=p*3//4
    count[job]=0

tr = []
ts = []

n = df.shape[0]
for x in range(n):
    row = df.iloc[x,93:]
    r = row['Suggested Job Role_Applications Developer':]
    #print(r)
    
    for items in r.iteritems(): 
        if(items[1] == 1):
            role = items[0]

    i = role.find('_')
    role = role[i+1:]
    #print(role)
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
