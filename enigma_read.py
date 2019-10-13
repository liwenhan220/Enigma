import numpy as np
import random

SETTINGS = 'settings-v0.npy'
settings = np.load(SETTINGS,allow_pickle=True)
SHOW_PROCESS = True
def read(sets, input_str):
    cvt_mes = None
    try:
        while len(input_str) > 0:
            for i in range(len(sets)):
                if input_str[0] + input_str[1] == str(sets[i][1][0]):
                    if cvt_mes is not None:
                        cvt_mes += sets[i][0]
                    else:
                        cvt_mes = sets[i][0]
                    input_str = input_str[2:]
                    if SHOW_PROCESS:
                        print(input_str)
    except:
        pass
    return cvt_mes

message = str(input())
cvt_m = read(settings, message)
print(cvt_m)
        
    
    
    
