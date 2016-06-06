# -*- coding: utf-8 -*-

def triangles():
	t=[]
	while 1:
		t1=[1]
		if len(t)<1:
			yield t1
		if len(t)>1:
			for i in range(len(t)-1):
				t1.append(t[i]+t[i+1])
		t1.append(1)
		yield t1
		t=t1

n=0
for t in triangles():
	print(t)
	n+=1
	if n==10:
		break


