from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactForm(models.Model):
    user = models.ForeignKey(User, related_name='contact_forms', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return f'{self.full_name}, {self.email}'