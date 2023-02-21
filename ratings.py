import pandas as pd
import numpy as np

# Se cargan los sets de datos necesarios 
rating1 = pd.read_csv('Datasets/NormalDataSet/ratings/1.csv')
rating2 = pd.read_csv('Datasets/NormalDataSet/ratings/2.csv')
rating3 = pd.read_csv('Datasets/NormalDataSet/ratings/3.csv')
rating4 = pd.read_csv('Datasets/NormalDataSet/ratings/4.csv')
rating5 = pd.read_csv('Datasets/NormalDataSet/ratings/5.csv')
rating6 = pd.read_csv('Datasets/NormalDataSet/ratings/6.csv')
rating7 = pd.read_csv('Datasets/NormalDataSet/ratings/7.csv')
rating8 = pd.read_csv('Datasets/NormalDataSet/ratings/8.csv')

# Se unen todos los sets de datos de la puntuacion de los usuarios
totalRatings = pd.concat([rating1, rating2, rating3, rating4, rating5, rating6, rating7, rating8])

# Se crea un nuevo set de datos, con el promedio de puntuacion de todos los usuarios por pelicula
scoreMovies = totalRatings.groupby(['movieId']).agg({'rating':np.mean})

# Creamos los archivos 'CSV' donde se almacena el score de las peliculas y el total de puntuaciones de personas
totalRatings.to_parquet('Datasets/TransformedDataSet/Ratings/totalRatings.parquet', index = False)
scoreMovies.to_csv('Datasets/TransformedDataSet/Ratings/scoreMovies.csv')