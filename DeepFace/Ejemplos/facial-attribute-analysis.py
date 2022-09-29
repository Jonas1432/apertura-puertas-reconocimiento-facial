from deepface import DeepFace

obj = DeepFace.analyze(img_path = "/home/jonathan/apertura-puertas-reconocimiento-facial/DeepFace/Face/aigeneratedFace1.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print("El resultado del analisis es: ")
print(obj)