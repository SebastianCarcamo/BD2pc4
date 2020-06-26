import face_recognition
import math
import pickle

 
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


class Secuential_KNN:
	def __init__(self, result_file):
		with open(result_file,'rb') as f:
			self.faces = pickle.load(f)

	def KNN_Faces(self,image_path,n):
		img = face_recognition.load_image_file(image_path)
		vec = face_recognition.api.face_encodings(img)
		if len(vec) == 0:
			print("The image couldn't be identified")
		else:
			ed_order = sorted(self.faces,key=lambda x: ED(vec[0],x[1]))
			md_order = sorted(self.faces,key=lambda x: MD(vec[0],x[1]))
		return [item[0] for item in ed_order[:n]] , [item[0] for item in md_order[:n]]

# ####################################
# sknn = Secuential_KNN('result.pkl')

# print(sknn.KNN_Faces('./lfw/Gloria_Macapagal_Arroyo/Gloria_Macapagal_Arroyo_0001.jpg',16))
####################################