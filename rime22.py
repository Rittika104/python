a=0
b=1
n=int(input("enter the number of terms needed"))
print(a,b,end=" ")
while(n-1):
	x=a+b
	a=b
	b=x
	print(x,ends=" ")
	n=n-1