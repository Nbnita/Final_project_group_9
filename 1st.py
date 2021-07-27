import cv2
import numpy as np
import face_recognition
import os

path = 'images'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
encodeListKnown = findEncoding(images)
print(len(encodeListKnown))
#img= face_recognition.load_image_file('images/test.jpg')
while True:
    img = cv2.imread("images/petal sikari.jpg", cv2.IMREAD_COLOR)
    imgSmall = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgSmall= cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodeCurFaces = face_recognition.face_encodings(imgSmall, facesCurFrame)

    for encodeFace , faceLoc in zip(encodeCurFaces,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDist)
        matchIndex = np.argmin(faceDist)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)

            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img, name , (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            #QmarkAttendance(name)

    cv2.imshow('webcam',img)
    cv2.waitKey(1)
'''imgMe = face_recognition.load_image_file('images/test.jpg')
imgMe = cv2.cvtColor(imgMe, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('images/nabanita.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgMe)[0]
encodeMe = face_recognition.face_encodings(imgMe)[0]
cv2.rectangle(imgMe, (faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]), (255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]), (255,0,255),2)
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[2]-35),(faceLocTest[1],faceLocTest[2]),(0,255,0),cv2.FILLED)

results = face_recognition.compare_faces([encodeMe],encodeTest)
faceDis = face_recognition.face_distance([encodeMe], encodeTest)
matchIndex = np.argmin(faceDis)
if results[matchIndex]:
    name = classNames[matchIndex].upper()
    cv2.putText(imgTest,name,(faceLocTest[3]+6,faceLocTest[2]-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
print(results)
print(faceDis)

cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Me', imgMe)
cv2.imshow('Me Test', imgTest)
cv2.waitKey(0)
for encodeFace, faceLoc1 in zip(encodeTest, faceLocTest):
    matches = face_recognition.compare_faces([encodeMe],encodeTest)
    faceDist = face_recognition.face_distance([encodeMe], encodeTest)
    # print(faceDist)
matchIndex = np.argmin(faceDist)
if matches[matchIndex]:
    name = classNames[matchIndex].upper()
        # print(name)

    y1, x2, y2, x1 = faceLoc1
    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#markAttendance(name)'''