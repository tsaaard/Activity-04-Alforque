import cv2
from time import sleep
from os import system

print("""Select image type:
 1 = loads a colored image
 0 = loads image in grayscale
-1 = loads a colored image with transparency""")
flag = int(input("Enter option: "))

if flag > 1 or flag < -1:
    print("Invalid Input. Closing program")
    sleep(3)
    exit()

print("""
Select from these image:
1. gojo.jpg
2. ayane.jpg
3. marin.jpg
4. airi.jpg

or type 'add' if you add image to the same folder""")
opt = input("Input: ")
if opt == "add":
    system('cls')
    print("""NOTES: 
     > IMAGE MUST BE IN THE IMAGES FOLDER.
     > YOU CAN ADD IT WHILE THIS IS RUNNING.
     > INVALID INPUT WILL CLOSE THE PROGRAM.\n\n""")
    pat = input("Enter Image name and its extension (e.g. hello.jpg): ")
elif opt == '1':
    pat = 'gojo.jpg'
elif opt == '2':
    pat = 'ayane.jpg'
elif opt == '3':
    pat = 'marin.jpg'
elif opt == '4':
    pat = 'airi.jpg'
else:
    print("Invalid Input. Closing program")
    sleep(3)
    exit()

filePath = "images/" + pat

image = cv2.imread(filePath, flag)

cv2.imshow("airi", image)

cv2.waitKey(0)

cv2.destroyAllWindows()