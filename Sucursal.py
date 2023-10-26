class Sucursal:
    def __init__(self, id: int, registro: List[Viaje]):
        self.id = id
        self.registro = registro
    
    def crear_viaje(self):
        print("Se realiza crear viaje")
        
    def modificar_viaje(self):
        print("Se realiza modificar viaje")
        
    def eliminar_viaje(self):
        print("Se realiza eliminar viaje")
        
    def ver_estadisticas(self):
        print("Se realiza ver estadísticas")