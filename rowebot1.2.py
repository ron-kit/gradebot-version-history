import random
while True:
    students,flips,coffee,split,coin,ib,bounds = int(input("# of students to be graded: ")),int(input("# of coins flipped: ")),input("Quality of Mr. Rowe's Coffee (good, ok, bad):"),0,0,0,[(0,4),(5,7),(8,9),(10,11),(12,14),(15,16),(17,20)]
    if coffee == "good": split = .5
    if coffee == "ok": split = 0
    if coffee == "bad": split = -.5
    else: split = random.randint(-1,1)*.5
    
    for i in range(students):
        grade = [3,3,3,3]
        
        for g in range(flips):
            category = random.randint(0,3)
            coin = 1 - 2 * random.random()
            if coin < split and grade[category] > 1: grade[category] -= 1 
            if coin >= split and grade[category] < 5: grade[category] += 1
            split *= 1 - 1/max(flips,20)
            #print(split)

        for i in range(7): #I am bad with arrays so bob helped with this part, thanks bob
            if bounds[i][0] <= sum(grade) <= bounds[i][1]: 
                ib = i+1
                break
        print(grade,"TOTAL MARK:",sum(grade),"IB GRADE",ib)
        #print(split)

    print("These are the grades of " + str(students) + " students generated with " + str(flips) + " coin flips each.")