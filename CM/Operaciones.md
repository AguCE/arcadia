# Cuadro de operaciones

Este es un ejemplo de un cuadro de mando orientado a los KPI del área de operaciones realizado con PowerBI. Búsca ser una herramienta de fácil utilización por parte de los interlocutores, por ello se ha definido su navegación en 3 niveles de granularidad. 
Respecto al modelo de datos, indicar que es bastante simple. Está compuesto por una tabla de hechos, y algunas tablas de dimensiones. Concretamente es un excel que está en Sharepoint, pero al igual podría ser una tabla de CDS (Common Data Service), una base de datos operacional on un Datalake.

La tabla de hechos contiene información sobre las tareas y las características asociadas: trabajador asignado, proyecto, codigo de la tarea, descripción, fechas planificadas, fechas reales, % de avance, horas acumuladas.... La idea era utilizar un modelo de registros y atributos, simple, común a la mayoria de las aplicaciones de gestión de proyectos o  archivos excel tan habituales en pequeñas empresas. 

La finalidad 

## Nivel 1: Visión General
![CMJP_1](https://user-images.githubusercontent.com/63968211/110802861-e2f30680-827e-11eb-8163-fe00419be64a.jpg)



## Nivel 2: Detalle de JP
![CMJP_3](https://user-images.githubusercontent.com/63968211/110803511-8e9c5680-827f-11eb-92c6-ee2f25ea0812.jpg)


## Nivel 3: Detalle de Proyecto
![CMJP_5](https://user-images.githubusercontent.com/63968211/110803589-a1169000-827f-11eb-8909-1f98646c46d9.jpg)
