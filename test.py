from calendar import c
import cv2
import numpy as np

# Kante 1: img[0, 0] bis img[0, 99] => links
# Kante 2: img[0, 99] bis img[99, 99] => unten
# Kante 3: img[99, 99] bis img[99, 0] => rechts
# Kante 4: img[99, 0] bis img[0, 0] => oben

# r = 2
# g = 0
# b = 1

eingabeDS = []

for i in range(1, 13):
    eingabeDS.append([])
    # if (i < 10):
    #     path = "./images/image_part_00" + str(i) + ".jpg"
    # else:
    #     path = "./images/image_part_0" + str(i) + ".jpg"
    path = "./images/image2/" + str(i) + ".jpg"
    img = cv2.imread(path)
    hh, ww = img.shape[:2]
    eingabeDS[i-1].append([])
    for y in range(0, 200):
        eingabeDS[i-1][0].append([img[0, y, 0], img[0, y, 1], img[0, y, 2]])
    eingabeDS[i-1].append([])
    for x in range(0, 200):
        eingabeDS[i-1][1].append([img[x, 199, 0], img[x, 199, 1], img[x, 199, 2]])
    eingabeDS[i-1].append([])
    for y in range(199, -1, -1):
        eingabeDS[i-1][2].append([img[199, y, 0], img[199, y, 1], img[199, y, 2]])
    eingabeDS[i-1].append([])
    for x in range(199, -1, -1):
        eingabeDS[i-1][3].append([img[x, 0, 0], img[x, 0, 1], img[x, 0, 2]])
    # print(eingabeDS)

def compareEdges(edge1, edge2):
    error = 0
    for i in range(len(edge1)):
        pxlError = 0
        for j in range(len(edge1[i])):
            pxlError += abs(int(edge1[i][j]) - int(edge2[i][j]))
        error += pxlError^2
    return error


for k in range(4):
    print("Kante " + str(k+1) + ":")
    results = {}
    for j in range(1, 12):
        # print("Bild " + str(j+1) + ":")
        for i in range(4):
            # print(" Kante " + str(i+1) + ":")
            # print("  " + str(compareEdges(eingabeDS[0][2], eingabeDS[j][i])))
            results[str(j+1) + "-" + str(i+1)
                    ] = compareEdges(eingabeDS[0][k], eingabeDS[j][i])
    # print(results)
    print({k: v for k, v in sorted(results.items(), key=lambda item: item[1])})
