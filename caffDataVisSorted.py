import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import pprint

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

caffDic = {}

with open('caffData.csv', 'r') as dataIn:
    csvReader = csv.reader(dataIn, delimiter = ',')
    lineCnt = 0
    for row in csvReader:
        if lineCnt == 0:
            lineCnt += 1
            continue
        else:
            item = row[0]
            foodType = row[1]
            caff = int(row[2])
            caffDic[item] = {'foodType':foodType,'caffContent':caff}
            lineCnt += 1
            
hotDrinks = [(k,caffDic[k]['caffContent']) for k in caffDic if caffDic[k]['foodType'] == 'Hot Drink']
hotDrinks.sort(key = lambda x:x[1], reverse = True)

food = [(k,caffDic[k]['caffContent']) for k in caffDic if caffDic[k]['foodType'] == 'Chocolate']
food.sort(key = lambda x:x[1], reverse = True)

softDrinks = [(k,caffDic[k]['caffContent']) for k in caffDic if caffDic[k]['foodType'] == 'Soft Drink']
softDrinks.sort(key = lambda x:x[1], reverse = True)

energyDrinks = [(k,caffDic[k]['caffContent']) for k in caffDic if caffDic[k]['foodType'] == 'Energy Drink']
energyDrinks.sort(key = lambda x:x[1], reverse = True)

medication = [(k,caffDic[k]['caffContent']) for k in caffDic if caffDic[k]['foodType'] == 'Medication']
medication.sort(key = lambda x:x[1], reverse = True)

joinedList = [('',0)] + medication + hotDrinks + softDrinks + [('',0)] + energyDrinks + food

contCaffVals = [i[1] for i in joinedList]
labels = [i[0] for i in joinedList]

iN = len(contCaffVals)
arrCnts = np.array(contCaffVals)
theta=np.arange(0,2*np.pi,2*np.pi/iN)
width = (2*np.pi)/iN *0.9

fig = plt.figure(figsize = (8,8))
ax = fig.add_axes([0.1, 0.1, 0.75, 0.75], polar=True)
bars = ax.bar(theta, arrCnts, width=width, bottom=200, color=([]), edgecolor='black')
ax.xaxis.grid(b=None)
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])

# Below = add labels. Do properly in illustrator for final fig...

rotations = np.rad2deg(theta)
y0,y1 = ax.get_ylim()

for x, bar, rotation, label in zip(theta, bars, rotations, labels):
 offset = (200 + bar.get_height())/(y1-y0)
 lab = ax.text(0, 0, label, transform=None, 
         ha='center', va='center')
 renderer = ax.figure.canvas.get_renderer()
 bbox = lab.get_window_extent(renderer=renderer)
 invb = ax.transData.inverted().transform([[0,0],[bbox.width,0] ])
 lab.set_position((x,offset+(invb[1][0]-invb[0][0])/2.*2.7 ) )
 lab.set_transform(ax.get_xaxis_transform())
 lab.set_rotation(rotation)

# plt.savefig("caffDataGrouped.pdf", transparent=True)
