from base_datos_lista_empleados import BD_lista_empleados
from empleado_modelo import Empleado
obj_lista_empleado=BD_lista_empleados()

obj_empleado=Empleado("10001283999","Juan"," Perez","3224567890")
obj_empleado2=Empleado("10001283998","Maria"," Gomez","3224567891")
obj_empleado3=Empleado("10001283997","Carlos"," Rodriguez","3224567892")

obj_lista_empleado.guardar_empleado(obj_empleado2)
obj_lista_empleado.guardar_empleado(obj_empleado3)
obj_lista_empleado.guardar_empleado(obj_empleado)

nuevos_empleados=[obj_empleado,obj_empleado2,obj_empleado3]
obj_lista_empleado.extenend_lista_empleados(nuevos_empleados)

obj_lista_empleado.imprimir_listas()