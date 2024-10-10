n = int (input ())
a = []
for i in range (n):
    b = str (input ()).split ()
    a.append (b)
c = str (input ())
for i in range (n):
    c = c.replace (a[i][1], a[i][0])
    c = c.replace (a[i][2], a[i][0])
    c = c.replace (a[i][3], a[i][0])
print (c)