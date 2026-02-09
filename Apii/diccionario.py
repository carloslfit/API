class datos_diccionario:
    def __init__(self):
        self.datos_diccionario={"10932783976":{"nombre":"kevin", "apellido":"sanchez","maquina":("maquina1",
        "maquina2","maquina3")}}

    def longitud_diccionario(self):
        longitud= len(self,datos_diccionario)
        return longitud
    
    def limpiar_diccionario(self):
        limpiar=self.datos_diccionario.clear()
        self.datos_diccionario=limpiar
        
    def copiar_diccionario(self):
        copiar=self.datos_diccionario.copy()
        return copiar
    
    def sacar_elementos(self):
        sacar=self.datos_diccionario.items()
        return sacar
    
    def devolver_llaves(self):
        devolver=self.datos_diccionario.keys()
        return devolver
    
    def sacar_valores(self):
        dato_valores=self.datos_diccionario.values()
        return dato_valores
    
    def eliminar_info(self):
        eliminar=self.datos_diccionario.pop()
        return eliminar
    
    def eliminar_elemento(self):
        eliminar = self.datos_diccionario.popitem()
        return eliminar
    
    def actualizar_info(self,nuevo_diccionario):
        self.datos_diccionario.update(nuevo_diccionario)
        
    def imprimir_info(self):
        for clave in self.datos_diccionario.keys():
            print(f"dato info:{self.datos_diccionario[clave]}")
            