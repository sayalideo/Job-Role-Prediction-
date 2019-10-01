#Checks if distribution is correct

import pandas as pd

roo        = "../Data/train.csv"

df = pd.read_csv(roo)

mine = {}
num  = {}

for key, value in df.iteritems():
    temp      = list(set(value)) 
    mine[key] = temp
    num[key]  = len(temp)

data = {}

for key, value in df.iteritems():
    data[key] = {}
    col = df[key]
    for x in col:
        if x not in data[key].keys():
            data[key][x]=0
        else:
            data[key][x]=data[key][x]+1


# print('mine',mine)
#print('num',num)
print('data',data)

#Train Data
'''Suggested Job Role_Applications Developer': {0: 14547, 1: 411}, 'Suggested Job Role_Business Intelligence Analyst': {0: 14555, 1: 403}, 
'Suggested Job Role_Business Systems Analyst': {0: 14524, 1: 434}, 'Suggested Job Role_CRM Business Analyst': {0: 14522, 1: 436}, 
'Suggested Job Role_CRM Technical Developer': {0: 14535, 1: 423}, 'Suggested Job Role_Data Architect': {0: 14537, 1: 421}, 
'Suggested Job Role_Database Administrator': {0: 14515, 1: 443}, 'Suggested Job Role_Database Developer': {1: 434, 0: 14524}, 
'Suggested Job Role_Database Manager': {0: 14533, 1: 425}, 'Suggested Job Role_Design & UX': {0: 14519, 1: 439}, 
'Suggested Job Role_E-Commerce Analyst': {0: 14551, 1: 407}, 'Suggested Job Role_Information Security Analyst': {0: 14553, 1: 405}, 
'Suggested Job Role_Information Technology Auditor': {0: 14542, 1: 416}, 'Suggested Job Role_Information Technology Manager': {0: 14517, 1: 441},
'Suggested Job Role_Mobile Applications Developer': {0: 14557, 1: 401}, 'Suggested Job Role_Network Engineer': {0: 14494, 1: 464}, 
'Suggested Job Role_Network Security Administrator': {0: 14126, 1: 832}, 'Suggested Job Role_Network Security Engineer': {0: 14488, 1: 470}, 
'Suggested Job Role_Portal Administrator': {0: 14515, 1: 443}, 'Suggested Job Role_Programmer Analyst': {0: 14563, 1: 395}, 
'Suggested Job Role_Project Manager': {0: 14509, 1: 449}, 'Suggested Job Role_Quality Assurance Associate': {0: 14536, 1: 422}, 
'Suggested Job Role_Software Developer': {0: 14520, 1: 438}, 'Suggested Job Role_Software Engineer': {0: 14518, 1: 440},
'Suggested Job Role_Software Quality Assurance (QA) / Testing': {0: 14532, 1: 426}, 'Suggested Job Role_Software Systems Engineer': {0: 14529, 1: 429},
'Suggested Job Role_Solutions Architect': {0: 14527, 1: 431}, 'Suggested Job Role_Systems Analyst': {0: 14548, 1: 410}, 
'Suggested Job Role_Systems Security Administrator': {0: 14539, 1: 419}, 'Suggested Job Role_Technical Engineer': {0: 14542, 1: 416},
'Suggested Job Role_Technical Services/Help Desk/Tech Support': {0: 14542, 1: 416}, 'Suggested Job Role_Technical Support': {0: 14536, 1: 422}, 
'Suggested Job Role_UX Designer': {0: 14518, 1: 440}, 'Suggested Job Role_Web Developer': {0: 14533, 1: 425}'''

#Test Data
''''Suggested Job Role_Applications Developer': {0: 4900, 1: 138}, 'Suggested Job Role_Business Intelligence Analyst': {0: 4903, 1: 135}, 
'Suggested Job Role_Business Systems Analyst': {0: 4892, 1: 146}, 'Suggested Job Role_CRM Business Analyst': {0: 4892, 1: 146}, 
'Suggested Job Role_CRM Technical Developer': {0: 4896, 1: 142}, 'Suggested Job Role_Data Architect': {0: 4897, 1: 141}, 
'Suggested Job Role_Database Administrator': {0: 4890, 1: 148}, 'Suggested Job Role_Database Developer': {0: 4893, 1: 145}, 
'Suggested Job Role_Database Manager': {0: 4895, 1: 143}, 'Suggested Job Role_Design & UX': {0: 4891, 1: 147}, 
'Suggested Job Role_E-Commerce Analyst': {0: 4901, 1: 137}, 'Suggested Job Role_Information Security Analyst': {0: 4902, 1: 136}, 
'Suggested Job Role_Information Technology Auditor': {0: 4898, 1: 140}, 'Suggested Job Role_Information Technology Manager': {0: 4890, 1: 148}, 
'Suggested Job Role_Mobile Applications Developer': {0: 4903, 1: 135}, 'Suggested Job Role_Network Engineer': {0: 4883, 1: 155}, 
'Suggested Job Role_Network Security Administrator': {0: 4760, 1: 278}, 'Suggested Job Role_Network Security Engineer': {0: 4880, 1: 158}, 
'Suggested Job Role_Portal Administrator': {0: 4890, 1: 148}, 'Suggested Job Role_Programmer Analyst': {0: 4906, 1: 132}, 
'Suggested Job Role_Project Manager': {0: 4887, 1: 151}, 'Suggested Job Role_Quality Assurance Associate': {0: 4897, 1: 141}, 
'Suggested Job Role_Software Developer': {0: 4891, 1: 147}, 'Suggested Job Role_Software Engineer': {0: 4890, 1: 148}, 
'Suggested Job Role_Software Quality Assurance (QA) / Testing': {0: 4895, 1: 143}, 'Suggested Job Role_Software Systems Engineer': {0: 4894, 1: 144}, 
'Suggested Job Role_Solutions Architect': {0: 4893, 1: 145}, 'Suggested Job Role_Systems Analyst': {1: 138, 0: 4900}, 
'Suggested Job Role_Systems Security Administrator': {0: 4897, 1: 141}, 'Suggested Job Role_Technical Engineer': {0: 4899, 1: 139}, 
'Suggested Job Role_Technical Services/Help Desk/Tech Support': {0: 4898, 1: 140}, 'Suggested Job Role_Technical Support': {0: 4897, 1: 141}, 
'Suggested Job Role_UX Designer': {0: 4891, 1: 147}, 'Suggested Job Role_Web Developer': {0: 4895, 1: 143}'''