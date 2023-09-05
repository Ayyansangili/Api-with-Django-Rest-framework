from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    firstname = models.CharField(db_index=True,max_length=255,)
    lastname = models.CharField(db_index=True,max_length=255,null=True)
    email = models.EmailField(db_index=True, unique=True,max_length=255,)
    roles = models.CharField(db_index=True,max_length=255,)
    password = models.CharField(db_index=True,max_length=255,)

    def __str__(self):
        return self.username
    
    
    
    
    
class CollectionQuery(models.Model):
    key = models.CharField(max_length=50, unique=True)
    query = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
    