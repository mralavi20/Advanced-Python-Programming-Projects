a = str (input ()).split ()
b = []
c = []
for i in range (1, len (a)):
    if ((a[i][0].isupper ()) and ("." not in a[i - 1])):
        d = a[i].replace (".", "")
        d = d.replace (",", "")
        b.append (i + 1)
        c.append (d)
if (len (b) == 0):
    print ("None")
else:
    for i in range (len (b)):
        print (str (b[i]) + ":" + c[i])
