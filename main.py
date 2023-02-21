import pandas as pd
from fastapi import FastAPI
from statistics import mode # Se utilizo 'mode' para realizar la consigan 4 y obtener el actor que mas se repite

# Se crea una instancia de FastAPI
app = FastAPI(title = 'Personal_Project')

# Se cargan los data sets necesarios para relizar las consignas
totalMovies = pd.read_csv('Datasets/TransformedDataSet/totalMovies.csv')
totalRatings = pd.read_parquet('Datasets/TransformedDataSet/Ratings/totalRatings.parquet')
scoreMovies = pd.read_csv('Datasets/TransformedDataSet/Ratings/scoreMovies.csv')


#----------Carta de presentación----------

@app.get("/")
def presentacion():
    return "Proyecto Individual - Rodriguez Salcedo Juan Esteban. Gracias por testear mi api!"

@app.get("/contacto")
def contacto():
    return "Email: je_rodriguez26@hotmail.com / Github: JuanRS26"

@app.get("/menu")
def menu():
    return ("Funciones de mi API: (1) get_max_duration (2) get_score_count (3) get_count_platform (4) get_actor")


# ---------------------------------------------Consignas----------------------------------------------


# Consigna 1: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get('/maxDuration/{year}/{platform}/{duration_type}')
def get_max_duration(year: int, platform: str, duration_type: str):

    # Creamos dos variables para almacenar la pelicula y la maxima durabilidad de la misma
    max = 0
    movie = []

    # Se convierte el nombre de la plataforma y el tipo de duracion a minusculas para mejor manipulacion
    platform = platform.lower()
    duration_type = duration_type.lower()

    # creamos un filtro de la plataforma que el usuario digito para poder filtrar mejor en el dataset y tambien si el usuario digito una plataforma incorrecta
    if platform == "amazon":
        initial = "a"
    elif platform == "disney":
        initial = "d"
    elif platform == "hulu":
        initial = "h"
    elif platform == "netflix":
        initial = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix.")

    # Se hace un filtro en dado caso que el usuario haya digitado el tipo de duracion de una forma distinta pero con la misma finalidad
    if duration_type == 'temporada' or duration_type == 'season':
        duration_type = 'season'
    elif duration_type == 'minutos':
        duration_type = 'min'
    else:
        return ("Tipo de duracion incorrecta. Las opciones son: min, season o temporada")


    # Se crea un ciclo for para poder hacer los filtros correspondientes e ir comparando las peliculas con los datos ingresados por el usuario
    for i in range(0, len(totalMovies)):
        if totalMovies.release_year[i] == year:     # Primero: se hace el filtro por el anio seleccionado por el usuario
            if totalMovies.Id[i][0] == initial:     # segundo: Se filtra por la inicial de la plataforma que el usuraio digito y previamente asignamos
                if totalMovies.duration_type[i] == duration_type:   # tercero: Se filtra por el tipo de duracion que el usuraio digito
                    if totalMovies.duration_int[i] > max:           # Cuarto: Se hace la comparacion de las peliculas que pasaron los filtros y saber cual es la que mas dura
                        max = totalMovies.duration_int[i]
                        movie = totalMovies.title[i]


    # Se hace el respectivo mensaje, el cual aparecera en pantalla del usuraio con el resultado de la consulta
    return f'La pelicula con mayor duracion del {year} en la plataforma de {platform} con el tipo de duracion {duration_type} es: {movie}'



