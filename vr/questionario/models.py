from django.db import models


class Questionario(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
            db_table ='questionario'
            verbose_name ='questionario'
            verbose_name_plural ='questionari'
    def __str__(self):
        return self.name


class Domanda(models.Model):

    chiave= models.CharField(max_length=6)
    testo = models.CharField(max_length=256)

    class Meta:
            db_table ='domanda'
            verbose_name ='domanda'
            verbose_name_plural ='domande'
    def __str__(self):
        return self.chiave
