# Tutorial de Django

Django es un marco web del lado del servidor back-end.

Django es gratuito, de código abierto y está escrito en Python.

Django facilita la creación de páginas web utilizando Python.

# Introducción 

## ¿Qué es Django?

Django es :
- Open Source 
- Se pueden utilizar componentes DRY
- Operaciones CRUD

## ¿Cómo funciona Django?

- MVT 


## Modelo 

En Dejango, los datos se entregan como un Mapeo Relacional de Objetos

Djnaogo, con ORM, facilita la comunicación con la base de datos, sin tener que escribir sentencias SQL complejas.

que suelen estár ubicados en un archivo llamado **models.py**
 
# Vista 

Una vista es una función o método que toma solicitudes http como argumentos, importa los modelos relevantes, descubre qué ddatos enviar a la plantilal y devuleve el resultado final.

Las vistas suelen estar ubicadas en un archivo llamado **views.py**

## Plantilla

Una plantilla es una aplicación se encuentran en una caprreta llamada **templates**.

## URL

Django también proporciona una forma de navegar por las diferentes páginas de un sitio web. 

Cuando un usuario solicita una URL, Django decide a qué vista la enviará.

Esto se hace en un archivo llamado **urls.py**

# ¿Entonce squé está pasando? 

Cuando instala Django y crea su primera aplicación web Django, y el navegador solicita la URL, esto es básicamente lo que sucede:

1. Django recibe la URL, verifica el ***url.py*** archivo y llama a la vista que coincide con la URL.
2. La vista, ubicada en ***views.py*** busca modelso relevantes.
3. Los modelso se importan desde el ***models.py*** archivo.
4. Luego, la vista envía los datos a una plantilla especificada en la ***template*** carpeta. 
5. La plantilla contiene HTML y DJango, y con los datos devuelve el contenido HTML terminado al navegador. 

Django puede hacer mucho más que esto, pero esto es básicamente lo que aprenderá en este tutorial y con los pasos básicos en una aplicación web simple hecha con DJango. 


# Hitoria de DJango

Django fue inventado por Lawrence Journal-World en 2003, para cumplir con los cortos plazos del periódo y al mismo tiempo satisfacer las demandas de los desarrolladores web experimentados. 

El lanzamiento inicial al público fue en julio de 2005. 

La última versión de Django es 4.0.3 (marzo de 2022)


# Crear un entorno virtual 

```bash
python3 -m venv djangoenviroment

```

## Activar el entorno virtual 

```bash
source djangoenviroment/bin/activate
```

## Instalar Django 

```bash
pip install Django
```

## Verificar versión de Django

```bash
django-admin --version
```


# Proyecto de creación Django

```bash
django-admin startproject my_data_club
```


## Ejecutamos el proyecto 

```bash
python manage.py runserver
```

## Creamos una aplicación 

Una aplicación tiene el significado específico en su proyecto, como una página de inicio, un formulario de contacto o una base de datos de miembros.

Le daré un nombre a mi aplicación **members**. La cual creare dentro de la carpeta ***my_data_club***. 

```bash
python manage.py startapp members
```

## Views 

Hay un ***views.py*** en su ***members*** caperta que se parece a lo siguiente: 
























