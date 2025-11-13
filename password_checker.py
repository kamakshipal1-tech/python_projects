
password =input()
length_password= len(password)


if  length_password <4 :
     print("Weak password")
elif length_password<8 :
     print("Medium password")
else:
     print("Strong password")