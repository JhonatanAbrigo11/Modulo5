from libro import Libro

libro1 = Libro('Cien años de soledad', 'Gabriel Garicia Marquez',417)
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", 96)

print(libro1.mostrarInfo())
print(libro2.mostrarInfo())

print('¿Es grande? ',Libro.es_grande(libro1.paginas))
print('¿Es grande? ',Libro.es_grande(libro2.paginas))

print('Total libros ',Libro.cantidad_Libro())
