import cv2
import face_recognition
import pickle
import os

def findEncodings(imgList):
    """
    This Function is to encode face img
    """
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def WriteEncode(encoded):
    """
    This function writes the encoded faces with ids to a face
    this would be in a file called EncodeFile
    """
    file = open("EncodeFace/EncodeFile.p", 'wb')
    pickle.dump(encoded, file)
    file.close()
    print("file has been computed")


#importing student images
folderPath = 'face_image'
imgPathList = os.listdir(folderPath)
imgList = []
peopleIds = []
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    #print(os.path.splitext(path)[0])
    peopleIds.append(os.path.splitext(path)[0])
#this print is to check if the for loop is getting the right amount of images from the folder
#print(len(imgList))
#this print displays the ids of the people in the list 
#print(peopleIds)
print("starting encoding img ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,peopleIds]
print("done encoding faces")
WriteEncode(encodeListKnownWithIds)
