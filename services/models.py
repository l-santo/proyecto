from django.db import models

 

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image1 = models.ImageField(verbose_name="Imagen 1", upload_to="services")
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to="services")
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

 

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

 

    def str(self):
        return self.title



