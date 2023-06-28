# Evidencia 3


## En esta actividad creamos la BD y nos conectamos desde Python tal cual lo vimos en clases sincrónicas. Utilizamos para esto el siguiente codigo:


import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "dupe",
    database= "proyectoIntegrador"
)

print (midb)