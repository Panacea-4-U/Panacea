from django.db import models

# Create your models here.
class TempDb(models.Model):   
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ph_no = models.CharField(max_length=15)
    class Meta:
        db_table = "tempdb"