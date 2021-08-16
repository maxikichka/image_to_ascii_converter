from PIL import Image
import numpy as np
import pyperclip

#$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#@%#*+=-:. 
gscale = "@%#*+=-:. "

img = Image.open(r"C:\Users\User\Pictures\chrome_dino_game_arduino_lcd.PNG").convert('L')
img = np.array(img)
newImg = [[]]
print(len(img), len(img[0]))

pixelSize = 10
pixelCount = pixelSize
pixel = []

print(np.array(img))
print()

asciiString = ""
i = 0
j = 0
x = 0
y = 0

while i < len(img[0]) and j < len(img):
    #print(i, j, x)
    pixel.append(img[j][i])
    i += 1
    if i >= pixelSize * (x + 1):
        #print("hi")
        i = pixelSize * x
        j += 1
    if j >= pixelSize * (y + 1):
        i = pixelSize * (x + 1)
        x += 1
        #print("x")
        #print(x)
        j -= pixelSize
        newImg[-1].append(sum(pixel) // len(pixel))
        pixel = []
        try:
            asciiString += (gscale[(newImg[-1][-1] * len(gscale))//255] * 2)
        except IndexError:
            asciiString += (" " * 2)
        #print("blah")
        #print(x)
    if i >= len(img[0]):
        newImg.append([])
        y += 1
        x = 0
        j += pixelSize
        i = 0
        asciiString += "\n"
print(i, j)
#print(newImg)
#print()
pyperclip.copy(asciiString)
print(asciiString)




##newImg = []
##tpX = 0
##tpy = 0
##for i in range(len(img)):
##    newImg.append([])
##    newImg[-1].append([])
##    for j in range(len(img[i])):
##        tpX = i * (len(img) // pixelSize) // len(img)
##        tpY = j * (len(img[i]) // pixelSize) // len(img[i])
##        print(tpX, tpY)
##        print(i, j)
##        newImg[tpX][tpY].append(img[i][j])
##        print(newImg)
##        if len(newImg[tpX][tpY]) == pixelSize:
##            newImg[tpX].append([])
##print(newImg)
