import pandas as pd

# Cargamos los sets de datos necesarios
amazonDF = pd.read_csv('Datasets/NormalDataSet/amazon_prime_titles.csv')
disneyDF = pd.read_csv('Datasets/NormalDataSet/disney_plus_titles.csv')
huluDF = pd.read_csv('Datasets/NormalDataSet/hulu_titles.csv')
netflixDF = pd.read_csv('Datasets/NormalDataSet/netflix_titles.csv')


# Creamos una funcion para crear una columna nueva y agregar la inicial de la plataforma en la columna 'showId'
def columID(df, initial):

    # Se crea una lista para crear la nueva columna
    id = []

    # Realizamos un ciclo for para agregar la inicial a la columna 'showId'
    for i in df['show_id']:
        id.append(f'{initial}{i}')  # Agregamos los ID nuevos en la columna anteriormente creada

    df.insert(0,'Id', id, True)     # Insertamos la nueva columna en el set de datos


# Creamos una funcion para llenar los espacion vacios en la columna rating y agregar una 'g'
def ratingG(df):
    df['rating'].fillna('G', inplace = True)


# Creamos una funcion para eliminar los espacios a la izquierda de la columna 'date_added' y poder manipular dicha columna
def dropSpace(df):
    for i in range(0, len(df.date_added)):
        if type(df.date_added.loc[i]) != float:
            df['date_added'].loc[i] = df['date_added'].loc[i].lstrip()

    return df


# Creamos una funcion para convertir todas las columnas de tipo 'str' en minusculas
def lowerCase(df):
    df["type"] = df["type"].str.lower()
    df["title"] = df["title"].str.lower()
    df["director"] = df["director"].str.lower()
    df["cast"] = df["cast"].str.lower()
    df["country"] = df["country"].str.lower()
    df["rating"] = df["rating"].str.lower()
    df["duration"] = df["duration"].str.lower()
    df["listed_in"] = df["listed_in"].str.lower()
    df["description"] = df["description"].str.lower()

    return df


# Paso 1: Creo el campo 'Id'

columID(amazonDF,'a')
columID(disneyDF,'d')
columID(huluDF,'h')
columID(netflixDF,'n')


# Paso 2: Remplazo los valores nulos del campo 'Rating' por 'G'

ratingG(amazonDF)
ratingG(disneyDF)
ratingG(huluDF)
ratingG(netflixDF)


# Paso 3: Cambio el tipo de formato de las fechas

amazonDF["date_added"] = pd.to_datetime(amazonDF["date_added"], format='%B %d, %Y')
disneyDF["date_added"] = pd.to_datetime(disneyDF["date_added"], format='%B %d, %Y')
huluDF["date_added"] = pd.to_datetime(huluDF["date_added"], format='%B %d, %Y')

# En el caso del set de datos de netflix, hay campos que toco eliminar espacios en blanco para poder hacer cambio de formato
netflixDF = dropSpace(netflixDF)
netflixDF["date_added"] = pd.to_datetime(netflixDF["date_added"], format='%B %d, %Y')


# Paso 4: Se modifican los campos que son cadenas de texto y se colocan todas en minuscula si excepcion

amazonDF = lowerCase(amazonDF)
netflixDF = lowerCase(netflixDF)
disneyDF = lowerCase(disneyDF)

# En el caso de 'HuluDF' en el campo 'cast', se modifica el tipo de dato a 'str' ya que se encuentra en 'float64'
huluDF['cast'] = huluDF['cast'].astype('str')
huluDF = lowerCase(huluDF)


# Paso 5: Divido la columna "duration" en 'duration_int' y 'duration_type' 

amazonDF[['duration_int', 'duration_type']] = amazonDF['duration'].str.extract('(\d+)\s*(\w+)')
disneyDF[['duration_int', 'duration_type']] = disneyDF['duration'].str.extract('(\d+)\s*(\w+)')
huluDF[['duration_int', 'duration_type']] = huluDF['duration'].str.extract('(\d+)\s*(\w+)')
netflixDF[['duration_int', 'duration_type']] = netflixDF['duration'].str.extract('(\d+)\s*(\w+)')

    # Reemplazo "seasons" por "season": 
amazonDF["duration_type"] = amazonDF["duration_type"].str.replace("seasons", "season")
disneyDF["duration_type"] = disneyDF["duration_type"].str.replace("seasons", "season")
huluDF["duration_type"] = huluDF["duration_type"].str.replace("seasons", "season")
netflixDF["duration_type"] = netflixDF["duration_type"].str.replace("seasons", "season")


# Paso 6: unimos los sets de datos de las 4 plataformas para tener un mejor manejo de la informacion

totalMovies = pd.concat([amazonDF, disneyDF, huluDF, netflixDF])


# Paso 7: Cambiamos el tipo de variable de la columna 'duration_int', la cual esta en 'object' y pasamos a 'int64'

totalMovies['duration_int'] = totalMovies['duration_int'].astype("float")


# Paso 8: Por ultimo, generamos un archivo 'CSV' con el set de datos de todas las peliculas de las cuatro plataformas

huluDF.to_csv('Datasets/TransformedDataSet/huluTransformed.csv', index = False)
amazonDF.to_csv('Datasets/TransformedDataSet/amazonTransformed.csv', index = False)
disneyDF.to_csv('Datasets/TransformedDataSet/disneyTransformed.csv', index = False)
netflixDF.to_csv('Datasets/TransformedDataSet/netflixTransformed.csv', index = False)
totalMovies.to_csv('Datasets/TransformedDataSet/totalMovies.csv', index = False)