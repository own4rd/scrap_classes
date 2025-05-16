from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)

    estado_1 = models.CharField(max_length=50, default='Alagoas')
    estado_2 = models.CharField(max_length=50, default='Alagoas')
    categoria = models.CharField(max_length=50, default='Antiguidades')
    cidade = models.CharField(max_length=50, default='Maceió')
    bairro = models.CharField(max_length=50, default='Santos Dumont')

    location = models.CharField(max_length=100, default='São Paulo, SP')
    pay_online = models.BooleanField(default=False)
    installment_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title
