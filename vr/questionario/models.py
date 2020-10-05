from django.db import models




class Questionario(models.Model):


    class Meta:
            tb_table ='Questionario'
            verbose_name ='Questionario'
            verbose_name_plural ='Questionari'
            def __str__(self):
                return self.name
