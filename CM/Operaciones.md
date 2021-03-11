# Cuadro de operaciones





Este es un ejemplo de un **cuadro de mando orientado a los KPI del área de operaciones** realizado con **PowerBI**. Búsca ser una herramienta de fácil utilización por parte de los interlocutores, por ello se ha definido su navegación en 3 niveles de granularidad. 
Respecto al modelo de datos, indicar que es bastante simple. Está compuesto por una tabla de hechos, y algunas tablas de dimensiones. Concretamente es un excel que está en Sharepoint, pero al igual podría ser una tabla de CDS (Common Data Service), una base de datos operacional on un Datalake.

La tabla de hechos contiene información sobre las tareas y las características asociadas: trabajador asignado, proyecto, codigo de la tarea, descripción, fechas planificadas, fechas reales, % de avance, horas acumuladas.... La idea era utilizar un modelo de registros y atributos, simple, común a la mayoria de las aplicaciones de gestión de proyectos o  archivos excel tan habituales en pequeñas empresas. 

**Finalidad:**
* Normalizar, digitalizar, y automatizar el cálculo de indicadores de la operación. Es decir, desacoplar esta tarea de los usuarios que pueden ser considereados como responsables del proceso. Evidentemente esto genera como beneficio ahorro de tiempos, disminución de errores de cálculo...
* Permitir la navegación hacia el detalle (Drill Down) para que el usuario pueda decidir a que nivel quiere mantenerse

## Nivel 1: Visión General
Esta pantalla inicial es por la cual se comienza la navegación en el cuadro, y su enfoque es ver la totalidad de la cartetara de proyectos y mostrar indicadores a nivel global.
![CMJP_1](https://user-images.githubusercontent.com/63968211/110802861-e2f30680-827e-11eb-8163-fe00419be64a.jpg)](https://www.youtube.com/watch?v=DSZq8_tGM6M "CMO-PB")
)

En este nivel a excepción de los nombre de los jefe de proyecto, su fotografía o los nombres de los proyectos, el resto son medidas calculada en PowerBI (conteos, agrupaciones, porcentajes o algunas más complejas como la estimación del tiempo para acabar el proyecto).

Está dividido en tres secciones: **indicadores numéricos; gráficas de evolución, y tablas**.
* Dentro de los **indicadores númericos**: tenemos el contejo del numero de proyectos en ejecución, el estado de las tareas desde distintas perspectivas (total de tareas, tareas cerrradas, abiertas, no empezadas, retrasadas y no retrasadas); y por último los porcentajes de avance. Son  dos  indicadores, por un lado el porcentaje de avance declarado global y por otro lado el porcentaje de avance consumido real.
* El **%Avande Declarado** es calculado de manera ponderada, a través los avances registrados en cada una de las tareas por el trabajador que las tienen asignada.  En cambio el **%Avance consumido** es un calculo a partir de las horas declaradas y las horas planificadas. Por lo tanto si "%Avance consumido > Avande Declarado" se está consumiendo más recursos (horas hombre) de lo que se planificó.

![CMJP_1 3](https://user-images.githubusercontent.com/63968211/110811827-57ca3e80-8287-11eb-830e-1dbdfa209bd1.jpg)

* La gráficas de evolución vienen a complementar a los *% de Avance*. Es el mimso indicador pero cambiando de variable una está espresada en terminos monetarios (Euros) y la otra en tiempo.  El valor mínimo del gráfico muestra el valor teórico (el tiempo o los euros que deberiamos llevar consumidos) el valor central que es equivalente al área azul, es la cantidad que llevamos consumida de la magnitud. El número en color dorado representado también por una línea dorada es el valor planificado; y el máximo es la estimación calculada de lo que vamos a necesitar para ejecutar  el resto de las tareas que tenemos en el backlog. Es decir, el máximo de la gráfica nos indica el importe de tiempo o económico al que vamos a llegar si seguimos ejecutando a este ritmo.



## Nivel 2: Detalle de JP
![CMJP_3](https://user-images.githubusercontent.com/63968211/110803511-8e9c5680-827f-11eb-92c6-ee2f25ea0812.jpg)


## Nivel 3: Detalle de Proyecto
![CMJP_5](https://user-images.githubusercontent.com/63968211/110803589-a1169000-827f-11eb-8909-1f98646c46d9.jpg)
