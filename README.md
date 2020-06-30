<h1 align="center">:house_with_garden: AirBnB_clone :house_with_garden:</h1>

![logo](img/hbnb.png)

## :page_with_curl: Description

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

## :computer: The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

## :warning: Requirements

- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the ```PEP 8``` style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- All your classes should have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
- All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` - and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)

## First Step

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## :file_folder: Files and Directories

- ```models``` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/- instance.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models. It contains common elements:
- attributes: ```id```, ```created_at``` and ```updated_at```
- methods: ```save()``` and ```to_json()```
- ```models/engine``` directory will contain all storage classes (using the same prototype). For the moment you will have only one: ```file_storage.py```.

![Error](img/console.png)

## :black_nib: Authors

- Adrian De La Asunción - [Github](https://github.com/AdrianDel07) , [Twitter](https://twitter.com/AdrianDeLaAsun1)
- Juliana Chois - [Github](https://github.com/julianachois) , [Twitter](https://twitter.com/julianachois)

See also the list of [contributors](https://github.com/jchois/AirBnB_clone/graphs/contributors) who participated in this project.

## :triangular_flag_on_post: Acknowledgments

- Holberton School, we would like to thank the staff and our peers for helping us in this great experience.