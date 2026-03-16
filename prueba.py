from prefect import flow, task
import requests

@task
def obtener_posts():
    url = "https://jsonplaceholder.cypress.io/posts"
    respuesta = requests.get(url)
    return respuesta.json()

@task
def mostrar_posts(posts):
    print("Primeros 5 posts:")
    for post in posts[:5]:
        print(post["title"])

@flow
def flujo_api():
    datos = obtener_posts()
    mostrar_posts(datos)

flujo_api()