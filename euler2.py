a=1
b=2
sum=2
while(1):
	c=b
	b=b+a
	a=c
	if(b>=4000000):
		break;
	#print b,
	if b%2==0:
		sum=sum+b

print sum