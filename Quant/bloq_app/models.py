from django.db import models

class SingletonManager(models.Manager):
    def create(self, **kwargs):
        # Check if there is an existing record
        existing_record = self.model.objects.first()
        if existing_record:
            # Delete the existing record
            existing_record.delete()
        # Create the new record
        return super().create(**kwargs)

# Create your models here.
class units_model(models.Model):
    UNIT_CHOICES = [
        ('mm', 'Millimeter'),
        ('inch', 'Inch'),   
        ('m', 'Meter'),
        ('ft', 'Foot'),
        ('cm', 'Centimeter'),
    ]
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    objects = SingletonManager()

    def __str__(self):
        return self.unit

class block_model(models.Model):
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    length = models.IntegerField(blank=False)
    layer = models.CharField(max_length=100, blank=False)
    # mortar = models.IntegerField(blank=False)

    def __str__(self):
        return f'W-{self.width} H-{self.height} L-{self.length} Layer-{self.layer}'
    
class door_model(models.Model):
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'W-{self.width} H-{self.height} Q-{self.quantity}'
    
class window_model(models.Model):
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'W-{self.width} H-{self.height} Q-{self.quantity}'
    
class opening_model(models.Model):
    area = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f'A-{self.area} Q-{self.quantity}'