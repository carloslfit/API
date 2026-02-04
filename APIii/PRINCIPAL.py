from Base_datos_empleado import Base_datos_empleado
from empleado_modelo import Empleado_modelo

  
#codigo principal

#creo la base de datos de empleados
objeto_Api = Base_datos_empleado()

#creo el objeto empleado que voy a guardar
objeto_empleado = Empleado_modelo("Juan","Perez","12345678","555-1234")
objeto_empleado2= Empleado_modelo("Ana","Gomez","87654321","555-5678")
objeto_empleado3= Empleado_modelo("Luis","Martinez","11223344","555-8765")


#creo la lista para guardar masivamente
lista_nuevos_empleados =(objeto_empleado,objeto_empleado2,objeto_empleado3)
#llamo el metodo de la base de datos que guarda al objeto

objeto_Api.agregar_empleado(objeto_empleado)
objeto_Api.agregar_empleado(objeto_empleado2)
objeto_Api.agregar_empleado(objeto_empleado3)

objeto_Api.extender_varios_empleados(lista_nuevos_empleados)

#imprimo toda la lista de empleados
objeto_Api.imprimir_info()
