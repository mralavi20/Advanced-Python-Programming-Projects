a = int (input ())
horror = [0, 5]
romance = [0, 6]
comedy = [0, 3]
history = [0, 4]
adventure = [0, 2]
action = [0, 1]
for i in range (a):
    b = str (input ()).split ()
    for j in range (1, len (b)):
        if (b[j] == "Horror"):
            horror[0] = horror[0] + 1
        elif (b[j] == "Romance"):
            romance[0] = romance[0] + 1
        elif (b[j] == "Comedy"):
            comedy[0] = comedy[0] + 1
        elif (b[j] == "History"):
            history[0] = history[0] + 1
        elif (b[j] == "Adventure"):
            adventure[0] = adventure[0] + 1
        elif (b[j] == "Action"):
            action[0] = action[0] + 1
r = [horror, romance, comedy, history, adventure, action]
for i in range (6):
    for j in range (i, 6):
        if (r[i][0] < r[j][0]):
            r[i],r[j] = r[j],r[i]
        elif (r[i][0] == r[j][0] and r[i][1] > r[j][1]):
            r[i],r[j] = r[j],r[i]
for i in range (6):
    if (r[i][1] == 1):
        print ("Action :", end = " ")
    elif (r[i][1] == 2):
        print ("Adventure :", end = " ")
    elif (r[i][1] == 3):
        print ("Comedy :", end = " ")
    elif (r[i][1] == 4):
        print ("History :", end = " ")
    elif (r[i][1] == 5):
        print ("Horror :", end = " ")
    elif (r[i][1] == 6):
        print ("Romance :", end = " ")
    print (r[i][0])
