user=input("enter the username")
password=input("enter the password")
a=5
if user=="india" and password=="ind":
	print("login successfull")
else:
	print("invalid username or password")
	while a>1:
		a-=1
		if user=="india" and password=="ind":
			print("login successfull")
		else:
			print("wrong password",a,"chances left")
			user=input("enter the username")
			password=input("enter the password")	
			while a==1:
				print("your account is blocked for 24 hours")
				break 

		