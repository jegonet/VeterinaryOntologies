import os
from owlready2 import *

cwd = os.getcwd()
onto_path.append(cwd)

onto = get_ontology("Tratamiento.owl")
onto.load()

print("\nClasses:\n")
print(list(onto.classes()))
print("\nIndividuals:\n")
print(list(onto.individuals()))
print("\nObject Properties:\n")
print(list(onto.object_properties()))

class Tratamiento(Thing):
	namespace = onto

#print("\n" + Tratamiento.iri)

#class ProteinaSimple(Proteina):
#	pass

#print("\n" + ProteinaSimple.iri)
#print("\n" + str(ProteinaSimple.is_a))
print("\n" + str(Tratamiento.ancestors()))
print("\n" + str(Tratamiento.subclasses()))

pr_ind = Tratamiento("Desparacitar")

####Crear una propiedad
#with onto:
#	class contiene(ObjectProperty):
#		domain    = [onto.Virus]
#		range     = [Proteina]

#print("\n" + str(contiene.range))
#print("\n" + str(contiene.domain))
		
#import owlready2
#owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk1.8.0_161\\bin\\java.exe"


##############
#with onto:
#	sync_reasoner(infer_property_values = True)
with onto:
	sync_reasoner(infer_property_values = True)

#print(list(default_world.inconsistent_classes()))

#onto.save(file = "Virus2.owl", format = "rdfxml")