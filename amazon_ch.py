## Amazon Coding Challenge 2022
# Start: 21/6/2022
# By: Mohammed Yasser


# Lets try first to implement the obstacles
from random import randint

#(Cancelled XXXX) I will try to implement them by using Dictionary as I think it will be easier to store them
#Ph1_obs = {9:7, 8:7, 6:7, 6:8}
# A key can't have keys with same values


#Lets try a list with x and a list with y
obs_x = [9, 8, 6, 6]
obs_y = [7, 7, 7, 8]

#Random Obsticles
for j in range(20):
    w = randint(1,10)
    z = randint(1,10)
    for i in range(len(obs_x)):
        if (obs_x[i]== w):
            if(obs_y[i] == z):
                w = randint(1,10)
                z = randint(1,10)
        if (w == 1):
            if(z == 1):
                w = randint(1,10)
                z = randint(1,10)
        if (w == 10):
            if(z == 10):
                w = randint(1,10)
                z = randint(1,10)
        
    obs_x.append(w)
    obs_y.append(z)

print("Obstacles: [", end="") 
for obsticle in range(len(obs_x)-1):
        print("(", obs_x[obsticle],",", obs_y[obsticle], ")", ", ", sep="", end="")
print("(", obs_x[-1], ',', obs_y[-1],')]', sep='')




steps_x = []
steps_y = []
last_move = []

# Lets start with the Algorithim

#Working_pathfinder1
# My initial idea is to check if the diagonal move is allowed as I think moving diagonaly is the fastest way
# If a diagonal move isn't allowed then downwards or right
# If not allowed then let or up


# Begining the list to be printed
print("Path: [", end="") 

#The Algorithim

# A working_pathfinder algorithim but not the best
def working_pathfind():
    x, y= 1, 1
    allowed = 1
    oops = 0
    

    while (x <= 10 and y <= 10 ):
        change = 0
        if(x>=9 and y>=9):
            break
        for i in range(len(obs_x)):
            if((x+1 == obs_x[i] and y+1 == obs_y[i]) or x==10 or y == 10):
                allowed = 0
                break
        if(allowed == 1 and x < 10 and y < 10):
            x += 1
            y += 1
            # print('(', x, ',', y, ')', ", ", sep='', end="")
            steps_x.append(x)
            steps_y.append(y)
            # c += 1
            last_move.append("diagonal")
            change = 1

        if(allowed == 0):
            allowed = 1

            for i in range(len(obs_x)):
                if (y+1 == obs_y[i]):
                    if (x == obs_x[i]):
                        allowed = 0 
                        break
            if(allowed == 1 and y != 10):
                y += 1
                # print('(', x, ',', y, ')', ", ", sep='', end="")
                # c+=1
                steps_x.append(x)
                steps_y.append(y)
                last_move.append("down")
                change =1
                continue
            allowed = 1
            for i in range(len(obs_x)):
                if(x+1 == obs_x[i] ):
                    if(y == obs_y[i]):
                        allowed = 0
                        break
            if(allowed == 1 and x != 10):
                x += 1
                # print('(', x, ',', y, ')', ", ", sep='', end="")
                # c+=1
                steps_x.append(x)
                steps_y.append(y)
                last_move.append("right")
                change = 1

            if (allowed == 0):
                if(last_move):
                    pass
                else:
                    print("Unable to reach deliviry point")
                    oops = 1
                    break
                     


                obs_x.append(x)
                obs_y.append(y)
                if(x == 1 and y == 1):
                    print("Unable to reach deliviry point]")
                    break
    
                if(last_move[-1] == "diagonal"):
                    x-=1
                    y-=1
                    del steps_x[-1]
                    del steps_y[-1]
                    del last_move[-1]
                    change=1
                if(last_move[-1] == "down"):
                    y-=1
                    del steps_x[-1]
                    del steps_y[-1]
                    del last_move[-1]
                    change =1
                if(last_move[-1] == "right"):
                    x-=1
                    del steps_x[-1]
                    del steps_y[-1]
                    del last_move[-1]
                    change =1
        if((x == 1 and y == 1) or change ==0):
            print("Unable to reach deliviry point]")
            oops = 1
            break
    if (oops == 1):
        pass
    else:   
        for step in range(len(steps_x)):
            print("(", steps_x[step],",", steps_y[step], ")", ", ", sep="", end="")
        print("(10,10)]","Number of steps:", len(steps_x)+1)

        




working_pathfind()
