

class Libro : 
    total = 0
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas =  paginas
        Libro.total += 1
        
    def mostrarInfo (self):
        return f'TITULO: {self.titulo} \nAUTOR: {self.autor} \nPAGINAS: {self.paginas} \n'
    
    @staticmethod
    def es_grande (paginas):
        if paginas > 300 : 
            return True
        else: 
            return False
    
    @classmethod
    def cantidad_Libro(cls):
        return cls.total
        
    
    pass