import random

while True:
    students,flips,coffee,split,change,sumall,ib,bounds = int(input("# of students to be graded: ")),int(input("# of random grade changes: ")),str(input("quality of coffee (good, ok, bad):")),0,0,0,0,[(0,4),(5,7),(8,9),(10,11),(12,14),(15,16),(17,20)]
    
    for i in range(students):
        grade = [3,3,3,3]
        
        if coffee == "good": split = -.5
        if coffee == "ok": split = 0
        if coffee == "bad": split = .5
        else: split = random.randint(-1,1)*.5
        #print(coffee)
        #print(split)
        
        for g in range(flips):
            category = random.randint(0,3)
            change = 1 - 2 * random.random()
            if change < split and grade[category] > 1: grade[category] -= 1 
            if change >= split and grade[category] < 5: grade[category] += 1
            split *= 1 - 1/flips
            #print(split)
            
        for i in range(len(bounds)): #I am bad with arrays so bob helped with this part, thanks bob
            if bounds[i][0] <= sum(grade) <= bounds[i][1]: 
                ib = i+1
                break
        
        print(grade,"TOTAL SCORE:",sum(grade)," IB GRADE",ib)
        sumall += sum(grade)
        #print(sumall)

    print("These are the grades of " + str(students) + " students generated with " + str(flips) + " random changes each.")
    print("Average grade: " + str(sumall/students))