# MODULES
import random
import datetime

q1 = input("For what you want to generate password? : ")

add = q1.replace("For what you want to generate password? :", "")

f = open("Password Records.txt", "a")
f.write('\n\nThe Password is generated for: ' + add)
f.close()


# CODE FOR GENERATING PASSWORD

lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sy = ";{}[]():><?*-+/"
print("How much letters do you want in your password? :")
le = int(input())
plist = lc+uc+num+sy
password = ''.join(random.sample(plist,le))
print("The password is : "+password)

# TAKING CURRENT TIME

time = datetime.datetime.now()
typecast_time = str(time)

t = open("Password Records.txt", "a")
t.write('\nThe Password is generated on : '+typecast_time)
t.close()

p = open("Password Records.txt", "a")
p.write('\nThe Password is : ' + password)
p.close()

x = input("Type q to Quit: ")
y = x.replace("Type q to Quit: ", "")

if 'q' in y:
    quit()
