from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Default Name")
    manufacturer = models.CharField(max_length=100, default="Default Manufacturer")
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.URLField(default='https://img.icons8.com/?size=32&id=PXS9WdRlqCPq&format=png')

    def __str__(self):
        return self.name