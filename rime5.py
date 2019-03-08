import random
l=["r","p","s"]
while True:
	#take input from user
	u=input("enter your choice,press n to dicontiue")
	#to exit
	if u=='n':
		print("Game over")
		exit()
		#input from computer
		c=ramdom.choice(l)
		print("computer chooses",c)

		#compare the user and computer choice
		if u==c:
			print("tie")
		elif u="r"and c=="p":
			print("computer wins")
			elif u=='r' and c=='s':
			print("userwins")
		elif u=='s'and c=='r':
		    print("compwins")
		elif u=='s' and c=='p':
		elif=='p' and c=='s':
		    print("userwins")
		    elif u=='p'and c=='s':
		    print("compwins")        