# Consigna 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
@app.get('/totalMovies/{platform}/{scored}/{year}')
def get_score_count(platform: str, scored: float, year: int):

    # Creamos la variable correspondiente para guardar las peliculas con mayor puntaje, segun el usuario
    titles = []

    # Se convierte el nombre de la plataforma y el tipo de duracion a minusculas para mejor manipulacion
    platform = platform.lower()

    # creamos un filtro de la plataforma que el usuario digito para poder filtrar mejor en el dataset y tambien si el usuario digito una plataforma incorrecta
    if platform == "amazon":
        initial = "a"
    elif platform == "disney":
        initial = "d"
    elif platform == "hulu":
        initial = "h"
    elif platform == "netflix":
        initial = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix.")

    # Se crea un ciclo for para poder hacer los filtros correspondientes con los datos ingresados por el usuario
    for i in range(0, len(totalMovies)):
        if totalMovies.Id[i][0] == initial and totalMovies.release_year[i] == year:     # Primero: Se filtran las peliculas por el año y la inicial de la plataforma 
            for j in range(0, len(scoreMovies)):
                if totalMovies.Id[i] == scoreMovies.movieId[j] and scoreMovies.rating[j] >= scored:     # Segundo: Se filtra por el id del data set de las peliculas y el dataset de el score asignado por todos los usuario y el score que asigno el usuario
                    titles.append(totalMovies.title[i])     # Tercero: Se guarda el titulo de la pelicula en la lista 
    
    # Se comprueba de que la lista no este vacia y contenga el titulo de las peliculas filtradas, en caso contrario, se muetra un mensaje diciendo que no se encontraron peliculas
    if len(titles) == 0:
        return f'No se encontraron titulos con una puntuacion mayor a {scored} en la plataforma {platform} para el año {year}'


    # Se hace el respectivo mensaje, el cual aparecera en pantalla del usuraio con el resultado de la consulta
    return f'Los titulos en la plataforma de {platform} para el año {year} con puntuacion mayor a {scored} son : {titles}'



# Consigna 3: Cantidad de películas por plataforma con filtro de PLATAFORMA.
@app.get('/moviesPlatform/{platform}')
def get_count_platform(platform: str):

    # Se crea una variable para sumar la cantidad de peliculas por plataforma
    sum = 0

    # Se convierte el nombre de la plataforma y el tipo de duracion a minusculas para mejor manipulacion
    platform = platform.lower()

    # creamos un filtro de la plataforma que el usuario digito para poder filtrar mejor en el dataset y tambien si el usuario digito una plataforma incorrecta
    if platform == "amazon":
        initial = "a"
    elif platform == "disney":
        initial = "d"
    elif platform == "hulu":
        initial = "h"
    elif platform == "netflix":
        initial = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix.")

    # Se crea un ciclo for para poder hacer los filtros correspondientes con los datos ingresados por el usuario
    for i in range(0, len(totalMovies)):
        if totalMovies.Id[i][0] == initial:     # Se filtran las peliculas segun la plataforma indicada por el usuario
            sum += 1


    # Se hace el respectivo mensaje, el cual aparecera en pantalla del usuraio con el resultado de la consulta
    return f'Hay {sum} peliculas y series en la plataforma de {platform}'


# Consigna 4: Actor que más se repite según plataforma y año.
@app.get('/actor/{platform}/{year}')
def get_actor(platform: str, year: int):
    
    # Creamos una lista vacia para almacenar todos los actores de cada pelicula 
    listActors = []

    # Se convierte el nombre de la plataforma y el tipo de duracion a minusculas para mejor manipulacion
    platform = platform.lower()

    # creamos un filtro de la plataforma que el usuario digito para poder filtrar mejor en el dataset y tambien si el usuario digito una plataforma incorrecta
    if platform == "amazon":
        initial = "a"
    elif platform == "disney":
        initial = "d"
    elif platform == "hulu":
        initial = "h"
    elif platform == "netflix":
        initial = "n"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix.")

    # Se crea un ciclo for para poder hacer los filtros correspondientes con los datos ingresados por el usuario
    for i in range(0, len(totalMovies)):
        if totalMovies.Id[i][0] == initial:     # Primero: Se filtra por la inicial de la plataforma que el usuario asigno 
            if totalMovies.release_year[i] == year:     # Segundo: Se filtra por el año que el usuario asigno
                if type(totalMovies.cast[i]) == str:    # Tercero: Se hace un filtro con el tipo de dato, ya que en el dataset no se encuantran registrados actores de algunas peliculas
                    a = totalMovies.cast[i].split(', ') # Cuarto: Se crea una variable temporal, la cual guarda el nombre de cada actor que participo en la pelicula, en una lista
                    for j in a:
                        listActors.append(j)    # Quinto: Se agrega cada nombre de los actores de cada pelicula en la lista principal


    # 'mode' es una funcion de 'statistics' la cual nos ayuda a mostrar el valor que mas se repite, en este caso, el nombre del actor que mas se repite en la lista 
    # Se hace el respectivo mensaje, el cual aparecera en pantalla del usuraio con el resultado de la consulta
    return f'{mode(listActors)} es la actriz/actor que mas se repite en la plataforma de {platform} en el año {year}'
