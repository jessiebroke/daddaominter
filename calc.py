u1 = 61754 
u2 = 1038
u3 = 1542 
u4 = 580
u5 = 195
u6 = 5

t1 = 5000
t2 = 50000
t3 = 500000
t4 = 5000000
t5 = 50000000
t6 = 143000000

amounttotal = u1*t1 + u2*t2 + u3*t3 + u4*t4 + u5*t5 + u6*t6
usertotal = u1 + u2 + u3 + u4 + u5 + u6
print("Total amount: " + str(amounttotal))
print("Total users: " + str(usertotal))

customtotal = u6*t6
customuser = u6

print("Total amount: " + str(customtotal))
print("Total users: " + str(customuser))

print("% Owned by Custom Users: " + str((customtotal/amounttotal)*100))