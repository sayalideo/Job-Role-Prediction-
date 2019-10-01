import pandas as pd

roo        = "./roo_data.csv"

df = pd.read_csv(roo)

# data_dum = pd.get_dummies(d, drop_first=False)
# print(data_dum)
# #yay = pd.concat(data_dum, ignore_index=True)


# with open('./temp.csv', 'w', encoding='utf-8') as f:
#     data_dum.to_csv(f, index=False)

# mine = {}
# num  = {}

# for key, value in df.iteritems():
#     temp      = list(set(value)) 
#     mine[key] = temp
#     num[key]  = len(temp)

# data = {}

# for key, value in df.iteritems():
#     data[key] = {}
#     col = df[key]
#     for x in col:
#         if x not in data[key].keys():
#             data[key][x]=0
#         else:
#             data[key][x]=data[key][x]+1


