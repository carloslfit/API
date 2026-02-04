#crear clase
class Base_datos_empleado:
    #crear constructor
    def __init__(self):
      #este es el array
      self.Api_datos = []
    #crear metodos  
    def agregar_empleado(self, obj_nuevo_empleado):
        self.Api_datos.append(obj_nuevo_empleado)
        return True
    
    def guardar_varios_empleados(self,varios_obj):
        self.Api_datos.extend(varios_obj)
        
    
    def imprimir_info(self):
        for i in range(len(self.Api_datos)):
            print (self.Api_datos[i].ver_info_empleado())
        #este para imprimir unos en especifico
        #print("xxxx: " , self.Api_datos)
        #print("aaaa: " , self.Api_datos[0].get_nombre_empleado())
        
