p,f,o=[[int(m) for m in n.replace("\n","").replace("-",",").split(",")] for n in open("../data/day04.txt")],0,0
for e in p:
 a,b,c,d=e;x,y=a-c,b-d
 if x*y<=0:f+=1 
 elif x*(b-c)<=0 or (a-d)*y<=0:o+=1
print(f,f+o)