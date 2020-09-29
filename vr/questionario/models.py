from django.db import models


CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
]


class Questionario(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    q1 = models.CharField(max_length=20, choices = CHOICES)
    q2 = models.CharField(max_length=20, choices = CHOICES)
