# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash
from django.db import models
from django.contrib.auth.models import User

class Pic(models.Model):
    Name = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        ordering  = ['Name']