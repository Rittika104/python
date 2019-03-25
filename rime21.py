x=int(input("enter x: "))
y=int(input("enter y: "))
z=int(input("enter z: "))
def sum(x,y,z):
	if(x==y or y==z)
		return(0)
	elif (x==z):
	    return(0)
	else:
	    return(x+y+z)    	
a=sum(x,y,z)
print(a)