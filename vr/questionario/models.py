from django.db import models


class Questionario(models.Model):
    nome = name.Chardfield(max_lenght =256)

    class Meta:
            db_table ='questionario'
            verbose_name ='questionario'
            verbose_name_plural ='questionari'
        def __str__(self):
            return self.name
