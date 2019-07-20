x = int(input("Type second:"))
if 0 <= x < 60: #calculate seconds
    print(0,"days", 0,"hours",0,"minutes", x, "seconds")
y = x//60  #calculate minutes
z = x%60  #calculate seconds
if 60 <= x < 3600:
    print(0, "days", 0, "hours", y , "minutes", z, "seconds")
m = x//3600  #calculate hours
n = (x-(3600*m))//60  # calculate minutes
b = x % 60  #calculate seconds
if 3600 <= x <86400:
    print(0, "days", m, "hours", n, "minutes", b, "seconds")
d = x//86400  #calculate days
j = (x-(86400*d))//3600  #calculate hours
k = (x-(3600*j))//60  #calculate minutes
u = x%60  #calculate seconds
if x >= 86400:
    print(d, "days", j, "hours", n, "minutes", u, "seconds")



