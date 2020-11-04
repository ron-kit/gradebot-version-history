import random
while True:
    stu,coin,sides,bounds,ib = int(input("# of students to be graded: ")),int(input("# of coins to be flipped: ")),[-1,1], [(0,4),(5,7),(8,9),(10,11),(12,14),(15,16),(17,20)],0
    for i in range(stu):
        grade = [3,3,3,3]
        
        for g in range(coin):
            ctg = random.randint(0,3)
            if grade[ctg] == 1: grade[ctg] = 2
            if grade[ctg] == 5: grade[ctg] = 4
            else:
                flip = random.choice(sides)
                grade[ctg] += flip
        for i in range(7): #im bad with arrays so bob helped with this part, thanks bob
            if bounds[i][0] <= sum(grade) <= bounds[i][1]: 
                ib=i+1
                break
        print(grade,sum(grade),ib) 

    print("These are the grades of "+str(stu)+" students generated with "+str(coin)+" coin flips.")