# here the sequence breaking and window will be formed
from data_structures import *

wind=list(map(int, input().split()))
se=[[],[],[],[],[],[],[]]

scenario=['normal','recon','priv']
mode=['single_combined','multi_raw']

def mismatch(x,y):
    return round(sum(1 for w in x if w not in y)/len(x),3)

arr=[]

for i in scenario:
    arr.append(globals()[f"{f"{i}_{mode[0]}"}"])
    arr.append(globals()[f"{f"{i}_{mode[1]}"}"])

for t in wind:
    for i in range(6):
        al=len(arr[i])
        for k in range(al-t+1):
            se[i].append(tuple(arr[i][k:k+t]))        

    nm_s=set(se[0])       # the base sequences (normal syscall set)
    nm_m=set(se[1])        # the sequences under cpu stress
    re_s=se[2]         # the sequences under Input/Output stress
    re_m=se[3]          # the sequences under memory stress
    pr_s=se[4]
    pr_m=se[5]

    mis_rate_res = mismatch(re_s,nm_s)
    mis_rate_rem = mismatch(re_s,nm_m)
    mis_rate_prs = mismatch(pr_s,nm_s)
    mis_rate_prm = mismatch(pr_m,nm_m)
    
    with open("../results/results.csv","a") as result:
        result.write(f"\n{t},recon,single,{mis_rate_res},{round(1-mis_rate_res,3)}")
        result.write(f"\n{t},priv,single,{mis_rate_rem},{round(1-mis_rate_rem,3)}")
        result.write(f"\n{t},recon,multi,{mis_rate_prs},{round(1-mis_rate_prs,3)}")
        result.write(f"\n{t},priv,multi,{mis_rate_prm},{round(1-mis_rate_prm,3)}")


# k, scenario,mode , mismatch_rate, coverage
