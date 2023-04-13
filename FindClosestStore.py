import geopy.distance
import csv

myStores = []
customers = []
outputList = []

#Input list containing data with headers in a "LocationIdentifier,  X(Long), Y(Lat)
with open("myStores.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        myStores.append(row)

#Input list containing data with headers in a "CustomerIdentifier,  X(Long), Y(Lat)
with open("customers.csv", 'r') as file2:
    csvreader = csv.reader(file2)
    header = next(csvreader)
    for row in csvreader:
        customers.append(row)
#Add the header 
outputList.append(["Customer", "Closest Store", "Distance"])

for Customer in customers:
    print("processing " + Customer[0])
    distanceToTrain = []
    for DestinationStore in myStores:
        #Source file was backwards, didnt want to correct it
        #Function takes y,x lat,long
        coords_1 = (Customer[2], Customer[1])
        coords_2 = (DestinationStore[2], DestinationStore[1])
        distance = geopy.distance.geodesic(coords_1, coords_2).miles
        distanceToTrain.append([Customer[0], DestinationStore[0], distance])
    distanceToTrain.sort(key=lambda x:x[2])
    outputList.append(distanceToTrain[0])

#Output the list to a CSV (will truncate existing file if exists or create if no file exists)
f = open('output.csv', 'w+', newline='')
# create the csv writer
writer = csv.writer(f)
# write a row to the csv file
writer.writerows(outputList)
