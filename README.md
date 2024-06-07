# Ejemplo API Rest (FastApi) con Operaciones CRUD

## Crear y activar el Entorno Virtual de Python:

```
$ python -m venv ./.venv
$ source ./.venv/Scripts/activate
```

## instalar paquetes:
```
$ pip install -r requirements.txt
```

## crear y iniciar contenedor de base de datos:
```
$ docker compose up -d
```
Nota (se debe crear la base de datos "fastapidb" a mano)

En este proyecto la base de datos esta seteada para crearse automaticamente al arranque, pero sin uso de migraciones incrementales. cambios en el modelo requiere actualizacion manual, o reseteo de la base de datos

## Iniciar Api (Sin Debug)
```
$ fastapi dev main.py
```

## Iniciar Api (Con Debug)
Presionar F5

## Control de calidad del codigo (Linting)

```
$ pylint src
$ pylint main.py
```