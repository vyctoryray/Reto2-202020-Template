"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model as m
import csv
from DISClib.ADT import list as lt
from DISClib.DataStructures import liststructure as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
def loadlst (file):
    lst = m.loadCSVFile(file,m.compareRecordIds) 
    first=lt.firstElement(lst)
    last=lt.lastElement(lst)
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    print ("Primera película:\n"+ " "*18 + "Título: " + first["original_title"]+ "\n"+ " "*18 + 
    "Fecha de estreno: "+ first["release_date"]+"\n"+ " "*18 + "Promedio de votación: "+ first["vote_average"]+
    "\n"+ " "*18 + "Número de votos: " +first["vote_count"]+"\n"+ " "*18 + "Idioma: "+ first["original_language"])
    print ("última película:\n"+ " "*18 + "Título: " + last["original_title"]+ "\n"+ " "*18 + 
    "Fecha de estreno: "+ last["release_date"]+"\n"+ " "*18 + "Promedio de votación: "+ last["vote_average"]+
    "\n"+ " "*18 + "Número de votos: " + last["vote_count"]+"\n"+ " "*18 + "Idioma: "+ last["original_language"])
    return lst

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________




# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
