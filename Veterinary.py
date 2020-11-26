import os
from owlready2 import *

cwd = os.getcwd()

onto_path.append(cwd + "\owl\\")
onto = get_ontology("TratamientoRDF.owl")
onto.load()

def describeEntity(obj):
    print("\nEntidad cuya clase padre es:\n")
    print(obj.is_a)
    print("\nClasses padre (ancestras):\n")
    print(list(obj.ancestors()))
    print("\nClasses hijas (descendientes):\n")
    print(list(obj.descendants()))
    print("\nInstancias:\n")
    print(list(obj.instances()))
    
def describeIndividual(obj):
    print("\nEs un individuo de la clase: ")
    print(obj.is_a)
    print("\nNombre: ")
    print(obj.name)
    print("\nPropiedades: ")
    for prop in obj.get_properties():
        for value in prop[obj]:
            print(".%s == %s" % (prop.python_name, value))

def getOntologyObjectByName(namespace, name):
    return onto.search_one(iri="*/" + namespace + "#" + name)


###Creación dinámica de individuos

moquillo = getOntologyObjectByName("enfermedad", "Moquillo")
moquillo.esGrave = [True]

canela = getOntologyObjectByName("Mascota", "Perro")("Canela")
canela.puedeEnfermar = [moquillo]

limpiezaNasal = getOntologyObjectByName("tratamiento", "NoInvasivo")("LimpiezaNasal")
limpiezaNasal.valorTratamiento = [120000]

angelaVeterinaria = getOntologyObjectByName("oficio", "Veterinaria")("AngelaVeterinaria")
angelaVeterinaria.diagnostica = [canela]
angelaVeterinaria.realizaTratamiento = [limpiezaNasal]

marco = getOntologyObjectByName("person", "Humano")("Marco")
marco.tieneMascota = [canela]


###Descripción de toda la ontología a nivel general

print("\nBienvenido!. A continuación se presentarán las clases, individuos, propiedades de objeto y propiedades de datos de toda la ontología:\n")

print("\nClasses:\n")
print(list(onto.classes()))
print("\nIndividuals:\n")
print(list(onto.individuals()))
print("\nObject Properties:\n")
print(list(onto.object_properties()))
print("\nData Properties:\n")
print(list(onto.data_properties()))


###Parte del código que sirve para describir una entidad o un individuo a demanda 
while input("\n¿Desea describir un entidad o individuo de la Ontología? (s/n) para continuar ").lower() == "s":
    print("\n")
    namespace = input("Digite el namespace de la entidad o individuo que desee describir: ")
    objectName = input("Digite el nombre de la entidad o individuo que desee describir: ")

    searchedObject = getOntologyObjectByName(namespace, objectName)

    if searchedObject is None:
        print("\nNot Found...\n")
    else:
        if str(type(searchedObject)) == "<class 'owlready2.entity.ThingClass'>":
            describeEntity(searchedObject)
        else:
            describeIndividual(searchedObject)

print("\nA continuación, se visualizan los individuos creados dinámicamente antes de ejecutar las reglas de SWRL:\n")
describeIndividual(canela)
describeIndividual(marco)

print("\n")

###Ejecución de reglas SWRL sin tener nada de logíca de las mismas en el código de la aplicación		
sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

print("\nA continuación, se visualizan los individuos creados dinámicamente después de ejecutar las reglas:\n")
describeIndividual(canela)
describeIndividual(marco)