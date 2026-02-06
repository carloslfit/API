class Api_lista_maquina:
    def __init__(self):
        self.Api_maquinas = []
        
    def agregar_maquina(self, nueva_maquina):
        self.Api_maquinas.append(nueva_maquina)
        
    def agregar_varias_maquinas(self, lista_maquinas):
        self.Api_maquinas.extend(lista_maquinas)
        
    def agregar_varias_maquinas(self, varias_maquinas):
        self .Api_maquinas.extend(varias_maquinas)
        
    def mostrar_maquinas(self):
        for i in self.Api_maquinas:
            print(i)
