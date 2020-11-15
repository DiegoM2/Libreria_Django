from django.db import models

# Create your models here.

class Autor(models.Model):
    Autor_ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    PaisOrigen = models.CharField(max_length=30)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino')) #Opciones para el sexo de los autores. 
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='F')

    def __str__(self):
        return "{0}".format(self.Nombre) 
    
class Idioma(models.Model): #tabla de idiomas de los libros para no tener que re-escribir los idiomas. 
    Idioma_ID = models.AutoField(primary_key=True)
    Idioma = models.CharField(max_length=25)

    def __str__(self):
        return self.Idioma
    
class Genero(models.Model): #Lo mismo que más arriba, pero con genero de libro. 
    Genero_ID = models.AutoField(primary_key=True)
    Genero = models.CharField(max_length=100)

    def __str__(self):
        return self.Genero 

class Libro(models.Model):
    Libro_ID = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100)
    Autor = models.ForeignKey(Autor, null=False, on_delete=models.PROTECT)
    Precio = models.IntegerField(default=0)
    Cantidad_Disponible = models.IntegerField(default=0)
    Idioma = models.ForeignKey(Idioma, null=True, on_delete=models.SET_NULL)
    Genero = models.ForeignKey(Genero, null=False,on_delete=models.PROTECT, default=1)
    Sinopsis = models.CharField(max_length=2000, null=True, default="Sinópsis no disponible actualmente")
    RutaImg = models.CharField(max_length=250, null=True)

    def __str__(self):
        return '{0}  (${1}), cantidad en bodega: {2}'.format(self.Titulo, self.Precio, self.Cantidad_Disponible)

class Venta(models.Model):
    Venta_ID = models.AutoField(primary_key=True)
    Rut = models.CharField(max_length=9)
    Nombre = models.CharField(max_length=100)
    ApellidoPaterno = models.CharField(max_length=100)
    ApellidoMaterno = models.CharField(max_length=100)
    Fecha = models.DateTimeField(auto_now_add=True)
    Libro_ID = models.ForeignKey(Libro, null=False, on_delete=models.PROTECT)
    Cantidad_Venta = models.IntegerField(default=0) 

    def __str__(self):
        txt = "({0}) {1} {2} {3} (rut: {4}) compró {5} copia(s) del libro: {6} "
        return txt.format(self.Fecha, self.Nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.Rut, self.Cantidad_Venta, self.Libro_ID)
