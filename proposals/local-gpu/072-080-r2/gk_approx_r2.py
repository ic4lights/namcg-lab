from math import log
def Delta(M1,M2,l1,l2):
    M=M1+M2
    s=sum(log((M-1+c)/(M1-1+c)) for c in range(1,l1+1))+sum(log((M-2+c)/(M2-1+c)) for c in range(1,l2+1))
    return s-log((l1+1)/(l1-l2+1))
for M1 in (1000,10000,100000):
    for l in (10, int(M1**0.5), M1//10):
        l1=l; l2=l//2
        d=Delta(M1,M1,l1,l2); a=l1*log(2)+l2*log(2)
        print(M1,l1,l2,'Delta=%.2f approx=%.2f diff=%.2f log l1=%.2f'%(d,a,d-a,log(l1)))
