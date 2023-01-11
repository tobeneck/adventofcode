def f(c):return sum([c.count(i) for i in c])>len(c)
d,i,p,m=open("../data/day06.txt").readline(),0,4,14
while f(d[i:i+p]):i+=1
j=i
while f(d[j:j+m]):j+=1
print(i+p,j+m)