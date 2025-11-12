from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Material(models.Model):
    UNIT_CHOICES = [
        ('un', 'Unidad'),
        ('kg', 'Kilogramo'),
        ('m', 'Metro'),
        ('lt', 'Litro'),
    ]
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES, default='un')
    stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    min_stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self): return self.name

class Tool(models.Model):
    STATUS = [('disponible','Disponible'),('asignada','Asignada'),('mantenimiento','Mantenimiento')]
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=STATUS, default='disponible')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tools')
    notes = models.TextField(blank=True)

    def __str__(self): return f"{self.code} - {self.name}"

class MaterialMovement(models.Model):
    KIND = [('ingreso','Ingreso'), ('salida','Salida')]
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    kind = models.CharField(max_length=10, choices=KIND)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): return f"{self.kind} {self.quantity} de {self.material}"

class ToolAssignment(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self): return f"{self.tool} -> {self.user}"
