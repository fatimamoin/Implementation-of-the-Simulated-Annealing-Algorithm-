import random
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def func(x,y):
    return x**2 + y**2 #function 1
   # return 100*(x**2 - y**2) + (1-x)**2 #function 2
   # return (((x**2) + (y**2))/4000) - (math.cos(x)*math.cos(y/math.sqrt(2))) + 1

def startrandom(range_x, range_y):
    x= random.randint(range_x[0], range_x[1])
    y= random.randint(range_y[0], range_y[1])

    return x,y

def Neighbor(x,y,range_x, range_y,step):
    neigbors=[[x+step,y], [x-step,y], [x,y+step], [x,y-step], [x+step,y + step],
              [x-step,y + step], [x-step,y-step], [x+step,y - step]] #create neighbors
    neigbors[:] = [neigbors[i] for i in range(len(neigbors)) if neigbors[i][0] >= range_x[0] and neigbors[i][0] <= range_x[1] and neigbors[i][1] >= range_y[0] and neigbors[i][1] <= range_y[1]]
    prob = random.randint(0, len(neigbors)-1)
    return neigbors[prob]

   
def simulate(step, factor_temp, initial_temp,final_temp, range_x, range_y, point):
    x, y = startrandom(range_x, range_y)
    z_val=[]
    y_val=[]
    x_val=[]
    iteration = []
    while initial_temp > final_temp:
        for i in range(10):
            neighbor= Neighbor(x ,y, range_x, range_y, step)
            change= func(neighbor[0], neighbor[1]) - func(x,y)
            if point == "Maximum":
                if change > 0:
                    x,y = neighbor[0], neighbor[1] 
                else:
                    prob= random.uniform(0,1)
                    value= math.exp(change/initial_temp)
                    if prob < value:
                        x,y = neighbor[0], neighbor[1]
            if point == "Minimum":
                if change < 0:
                    x, y = neighbor[0], neighbor[1]
                else:
                    prob= random.uniform(0,1)
                    value= math.exp(- change/initial_temp)
                    if prob > value:
                        x,y = neighbor[0], neighbor[1]
            x_val.append(x)
            y_val.append(y)
            z_val.append(func(x,y))
            if len(iteration) == 0:
                iteration.append(1)
            else:
                iteration.append(iteration[len(iteration)-1] + 1)
                
        initial_temp = initial_temp*factor_temp
       
    
    fig, axs = plt.subplots(2)
    axs[0].plot(iteration, z_val, label="z value")
    axs[1].plot(iteration, y_val, label="y value")
    axs[1].plot(iteration, x_val, label="x value")
    axs[0].set_title('func(x,y) against number of iterations',fontsize =9)
    axs[1].set_title('x and y against number of iterations', fontsize =9)
    axs[1].legend(loc ="upper right")
    axs[0].legend(loc ="upper right")
    plt.tight_layout()
    plt.show()
    return x,y, func(x,y)
            
        
    

range_x, range_y = (-5,5),(-5,5) #Function 1 range
#range_x, range_y = (-2,2),(-1,3) #Function 2 range
#range_x, range_y = (-100,100),(-100,100) #Function 3 range

step = 0.1
factor_temp= 0.9
initial_temp = 1000
final_temp = 1
print(simulate(step, factor_temp, initial_temp,final_temp, range_x,
               range_y, point="Minimum"))

#Note: Depending on what you are trying to find, please make it Minimum or Maximum
