 pip freeze > requirements.txt

pip install requests 

pip3 install --user django-crispy-forms

pip install django-admin-interface



sudo su postgres 
psql

create database  BasePrueba

\c baseprueba

\l
CREATE TABLE Usuario (
    Nombre varchar(30),
    Apellido varchar(10)
);

\d Usuario;

INSERT INTO Usuario (Nombre, Apellido) values ('fernando','Quezada')
