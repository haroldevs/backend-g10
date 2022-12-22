from camelcase import CamelCase

instancia=CamelCase()

text="hola mundo"
resultado=instancia.hump(text)
print(resultado)