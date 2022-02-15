import pytesseract
from pytesseract import Output
import PIL.Image
import cv2
myconfig =r"--psm 11 --oem 3"

'''text = pytesseract.image_to_string(PIL.Image.open("c:/Users/ghada/Desktop/tesseract/signs.png"), config=myconfig)
print(text)'''

img = cv2.imread("c:/Users/ghada/Desktop/tesseract/l.jpg")
height, width, _ = img.shape
'''
boxes = pytesseract.image_to_boxes(img, config=myconfig)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0,255,0))

cv2.imshow("img",img)
cv2.waitKey(0)
'''
data= pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
print

