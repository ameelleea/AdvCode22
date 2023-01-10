file = open("sop.txt", "r")
sop = file.read()
file.close()

#print(sop)

def findMarkers(sop, num):
    markers = []

    for i in range(len(sop)):
        marker = sop[i-(num-1):i+1]
        marker = set(marker)
        if len(marker) == num:
            markers.append(i+1)
    
    return markers[0]

print(findMarkers(sop, 4))
print(findMarkers(sop, 14))




        

