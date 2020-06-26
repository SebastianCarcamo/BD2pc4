import face_recognition
import math
import numpy as np
import sys
import os
import pickle

PATH = "./lfw/"




# image1 = face_recognition.load_image_file("./lfw/Joe_Gatti/Joe_Gatti_0002.jpg")
# image2 = face_recognition.load_image_file("./lfw/Abdullah/Abdullah_0003.jpg")
# vec1 = face_recognition.api.face_encodings(image1)
# vec2 = face_recognition.api.face_encodings(image2)

# print(face_recognition.api.face_encodings(image1)[0])

faces = []
for subdir, dirs, files in os.walk(PATH):
	for direct in dirs:
		print(direct)
		for i in os.listdir(PATH + direct):
			img = face_recognition.load_image_file(PATH + direct + "/" + i)
			vec = face_recognition.api.face_encodings(img)
			if len(vec) > 0:
				tmp = [direct]
				tmp.append(vec[0].tolist())
				faces.append(tmp)


with open('result.pkl','wb') as f:
	pickle.dump(faces,f)


# with open('result.pkl', 'rb') as f:
# 	test = pickle.load(f)


# print("ED:")
# print(ED(vec1[0],vec2[0]))
# print("MD:")
# print(MD(vec1[0],vec2[0]))