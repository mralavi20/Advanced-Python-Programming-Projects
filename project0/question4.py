n = int (input ())
a = []
b = []
c = []
for i in range (n):
    d,e,f = str (input ()).split (".")
    e = e.capitalize ()
    a.append (d)
    b.append (e)
    c.append (f)
for i in range (n):
    for j in range (i, n):
        if (a[i] == "m" and a[j] == "f"):
            a[i],a[j] = a[j],a[i]
            b[i],b[j] = b[j],b[i]
            c[i],c[j] = c[j],c[i]
for i in range (n):
    for j in range (i, n):
        if (b[i] > b[j] and a[i] == a[j]):
            a[i],a[j] = a[j],a[i]
            b[i],b[j] = b[j],b[i]
            c[i],c[j] = c[j],c[i]
for i in range (n):
    print (a[i], b[i], c[i])
