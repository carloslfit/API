from base_datos_lista_empleados import BD_lista_empleados
from empleado_modelo import empleado_modelo
from diccionario import datos_diccionario

obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_valores()
print(info)

nuevo_diccionario = {"109467678098": {"nombre": "juan","apellido":
"perez","maquina":{"maquina pinturas", "maquina hidraulica"}}}

obj_diccionario.actualizar_info(nuevo_diccionario)
obj_diccionario.imprimir_info()