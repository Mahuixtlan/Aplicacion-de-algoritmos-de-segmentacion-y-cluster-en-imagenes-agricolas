import cv2 
import matplotlib.pyplot as plt 

def imshow(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def informacion(img,bandera):
    #calculamos los detalles basicos de la imagen 
    #numero de dimensiones 
    ndimensiones = img.ndim
    #calculamos alto, ancho y canales 
    if bandera == 1:
        alto,ancho,canales = img.shape
    elif bandera ==2:
        alto,ancho = img.shape
    #calculamos el numero de pxeles de nuestra imagen
    npixeles = alto * ancho
    #calculamos la dimension de nuestra imagen 
    numbytes = img.nbytes
    #tipo de datos de los pixeles
    tipo_dato = img.dtype
    
    
    #imprimimos nuestros datos
    print(f'Nuestra imagen tiene: {ndimensiones} dimensiones')
    if bandera == 1:
        print(f'la imagen mide alto: {alto} ancho: {ancho} y tiene: {canales} canales')
    elif bandera == 2: 
        print(f'La imagen mide alto: {alto} ancho: {ancho}')
    print(f'por lo tanto nuestra imagen tiene {npixeles} pixeles')
    print(f'nuestra imagen tiene una dimension de {numbytes} bytes')  
    print(f'La imagen trabaja con datos del tipo: {tipo_dato}\n')
     
    return alto ,ancho

def procesamiento(img):
    #cargamos la imagen
    imagen = cv2.imread(img)
    #mostramos la imagen 
    imshow(imagen)
    
    #pasamos la iagen a RGB
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    imshow(imagen)
    
    #calculamos los detalles basicos de la imagen 
    print('Informacion imagen original')
    alto, ancho = informacion(imagen,1)
    
    #para un adecuado procesamiento redimenzionaremos nuestra imagen 
    #en este caso solo se redujieron sus dimensiones a la mitad pero podemos cambiar este paametro 
    new_tamaño = (ancho//2,alto//2)
    imagen = cv2.resize(imagen,new_tamaño)
    
    #mostramos nuestraimagen redimensionada 
    imshow(imagen)
    
    #calculamos los datos de nuestra imagen de nuevo para ver si han cambiado 
    print('Informacion imagen redimensionada')
    informacion(imagen,1)
    
    '''
    podemos observar como solo han cambiado algunos atributos de nuestra imagen, los cuales son alto ancho y numero de pixeles, 
    sin embargo tambien cambia la dimension de la imagen, la cual se hace mas pequeña, y esto es por que se redujo su tamaño haciendola mas facil procesar
    y tods los demas atributos se mantiene iguales ya que son caracteristcas que no dependen del tamaño de la imagen 
    '''
    
    # canales de la imagen 
    #con la siguiente linea podemos obtener los valores en los tres canales de cualquier pixel en nuestra imagen 
    pixel_value = imagen[0,0]
    print(pixel_value, '\n')
    
    #ahora dividiremos nuestra imagen en sus tres canales 
    r,g,b = cv2.split(imagen)
    
    #mostraremos los canales de nuestra imagen 
    #canal rojo 
    fig, axs = plt.subplots(3,1,figsize=(5,15))
    
    axs[0].imshow(r,cmap ='gray')
    axs[0].set_title('capa roja')
    axs[0].axis('off')
    
    axs[1].imshow(g, cmap ='gray')
    axs[1].set_title('capa verde')
    axs[1].axis('off')
    
    axs[2].imshow(b, cmap ='gray')
    axs[2].set_title('capa azul')
    axs[2].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    #hallaremos la informacion basca de cada capa para ver cuanto ha cambiado respecto a la imagen original 
    print('informacion canal rojo')
    informacion(r,2)
    print('informacion canal verde')
    informacion(g,2)
    print('Informacion canal azul')
    informacion(b,2)
    
    
    #haremos estadisticas de pixeles 
    
    #minimos y maximos de los pixeles en cada canal 
    minvalr,maxvalr,minlocr,maxlocr = cv2.minMaxLoc(r)
    minvalg,maxvalg,minlocg,maxlocg = cv2.minMaxLoc(g)
    minvalb,maxvalb,minlocb,maxlocb = cv2.minMaxLoc(b)
    
    print(f'El valor minimo es: {minvalr} localizado en {minlocr} el valor maximo es {maxvalr} localizado en {maxlocr}')
    print(f'El valor minimo es: {minvalg} localizado en {minlocg} el valor maximo es {maxvalg} localizado en {maxlocg}')
    print(f'El valor minimo es: {minvalb} localizado en {minlocb} el valor maximo es {maxvalb} localizado en {maxlocb}')
    
    #mostraremos los pixeles hallados en la imaegn 
    #creamos una copia de la imagen
    minymaxr = imagen.copy()
    copiar = r.copy()
    
    #los minimos estaran en circulos y los maximos en cuadrados 
    
    #capa roja
    cv2.circle(minymaxr,minlocr,5,(255,0,0),2)
    cv2.circle(copiar,minlocr,5,(255,0,0),2)
    
    cv2.circle(minymaxr,maxlocr,5,(255,0,0),2)
    cv2.circle(copiar,maxlocr,5,(255,0,0),2)
    
    fig, axs = plt.subplots(2,1,figsize=(5,10))
    
    axs[0].imshow(minymaxr)
    axs[0].set_title('minimos y maximos de la capa roja en la imagen original')
    axs[0].axis('off')
    
    axs[1].imshow(copiar)
    axs[1].set_title('minimos y maximos en la capa roja')
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    
    #capa verde 
    #imagenes copia 
    minymaxg = imagen.copy()
    copiag = g.copy()
    
    cv2.circle(minymaxg,minlocg,5,(0,255,0),2)
    cv2.circle(copiag,minlocg,5,(0,255,0),2)
    
    cv2.circle(minymaxg,maxlocg,5,(0,255,0),2)
    cv2.circle(copiag,maxlocg,5,(0,255,0),2)
    
    fig, axs = plt.subplots(2,1,figsize=(5,10))
    
    axs[0].imshow(minymaxg)
    axs[0].set_title('minimos y maximos de la capa VERDE en la imagen original')
    axs[0].axis('off')
    
    axs[1].imshow(copiag)
    axs[1].set_title('minimos y maximos en la capa VERDE')
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    
    #capa AZUL
    #imagenes copia 
    minymaxB = imagen.copy()
    copiaB = b.copy()
    
    cv2.circle(minymaxB,minlocb,5,(0,0,255),2)
    cv2.circle(copiaB,minlocb,5,(0,0,255),2)
    
    cv2.circle(minymaxB,maxlocb,5,(0,0,255),2)
    cv2.circle(copiaB,maxlocb,5,(0,0,255),2)
    
    fig, axs = plt.subplots(2,1,figsize=(5,10))
    
    axs[0].imshow(minymaxB)
    axs[0].set_title('minimos y maximos de la capa VERDE en la imagen original')
    axs[0].axis('off')
    
    axs[1].imshow(copiaB)
    axs[1].set_title('minimos y maximos en la capa VERDE')
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    
    
    
    

procesamiento('img1.jpg')