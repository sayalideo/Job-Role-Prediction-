import pandas as pd

roo        = "./roo1.csv"

df = pd.read_csv(roo,usecols = ['Logical quotient rating','coding skills rating','public speaking points'])

data = {
    'Logical quotient rating': {4: 2235, 7: 2225, 1: 2193, 5: 2274, 3: 2217, 2: 2254, 9: 2227, 6: 2176, 8: 2190},
    'coding skills rating': {4: 2223, 2: 2297, 1: 2139, 6: 2230, 8: 2241, 3: 2233, 5: 2205, 9: 2216, 7: 2207}, 
    'public speaking points': {8: 2203, 3: 2162, 5: 2157, 1: 2234, 6: 2227, 4: 2257, 9: 2265, 7: 2267, 2: 2219}, 
}

#(sum(click)+alpha)/(N+2*alpha)

