# Introducción a Prefect
## ¿Qué es Prefect?

Prefect es una herramienta de orquestación de flujos de trabajo en Python que permite automatizar procesos o pipelines de datos. Con Prefect es posible dividir un proceso en diferentes tareas llamadas tasks y organizarlas dentro de un flujo llamado flow.

Esto ayuda a ejecutar procesos de manera ordenada, manejar errores y monitorear la ejecución de los programas. Prefect es muy utilizado en proyectos de ingeniería de datos y automatización de procesos, ya que permite controlar cómo y cuándo se ejecutan las tareas dentro de un flujo de trabajo.

## Objetivo de la práctica

El objetivo de esta práctica es aprender a utilizar Prefect para crear y ejecutar flujos de trabajo en Python, siguiendo un tutorial y posteriormente modificándolo para crear un ejemplo propio utilizando una API pública.

## Ejecución del tutorial

En la primera parte de la actividad se siguió el tutorial Getting Started with Prefect (PyData Denver) para comprender cómo funciona Prefect y cómo se crean flujos de trabajo.

Video del tutorial:
https://www.youtube.com/watch?v=FETN0iivZps

En el tutorial se aprendió a:

Instalar Prefect en Python

Crear tareas (tasks)

Crear un flujo de trabajo (flow)

Ejecutar el flujo en la computadora


## Modificación y ejemplo propio

En la segunda parte se modificó el ejemplo para trabajar con una API pública llamada JSONPlaceholder, la cual permite realizar pruebas con datos simulados.

API utilizada:
https://jsonplaceholder.cypress.io/

Se creó un flujo en Prefect que obtiene información desde la API y muestra algunos resultados.


Este flujo realiza lo siguiente:

Se conecta a la API.

Obtiene los datos de los posts.

Muestra los primeros cinco títulos en la consola.

## Conclusión

Prefect es una herramienta muy útil para automatizar procesos en Python. Permite organizar diferentes tareas dentro de un flujo de trabajo, lo que facilita la ejecución de procesos complejos y el manejo de errores. En esta práctica se aprendió cómo crear un flujo básico y cómo modificarlo para obtener información desde una API, demostrando cómo Prefect puede utilizarse para automatizar procesos de obtención y procesamiento de datos.

## Referencias

Prefect Technologies. (2025). Prefect Documentation.
https://docs.prefect.io/

PrefectHQ. (2025). Prefect workflow orchestration framework.
https://github.com/PrefectHQ/prefect

JSONPlaceholder. (2025). Fake API for testing.
https://jsonplaceholder.cypress.io/
