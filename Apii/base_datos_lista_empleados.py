class BD_lista_empleados:
    def __init__(self):
        self.lista_bd_empleados = []

    def imprimir_listas(self):
        print(self.lista_bd_empleados)      
        for i in range(len(self.lista_bd_empleados)):
            print(self.lista_bd_empleados[i].ver_info_empleado())
            
    def guardar_empleado(self, obj_nuevo_empleado):
        self.lista_bd_empleados.append(obj_nuevo_empleado)
        
    def extenend_lista_empleados(self, nueva_lista):
        self.lista_bd_empleados.extend(nueva_lista)