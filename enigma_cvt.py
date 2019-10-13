import numpy as np
import random

SETTINGS = None

if SETTINGS is None:
    chars = ['abcdefghijklnmopqrstuvwxyz _!@.,-:;"()']
    assign = []
    rand = np.random.randint(10,99-len(chars[0]))
    for i in range(rand,rand+len(chars[0])):
        assign.append(i)
    settings = []

    for i in range(len(chars[0])):
        randn = np.random.randint(0,len(assign))
        settings.append([chars[0][i],[assign[randn]]])
        del assign[randn]
        
    np.save('settings-v0.npy',settings,allow_pickle=True)

else:
    settings = np.load(SETTINGS,allow_pickle=True)

def cvt(sets, input_str):
    cvt_mes = None
    for i in range(len(input_str)):
        for x in range(len(sets)):
            if sets[x][0] == input_str[i]:
                if cvt_mes is not None:
                    cvt_mes += str(*sets[x][1])
                else:
                    cvt_mes = str(*sets[x][1])
    return cvt_mes

string = str(input())
cvt_m = cvt(settings, string)
print(cvt_m)

    
    
