import cv2
import pytesseract

myData = []

################################### NUMBER_PLATE_DETECTION ###################################

# ######################################################
# frameWidth = 640
# frameHeight = 480
# nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
# minArea = 500
# color = (255,0, 255)
# ######################################################

# cap = cv2.VideoCapture("Resources/10cars.mp4")
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
# cap.set(10,10)
# count = 0
#
# while True:
#     success, img = cap.read()
#     h, w, c = img.shape
#     img = cv2.resize(img, (w // 2, h // 2))
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
#     for (x, y, w, h) in numberPlates:
#         area = w*h
#         if(area > minArea):
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#             cv2.putText(img, "Number Plate", (x,y-5),
#                         cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,color,2)
#             imgRoi = img[y:y+h, x:x+w]
#             cv2.imshow("ROI", imgRoi)
#
#     cv2.imshow("Result",img)
#
#     if cv2.waitKey(1) & 0xFF ==ord('s'):
#         cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
#
#         cv2.rectangle(img,(0,200), (640,300), (0,255,0), cv2.FILLED)
#         cv2.putText(img, " Scan Saved", (150,265), cv2.FONT_HERSHEY_DUPLEX,
#                     2, (0,0,255),2)
#         cv2.imshow("Result", img)
#         cv2.waitKey(500)
#         count +=1
################################################################################################

######################################## TEXT_DETECTION ########################################


print("######################### Extracting Data from images #########################")
for item in range(9):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    img = cv2.imread("Resources/Scanned/NoPlate_" + str(item) + ".jpg")
    h,w,c = img.shape
    img = cv2.resize(img, (w*2, h*2))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    myData.append(pytesseract.image_to_string(img))
    cv2.imshow('result', img)
    cv2.waitKey(100)

print(myData)
with open('data.csv', 'a+') as f:
    for data in myData:
        f.write(str(data))
