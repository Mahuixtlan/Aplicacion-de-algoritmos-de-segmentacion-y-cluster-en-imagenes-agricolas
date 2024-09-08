import cv2 
import matplotlib.pyplot as plt 
import numpy as np

imagen = cv2.imread('imagen_origen.jpg')
imagen_rgb = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
imagen_rgb = cv2.resize(imagen_rgb,(100,100))
plt.imshow(imagen_rgb)

pixeles = imagen_rgb.reshape((-1,3))
print(pixeles[:5])

pixeles = np.float32(pixeles)
print(pixeles[:5])

criterios = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,100,0.2)
wcss = []
for k in range(1,11):
    _,etiquetas,centroides = cv2.kmeans(pixeles,k,None,criterios,10,cv2.KMEANS_RANDOM_CENTERS)
    wcss.append(np.sum((pixeles - centroides[etiquetas])**2))

plt.plot(range(1,11), wcss,marker='o')


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111,projection='3d')

r,g,b = pixeles[:,0], pixeles[:,1],pixeles[:,2]

ax.scatter(r,g,b,c=pixeles/255,marker='o',s=1)

ax.set_xlabel('rojo')
ax.set_ylabel('verde')
ax.set_zlabel('azul')
ax.set_title('distribucion de colores')

plt.show()


