import csv
from collections import Counter

with open("HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(float(num))

n = len(new_data)
#mean
total = 0
for x in new_data:
    total+=x
mean = total/n
print("mean is: ",mean)

#median
new_data.sort()
if n%2==0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2+1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
print("The median is:", median)

#mode
data = Counter(new_data)
data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,


}

for height,occurance in data.items():
    if 75 <float(height)<85:
        data_for_range["75-85"]+=occurance
    elif 85 <float(height)<95:
        data_for_range["85-95"]+=occurance
    elif 95 <float(height)<105:
        data_for_range["95-105"]+=occurance
    elif 105 <float(height)<115:
        data_for_range["105-115"]+=occurance
    elif 115 <float(height)<125:
        data_for_range["115-125"]+=occurance
    elif 125 <float(height)<135:
        data_for_range["125-135"]+=occurance
    elif 135 <float(height)<145:
        data_for_range["135-145"]+=occurance
    elif 145 <float(height)<155:
        data_for_range["145-155"]+=occurance
    elif 155 <float(height)<165:
        data_for_range["155-165"]+=occurance
    elif 165 <float(height)<175:
        data_for_range["165-175"]+=occurance

mode_range,mode_occurance = 0,0
for range,occurance in data_for_range.items():

    if occurance > mode_occurance:
        mode_range = [int(range.split("-")[0]),int(range.split("-")[1])]
        mode_occurance=occurance  #67

mode = float((mode_range[0]+mode_range[1])/2)
print(mode)
print(occurance)