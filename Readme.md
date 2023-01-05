# API REST con Django y Django REST Framework

Esta es una api que fue diseñada para usar sqlite3 en desarrollo y postgres en producción. Diseñada para desplegarse en https://render.com/ como parte de pruebas de tecnologías y lenguajes

# Requerimientos

- Python 3
- Navegador web
- Cliente HTTP (Postman o thunderclient para Vscode)

## Comandos

Correr el servidor

```shell
python manage.py runserver
```

## Consultas

Consultas GET

http://localhost:8000/api/projects/

http://localhost:8000/api/projects/:id

Consultas POST (enviado por el body en un JSON)

http://localhost:8000/api/projects/

Consultas PATCH (Es similar a una consulta UPDATE solo que se optimiza, requiere de un JSON enviado por el body)

http://localhost:8000/api/projects/:id

Consultas DELETE (requiere solo el ID a eliminar)

http://localhost:8000/api/projects/:id