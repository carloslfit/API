class Empleado:
    def __init__(self,codigo,nombre,apellido,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.apellido=apellido
        self.estado=estado
        
    def ver_info_maquina(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nApellido: {self.apellido}\nestado: {self.estado}"
    
    def set_codigo(self,nuevo_codigo):
        self.codigo=nuevo_codigo
    def get_codigo(self):
        return self.codigo
    
    def set_nombre(self,nuevo_nombre):
        self.nombre=nuevo_nombre
    def get_nombre(self):
        return self.nombre
     
    def set_apellido(self,nuevo_apellido):
        self.apellido=nuevo_apellido
    def get_apellido(self):
        return self.apellido
    
    def set_estado(self,nuevo_estado):
        self.estado=nuevo_estado
    def get_estado(self):
        return self.estado
    

    
    