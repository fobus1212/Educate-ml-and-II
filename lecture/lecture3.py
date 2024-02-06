n = int(input())

def guess(n):
    if n/2<1:
        p = (n)
    elif n>0:
        for i in range(n+1):
            if i*i == n:
                p = i
                i= i+1
                if p is not None:
          