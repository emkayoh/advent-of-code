import math
f = open("input.txt").read()

outp = 0
end = len(f)-1 if len(f)%2==1 else len(f)-2
idx = 0
left = int(f[end])
E=False

for i in range(len(f)):
    if i%2 == 0:
        outp+= int(i/2)*sum(range(idx, int(f[i])+idx))
        idx+=int(f[i])
    else:
        for j in range(int(f[i])):
            outp+=idx*int(end/2)
            idx+=1
            left-=1
            if left == 0:
                end-=2
                left=int(f[end])
                if end <= i:
                    E=True
                    break
        if E:
            break
        if i+1 == end:
            outp+= int(end/2)*math.prod(range(idx, left+idx))
            break

print(outp)