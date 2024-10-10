def result (t1, t2):
    a,b = str (input ()).split ("-")
    a = int (a)
    b = int (b)

    if (a > b):
        t1[0] = t1[0] + 1
        t2[1] = t2[1] + 1
    elif (b > a):
        t1[1] = t1[1] + 1
        t2[0] = t2[0] + 1
    else:
        t1[2] = t1[2] + 1
        t2[2] = t2[2] + 1
    t1[3] = t1[3] + (a - b)
    t2[3] = t2[3] + (b - a)
    
    return (t1,t2)

i_team = [0, 0, 0, 0, 0, 1]
s_team = [0, 0, 0, 0, 0, 4]
p_team = [0, 0, 0, 0, 0, 3]
m_team = [0, 0, 0, 0, 0, 2]

i_team,s_team = result (i_team, s_team)
i_team,p_team = result (i_team, p_team)
i_team,m_team = result (i_team, m_team)
s_team,p_team = result (s_team, p_team)
s_team,m_team = result (s_team, m_team)
p_team,m_team = result (p_team, m_team)

i_team[4] = (3 * i_team[0]) + i_team[2]
s_team[4] = (3 * s_team[0]) + s_team[2]
p_team[4] = (3 * p_team[0]) + p_team[2]
m_team[4] = (3 * m_team[0]) + m_team[2]

r = [i_team, s_team, p_team, m_team]

for i in range (4):
    for j in range (i, 4):
        if (r[i][4] < r[j][4]):
            r[i],r[j] = r[j],r[i]
        elif (r[i][4] == r[j][4] and r[i][0] < r[j][0]):
            r[i],r[j] = r[j],r[i]
        elif (r[i][4] == r[j][4] and r[i][0] == r[j][0] and r[i][5] > r[j][5]):
            r[i],r[j] = r[j],r[i]
for i in range (4):
    if (r[i][5] == 1):
        print ("Iran", end = "  ")
    elif (r[i][5] == 2):
        print ("Morocco", end = "  ")
    elif (r[i][5] == 3):
        print ("Portugal", end = "  ")
    elif (r[i][5] == 4):
        print ("Spain", end = "  ")
    print ("wins:" + str (r[i][0]) + " , " + "loses:" + str (r[i][1]) + " , " + "draws:" + str (r[i][2]) + " , " + "goal difference:" + str (r[i][3]) + " , " + "points:" + str (r[i][4]))
