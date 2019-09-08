import pandas as pd
import numpy as np
roo        = "./roo1.csv"

#wines = np.genfromtxt("./roo1.csv", delimiter=";", skip_header=1)
data1 = np.loadtxt("./roo1.csv", delimiter=',', skiprows=1)
data  = data1[0:16129,:]
print(data.shape)
myu,sig = [],[]
for i in range(9):
    mean = np.mean(data[:,i])
    myu.append(mean)
    sigm = np.sum(np.square(data[:,i]))/data.shape[0]
    sigm = sigm**0.5
    sig.append(sigm)
    data[:,i] = (data[:,i]-mean)/sigm
    #print(data[:,i])
                                            
#print(myu,sig) 

print(data[:,0])