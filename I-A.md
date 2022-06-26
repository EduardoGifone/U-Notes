# INTELIGENCIA ARTIFICIAL

*** 

## INTRODUCCION

#### Que ciencias hay?

* Facticas
    * Naturaleza, Universo
* Formales
    * Ideas, Creatividad, Imaginacion

#### Que es inteligencia?

* Capacidad
    * Entender
    * Resolver problemas
    * Comprender
    * Adaptarse

#### Que es el test de Turing?

* Alan turing
* Distinguir entre una maquina y un humano cual es cual
* Se evalua la capacidad de la maquina de responder como lo haria un humano

#### Hitos de la IA

| Año | Hito |
| - | - |
| 1950 | Maquinas inteligentes |
| 1956 | Nacimiento de la IA |
| 70's | Invierno de la IA |
| 91's - presente | Impulso de la IA |

#### Que clasificaciones hay?

* Informales
    * Debil
    * Fuerte
* Formales
    * Simbolico
    * Sub-Simbolico

#### Algoritmos en la IA

* De busqueda
* Basado en probabilidades
* Basado en logica

#### Taxonomia de la IA

* Machine Learning
* Natural Language Processing
* Speech 
* Expert Systems
* Planning, Scheduling & Optimization
* Robotics
* Vision

#### Estructura

* IA
    * Machine Learning
        * Deep Learning

#### Machine Learning 

* Crear modelo matematico para que aprenda por si mismo
* Algoritmos para identificar patrones
* Crear modelo de predicciones
* Mas info, mejores predicciones

##### Areas

* Aprendizaje no supervisado
* Aprendizaje supervisado
* Aprendizaje reforzado

#### Natural language processing

* Formulacion y modelizacion matematica
* Comunicacion entre personas maquinas
* Usando lenguaje natural (es, en)

#### Speech 

* Mas importante en el procesamiento de seniales digitales
* Traduccion y reconocimiento de voz

#### Expert Systems

* Programas 
* Reproducen la actuacion de uno o varios expertos
* Distintos campos

#### Planning, scheduling & optimization

* Produccion de planes
* Ejecucion de un robot u otro agente

#### Robotics

* Creacion de aparatos que sustituyen a personas en tareas
* Utilizan sensores para reconoces su entorno
* Motores para realizar acciones fisicas

#### Computacional vision

* Reconocimiento de imagenes

#### La IA se sustenta de:

* Filosofia
* Matematicas 
* Economia
* Neurociencia
* Psicologia
* Ingenieria computacional
* Teoria de control y cibernetica
* Linguistica

#### Cuarta revolucion industrial

* Combinar sistemad digitales y fisicoes
* Mejorar calidad de vida del humano
* Uso de:
    * Herramientas digitales
    * **IA**
    * Analisis de datos

## AGENTES INTELIGENTES

### Conceptos generales

#### Que es un agente?

* Percibe su entorno con sensores
* Actua mediante efectores

##### Puede ser: 

* Humano
* Robot
* Agente de Software

#### Percepcion

* Percepcion
    * Recibir informacion del entorno
* Secuencia de percepciones
    * Historial de datos percibidos en un tiempo
    * Guardados en una memoria
* Las acciones dependen de la secuencia de percepciones 

#### Funcion de agente

* Elegir accion dependiendo de la secuenca de percepciones

#### Medidas de rendimiento 

* Perfeccion
    * Sabe lo que hace y actua de la mejor manera
    * Maximo rendimiento
    * En el mundo real es imposible
* Racionalidad
    * Supuestamente maximiza el rendimiento

#### Aprendizaje

* Aprender y maximizar su conocimiento (memoria)

* Exploracion
    * Recoleccion de informacion 
    * Memorizar cada caso posible

#### Autonomia

* Aprender todo lo que pueda
* Si no sabe nada, actua de forma aleatoria
* Dotarlo de:
    * Conocimiento inicial
    * Capacidad de explorar
    * Capacidad de aprender

#### Incerteza

* Limite de sensores
* Ignorancia
* Naturaleza estocastica

### El entorno

#### Ambientes utilizados

* Total o parcialmente observables (accesibilidad)
* Deterministico o estocastico (no determinista)
* Variables discretas o continuas (influencia de datos)
* Estaticos, dinamicos o semidinamicos (influencia del tiempo)
* Episodicos o secuenciales
* Conocido o desconocido 
* Agente unico o multiagente

#### Complejidad del entorno 

|Menos complejo|Mas Complejo|
|-|-|
|Totalmente observable|Parcialmente observable|
|Determinista|Estocastico|
|Episodico|Secuencial|
|Estatico|Dinamico|
|Discreto|Continuo|
|Conocido|Desconocido|
|Agente Individual |Multiagente|

#### Tipos de agentes

* Reactivos
    * Simples
    * En modelos
* Que planifican
    * Basados en objetivos
    * Basados en utilidad
* Que aprenden

#### Agentes Reactivos

* Estimulo - Respuesta
* Sin representacion explicita del entorno
* No le importa el pasado y futuro
* No considera las consecuencias de sus actos

##### Agentes Reactivos simples

* Seleccionan sus acciones con respecto a las  percepciones actuales
* Simples pero limitados
* Desicion correcta solo si la percepcion actual esta en un entorno totalmente observable

##### Agentes basados en modelos

* Almacena los datos observados
* Estado interno (mundo actual)
* Modelo del mundo (Como funciona el mundo)

#### Agentes que planifican

* Actuan dependiendo a su entorno
* Piensan en las consecuencias
* Realiza simulaciones

##### Agentes basados en objetivos

* Tiene un estado interno y modelo del mundo
* Escoge la mejor accion para llegar a su objetivo

##### Agentes basados en utilidad

* Si tiene varias opciones, compara estas
* Escoge la mas util
* Incertidumbre
    * Utilidad esperada
    * Suma ponderada de las utilidades de cada resultado segun la probabilidad de ocurrencia

#### Agentes que aprenden

* Aprenden dependiendo de:
    * Percepciones
    * Consecuencias
* Se compone de 4 elementos: 
    * Elemento de actuacion
    * Elemento de aprendizaje
    * Critica
    * Generador de problemas

### SOLUCION DE PROBLEMAS MEDIANTE BUSQUEDA
