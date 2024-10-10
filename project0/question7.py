class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_age (self):
        return self.age

    def get_height (self):
        return self.height
    
    def get_weight (self):
        return self.weight

def find_age_avg (n, c):
    sum_age = 0
    for i in range (n):
        sum_age = sum_age + c[i].get_age ()
    avg_age = sum_age / n
    return avg_age

def find_height_avg (n, c):
    sum_height = 0
    for i in range (n):
        sum_height = sum_height + c[i].get_height ()
    avg_height = sum_height / n
    return avg_height

def find_weight_avg (n, c):
    sum_weight = 0
    for i in range (n):
        sum_weight = sum_weight + c[i].get_weight ()
    avg_weight = sum_weight / n
    return avg_weight

n1 = int (input ())
ages = str (input ()).split ()
heights = str (input ()).split ()
weights = str (input ()).split ()
c1 = []

for i in range (n1):
    age = int (ages[i])
    height = int (heights[i])
    weight = int (weights[i])
    s = Student (age, height, weight)
    c1.append (s)

n2 = int (input ())
ages = str (input ()).split ()
heights = str (input ()).split ()
weights = str (input ()).split ()
c2 = []

for i in range (n2):
    age = int (ages[i])
    height = int (heights[i])
    weight = int (weights[i])
    s = Student (age, height, weight)
    c2.append (s)

age_avg1 = find_age_avg (n1, c1)
height_avg1 = find_height_avg (n1, c1)
weight_avg1 = find_weight_avg (n1, c1)
age_avg2 = find_age_avg (n2, c2)
height_avg2 = find_height_avg (n2, c2)
weight_avg2 = find_weight_avg (n2, c2)

print (age_avg1)
print (height_avg1)
print (weight_avg1)

print (age_avg2)
print (height_avg2)
print (weight_avg2)

if (height_avg1 > height_avg2):
    print ("A")
elif (height_avg1 < height_avg2):
    print ("B")
else:
    if (weight_avg1 < weight_avg2):
        print ("A")
    elif (weight_avg1 > weight_avg2):
        print ("B")
    else:
        print ("Same")
