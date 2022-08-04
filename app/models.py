from telnetlib import STATUS
from tkinter.messagebox import YES
from django.contrib.auth import get_user_model
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    STATUS = (
        ("doing", "Doing"),
        ("done", "Done"),
    )   
    done = models.CharField(
        max_length=5,
        choices=STATUS,        
    )
     
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.titulo)
