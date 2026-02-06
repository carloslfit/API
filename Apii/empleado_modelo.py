class Empleado:
    
     def __init__(self, nombre, apellido, telefono, cedula):
         self.nombre=nombre
         self.apellido=apellido
         self.telefono=telefono
         self.cedula=cedula
         
     def ver_info_empleado(self):
         return f" {self.cedula} {self.nombre} {self.apellido} {self.telefono}"
     
     def set_nombre(self,nuevo_nombre):
         self.nombre=nuevo_nombre
     def get_nombre(self):
         return self.nombre  
     
     def set_apellido(self,nuevo_apellido):
         self.apellido=nuevo_apellido
     def get_apellido(self):
         return self.apellido
       
     def set_telefono(self,nuevo_telefono):
         self.telefono=nuevo_telefono
     def get_telefono(self):
         return self.telefono
     
     def set_cedula(self,nueva_cedula):
         self.cedula=nueva_cedula
     def get_cedula(self):
         return self.cedula
     

        
         
         