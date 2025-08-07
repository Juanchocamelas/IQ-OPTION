from PIL import Image # Manejo de imagenes
import numpy as np # Para manejo de calculos matematicas
import os # Para manejar los archivos

# Funcion que procesa imagenes, se encarga de recortar 

def procesar_imagen_a_matriz(ruta_imagen): # Pasarle los archivos de dataSet, y el tamaño de las imagenes

    try:
        # Cargar la imagen, redimensionar y convertir a RGBA
        img = Image.open(ruta_imagen).convert("RGBA") 
        img_array = np.array(img)


        # Lienzo transparente para dibujar segun las dimensiones de la imagen pasada
        resultado_array = np.zeros(img_array.shape, dtype=np.uint8) 
        print (f"Estas son las dimensiones de resultado_array estado neutro: {resultado_array.shape}")

        # Desempaquetar canales de color
        r, g, b, a = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2], img_array[:,:,3]

        es_solido = a > 100  # Evitar píxeles casi invisibles
        es_verde = (g > r) & (g > b) & es_solido  # Es verde si el canal verde es el más alto
        es_rojo = (r > g) & (r > b) & es_solido   # Es rojo si el canal rojo es el más alto

        resultado_array[es_verde] = (0, 200, 5, 180)     # Verde IQ Option (alcista)
        resultado_array[es_rojo]  = (255, 45, 45, 180)   # Rojo IQ Option (bajista)

        # Eliminar pixel invisible 
        mask = resultado_array.any(axis=2) #Eliminar filas, altura, donde no haya ningun pixel verde o rojo

        # Calcular dimensiones activas según la máscara
        altura = np.any(mask, axis=1)     # filas validas, componen altura
        anchura = np.any(mask, axis=0)    # columnas validas, componen anchura

        print(f"Nueva altura: {np.sum(altura)}, Nueva anchura: {np.sum(anchura)}")

        matriz_final = resultado_array[altura] [:, anchura, :] # shape (h, w, 4) en conjunto
        print(f"Esta son las dimensiones de la matriz_final:  {matriz_final.shape}")
        
        # Desempaquetacion
        h, w, c = matriz_final.shape
        return matriz_final, h, w  # matriz_final  #altura → h, anchura → w

    except Exception as e:
        print(f"Error procesando la imagen {ruta_imagen}: {e}")
        return None, None, None

if __name__ == '__main__':
    ruta_prueba = "prediccion/hola.png"
    if os.path.exists(ruta_prueba):
        matriz_resultado, nueva_altura, nueva_anchura = procesar_imagen_a_matriz(ruta_prueba) #Array numpy imagen overplay, nueva altura y anchura luego de la transformacion
        if matriz_resultado is not None:
            print("Procesamiento de prueba exitoso. Mostrando imagen.")
            print(f"Dimensiones altura y anchura filtradas: {nueva_altura} x {nueva_anchura}")
            imagen_final = Image.fromarray(matriz_resultado, 'RGBA') # Lee el array que contiene una secuencia de pixeles
            print(f"Contenido de matriz_resultado despues del filtro: {matriz_resultado}")
            imagen_final.show() # mostrar imagen sin filas con canales RGBA en 0
        else:
            print("La matriz resultado es None. No se pudo procesar.")
    else:
        print(f"No se encontró la imagen de prueba en '{ruta_prueba}'")
     
