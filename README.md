<<<<<<< HEAD
## Proyecto Individual - Data Engineer 
_Ingeniera: Zapata, María Belén_

> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API que se me solicitó desarrollar.

[Video explicativo](https://youtu.be/rLUn2rhO37s)

:green_circle: **MENU:** :green_circle:
* **Datasets_RAW** - _las bases de datos que recibí para trabajar._
* **pycache** - _carpeta necesaria para el funcionamiento de la api._
* **PI01_Queries.ipynb** - _notebook con pruebas de las queries._
* **PI01_Transformación de Datos.ipynb** - _paso a paso del ETL._
* **README** - _Instrucciones de uso._
* **main.py** - _el código de la API._
* **movies_completo.csv** - _el csv que se utiliza para las consultas._ 
* **requirements.txt** - _dependencias necesarias para que funcione._
 
:green_circle: **Las funciones que componen la API son:** :green_circle:

:small_blue_diamond: Conteo de palabras clave, por plataforma. <br>
:small_blue_diamond: Conteo de peliculas, por año, plataforma y puntuación. <br>
:small_blue_diamond: Segunda película mejor puntuada en la plataforma seleccionada. <br>
:small_blue_diamond: Película de mayor duración, por plataforma y por año. <br>
:small_blue_diamond: Cantidad de películas con determinada clasificación. <br>

:green_circle: **Cómo escribir cada función en el navegador:** :green_circle: 

:white_medium_small_square: https://twj1kq.deta.dev/get_word_count/{plataforma}/{keyword} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_score_count/{plataforma}/{puntaje}/{ano} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_second_score/{plataforma} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_longest/{plataforma}/{duration_type}/{ano} <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_rating_count/{rating} <br>

:green_circle: **Queries de ejemplo para probar la api** :green_circle: 

:white_medium_small_square: https://twj1kq.deta.dev/get_word_count/netflix/love <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_score_count/netflix/85/2010 <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_second_score/amazon <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_longest/netflix/min/2016 <br>
:white_medium_small_square: https://twj1kq.deta.dev/get_rating_count/18+ <br>

:warning: **Sintaxis a tener en cuenta al escribir una consulta:** :warning:<br>
:small_blue_diamond: Todo debe estar escrito en minúsculas.  <br>
:small_blue_diamond: Las plataformas que admite son: Amazon, Disney, Hulu y Netflix. <br>
:small_blue_diamond: Evite utilizar caracteres hispanos. <br>
:small_blue_diamond: En caso de la query no arroje resultados, un mensaje explicativo se imprimirá en pantalla.<br>
:small_blue_diamond: En caso de que se ingrese una plataforma inválida, un mensaje explicativo se imprimirá en pantalla. <br>

:green_circle: **Funciones extra** :green_circle: <br>
:small_blue_diamond: Función _Presentación_: `/` <br>
Simplemente invocando el link vacío, muestra el nombre y a quien pertenece la api.<br>
:small_blue_diamond: Función _menú_: `/menu` <br>
Muestra una lista de las funciones disponibles para consultar. <br>
:small_blue_diamond: Función _Contacto_: `/contacto`<br>
Muestra dos maneras de contactar conmigo, en caso de necesidad. <br>
:small_blue_diamond: Función _docs_: `/docs` <br>
Muestra el menú principal de la api, donde también se puede testear las consultas.<br>

:green_circle: **Notas finales:** :green_circle:<br>
:innocent: Muchas gracias por testear mi api! <br> 
Todo el feedback es bien recibido. :coffee:
=======
## Proyecto Individual - Data Engineer - ML 
_Juan Esteban Rodriguez S._

> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API que se me solicitó desarrollar.

[Video explicativo]()

:green_circle: **MENU:** :green_circle:
* **Datasets** - _Los sets de datos que recibí para trabajar y tambien los sets de datos transformados para su posterior manipulacion._
* **README** - _Instrucciones de uso._
* **main.py** - _El codigo de la API._
* **ratings.py** - _Paso a paso del ETL em los sets de datos de las puntuaciones de los usuarios._
* **recommendationSystem.py** - _El sistema de recomendacion de peliculas a un usuario con ML._
* **requirements.txt** - _Dependencias necesarias para que funcione._
* **transformations.py** - _Paso a paso del ETL en los sets de datos de las plataformas._
 
:green_circle: **Las funciones que componen la API son:** :green_circle:

:small_blue_diamond: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. <br>
:small_blue_diamond: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. <br>
:small_blue_diamond: Cantidad de películas por plataforma con filtro de PLATAFORMA. <br>
:small_blue_diamond: Actor que más se repite según plataforma y año. <br>

:warning: **Sintaxis a tener en cuenta al escribir una consulta:** :warning:<br>

:small_blue_diamond: Todo debe estar escrito en minúsculas.  <br>
:small_blue_diamond: Las plataformas que admite son: Amazon, Disney, Hulu y Netflix. <br>
:small_blue_diamond: Evite utilizar caracteres hispanos. <br>
:small_blue_diamond: En caso de la query no arroje resultados, un mensaje explicativo se imprimirá en pantalla.<br>
:small_blue_diamond: En caso de que se ingrese una plataforma inválida, un mensaje explicativo se imprimirá en pantalla. <br>

:green_circle: **Como usar la Api:** :green_circle:<br>

:small_blue_diamond: Primero, se debe de instalar las dependencias que se encuentran en el archivo `requirements.txt` <br>
:small_blue_diamond: Segundo, luego de instalar las dependencias, se abre la terminal en la ubicacion donde esta nuestro proyecto y ponemos el siguiente codigo `uvicorn main:app --reload` <br>
:small_blue_diamond: Tercero, despues podemos utilizar la Api de forma local entrando en `localhost:8800/` y luego poner la funcion que queremos consultar <br>

:green_circle: **Queries de ejemplo para probar la api** :green_circle: 

:white_medium_small_square: localhost:8800/maxDuration/2016/Disney/minutos <br>
:white_medium_small_square: localhost:8800/totalMovies/Netflix/3.6/2005 <br>
:white_medium_small_square: localhost:8800/moviesPlatform/Hulu <br>
:white_medium_small_square: localhost:8800/actor/Amazon/2012 <br>

:green_circle: **Funciones extra** :green_circle: <br>

:small_blue_diamond: Función _Presentación_: `/` <br>
Simplemente invocando el link vacío, muestra el nombre y a quien pertenece la api.<br>
:small_blue_diamond: Función _menú_: `/menu` <br>
Muestra una lista de las funciones disponibles para consultar. <br>
:small_blue_diamond: Función _Contacto_: `/contacto`<br>
Muestra dos maneras de contactar conmigo, en caso de necesidad. <br>


:red_circle: **Funcionamiento del sistema de recomendacion:** :red_circle: <br>

:small_blue_diamond: Ejecutamos el archivo `recommendationSystem.py` en la terminal <br>
:small_blue_diamond: Esperamos unos minutos a que el sistema cargue los datos <br>
:small_blue_diamond: El sistema luego nos pedira digitar el ID de un usuario y el ID de una pelicula <br>
  :white_medium_small_square: Ejemplo: <br>
  :white_medium_small_square: User ID: 1 <br>
  :white_medium_small_square: Movie ID: ns3830 <br>
:small_blue_diamond: El sistema nos mostrara si es recomendable que el usuraio vea la pelicula/serie basado en las puntuaciones del mismo usuario <br>

:warning: **Sintaxis a tener en cuenta al usar el sistema de recomendacion:** :warning:<br>

:small_blue_diamond: Cuando digite el ID de la pelicula, inicie con la inicial de la plataforma en minuscula <br>

:green_circle: **Notas finales:** :green_circle:<br>
Muchas gracias por testear mi Proyecto! <br> 
Todo el feedback es bien recibido. :coffee:
>>>>>>> a86b17a48e0a1a873cf296027ed592813d0223a6
