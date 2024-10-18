from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Repository(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class File(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    content = models.TextField()  
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):    
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, default='open') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
class Collaborator(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50) 


    def __str__(self):
        return f"{self.user.username} - {self.repository.name}"    

