# Combines classes into one
import pandas as pd
roo        = "../Data/roo_data.csv"
df = pd.read_csv(roo)

a = ['Software Quality Assurance (QA) / Testing','Quality Assurance Associate',]

g = [  'Design & UX', 'UX Designer',]

h = ['Web Developer', 
   'Software Developer', 'Technical Engineer', 
  'Software Systems Engineer', 'Software Engineer',  'Mobile Applications Developer',  
   'Applications Developer']

b = ['Systems Security Administrator', 'Information Security Analyst', 'Network Engineer',  
 'Network Security Engineer',  'Network Security Administrator',]

c = ['Database Developer',  'Database Administrator',  'Database Manager']

d = ['Data Architect', 'Systems Analyst',  'Programmer Analyst',
'Business Systems Analyst', 'Business Intelligence Analyst','Solutions Architect','E-Commerce Analyst']

e = [
'CRM Technical Developer',  
'CRM Business Analyst', 
'Technical Services/Help Desk/Tech Support',
 'Technical Support',]

f = ['Project Manager', 'Portal Administrator',
 'Information Technology Auditor',
 'Information Technology Manager']

role = df['Suggested Job Role']
#print(len(a)+len(b)+len(c)+len(d)+len(e)+len(f)+len(g)+len(h))

for r in range(len(role)):
    x = role[r]
    if x in a:
        job = 'Software Quality Assurance (QA) / Testing'
    elif x in b:
        job = 'Security Administrator'
    elif x in c:
        job = 'Database Administrator'
    elif x in d:
        job = 'Business Intelligence Analyst'
    elif x in e:
        job = 'Technical Support'
    elif x in f:
        job = 'Project Manager'
    elif x in g:
        job = 'UX Designer'
    else:
        job = 'Software Developer'
    role[r] = job

df['Suggested Job Role'] = role

with open(roo, 'w', encoding='utf-8') as f:
    df.to_csv(f, index=False)
