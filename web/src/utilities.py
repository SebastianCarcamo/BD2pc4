import face_recognition
import math

def ED(vector1, vector2):
	res = 0
	for i in range(len(vector1)):
		res+= math.pow(vector1[i]-vector2[i],2)
	return math.sqrt(res)

def MD(vector1,vector2):
	res = 0
	for i in range(len(vector1)):
		res+= abs(vector1[i]-vector2[i])
	return res

def read_face(image_path):
	img = face_recognition.load_image_file(image_path)
	vec = face_recognition.api.face_encodings(img)
	return vec

