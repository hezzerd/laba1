import matplotlib.pyplot as plt
import math
import time 

start = time.time() #таймер пусть будет, чисто для души

log = open('examp_6.txt')

data = []
for line in log:
    data.append(line.split(";"))


position = []  #робота
lidar = []  #значения


for i in range(len(data)):

    result = []
    for j in data[i][0].split(', '):
        result.append(float(j))
    position.append(result)
    
    value_lidar = data[i][1][1:]

    res = []
    for j in value_lidar.split(", "):
        res.append(float(j))
    lidar.append(res)


vid_lidara = 240  

step = vid_lidara / len(lidar[0])  
print(step)
x_1 = []
y_1 = []

s = []
ugolok = -120

for i in range(len(lidar[0])):
    s.append(ugolok + step * i)


for i in range(len(lidar)):
    x = []
    y = []
    for j in range(len(lidar[i])):
        if lidar[i][j] < 5.6 and lidar[i][j] > 0.7:
            res_1 = (lidar[i][j] + 0.3) * math.cos(-s[j] * math.pi/180 + position[i][2])
            res_2 = (lidar[i][j] + 0.3) * math.sin(-s[j] * math.pi/180 + position[i][2])   
            x.append(res_1)
            y.append(res_2)
    x_1.append(x)
    y_1.append(y)


coordinates_all = []
position_all = []



for i in range(len(x_1)):
    for j in range(len(x_1[i])):
        x_1[i][j] = x_1[i][j] + position[i][0]
        y_1[i][j] = y_1[i][j] + position[i][1]

    plt.scatter(x_1[i], y_1[i], s = 1, color='black')
    plt.scatter(position[i][0], position[i][1], s = 1, color='red')
    plt.xlim((0, 15))
    plt.ylim((-7, 5))
    plt.pause(0.1)

plt.savefig("result.png")


end = time.time() - start

print(end)