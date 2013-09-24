from random import randrange


def celeb(G):
	n=len(G)
	u,v=0,1
	for c in range(2,n):
		#u knows v so u cant be celeb
		if G[u][v]: u=c
		else: v=c
	print(u,v)
	if G[u][v]: c=v
	else: c=u
	print(c)
	for v in range(n):
		if c==v: continue
		if G[c][v]: break
		if not G[v][c]:break
	else:
		return c
	return None







n=100
G=[[randrange(2) for i in range(n)] for i in range(n)]
#print(G) G[0][0] to G[99][99]
#G is a list of lists. Each inner list is a binary array 0 or 1

#now make sure there is one celeb
c = randrange(n)
print("Input Celeb",c)
for i in range(n):
	G[i][c]=True
	G[c][i]=False
G[c][c]=True


C=celeb(G)
print(C)
