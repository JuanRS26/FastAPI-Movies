import pandas as pd
import gradio as gr
from surprise import Dataset, Reader
from surprise import SVD

# Creamos una funcion para conocer los generos de la pelicula que el usuario digito
def movieGender(id):
    for i in range(0, len(totalMovies)):
        if totalMovies.Id.loc[i] == id:     # Se hace un filtro buscando la pelicula que el usuario digito 
            return totalMovies.listed_in.loc[i] # Retorna un


# Se cargan los sets de datos necesarios 
totalRatings = pd.read_parquet('Datasets/TransformedDataSet/Ratings/totalRatings.parquet')
totalMovies = pd.read_csv('Datasets/TransformedDataSet/totalMovies.csv')

setTrain = totalMovies.merge(totalRatings, left_on = 'Id', right_on = 'movieId')    # Se convinan los dos set de datos que cargamos y emparejarlos por medio del ID de las peliculas
setTrain = setTrain[['userId', 'listed_in', 'rating_y']]         # Se escoge las tres columnas que se van a utilizar y las ponemos en orden para que el modelo pueda leerlo bien


# ----------------------------Entrenamiento del modelo--------------------------------------------

# Pasamos nuestro dataframe llamado 'setTrain' a un dataframe de la libreria surprise para poder manipular los datos
reader = Reader()
data = Dataset.load_from_df(setTrain, reader)

# Generamos el set de entrenamiento 
data_train_surp = data.build_full_trainset()

# Definimos el modelo que vamos a usar 
svd = SVD()

# Entrenamos el modelo
svd.fit(data_train_surp)


# ------------------------------------Recomendacion segun datos del usuario---------------------------------------------

user_id = int(input('Dame el Id de un usuario, por favor: '))   # Solicitamos un Id de usuario  
content_id = input('Dame el Id de la pelicula: ')               # Solicitamos Un Id de una pelicula
gender = movieGender(content_id)                                # Obtenemos los generos de la pelicula que el usuario digito

a = svd.predict(uid = user_id, iid = gender)    # Hacemos la prediccion en el rango de 1 a 5 y la guardamos en una variable 
title = []      #Creamos una variable para guardar el nombre de la pelicula que el usuario digito 

# Creamos un ciclo for para obtener el titulo de la pelicula que el usuario digito
for i in range(0, len(totalMovies)):
    if totalMovies.Id.loc[i] == content_id:
        title = totalMovies.title.loc[i]
        break

porcentage = round((a[3] * 100) / 5, 1)     # Se crea una variable que almacena que tan probable es que al usuario le guste la pelicula/serie

# Hacemos la respectiva recomendacion al usuario, en el cual, si el modelo predijo una puntuacion superio a 4.0, es una pelicula recomendada, de lo contrario, no es recomendada
if a[3] > 4.0:
    print(f'hay un {porcentage}% de que al usuraio "{user_id}" le guste la pelicula/serie')
    print(f'Por ende, SI se recomienda que el usua  rio "{user_id}" vea "{title}".')
else:
    print(f'hay un {porcentage}% de que al usuraio "{user_id}" le guste la pelicula/serie')
    print(f'Por ende, NO se recomienda que el usuario "{user_id}" vea "{title}".')