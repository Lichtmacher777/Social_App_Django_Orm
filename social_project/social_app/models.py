from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core import validators
# Create your models here.

bad_word = ['cat','dog','fish']

def validate_bad_words(value):
    for word in bad_word:
        if word in value:
            raise ValidationError('No bad words')
        
def validate_age(value):
    if value and (value < 18 or value > 100):
        raise ValidationError('Age should be between 18 and 100')
    
def valide_email(value):
    if value and value.endswith('.what'):
        raise ValidationError("Email address should not end with '.what'.")
    
class User(models.Model):
    username = models.CharField(max_length=50,unique=True,validators=[validate_bad_words,validators.validate_slug])
    email = models.EmailField(unique=True,validators=[valide_email,validators.EmailValidator(message='enter a valid email')])
    bio = models.TextField(blank=True,validators=[validate_bad_words])
    joined_at = models.DateTimeField(default=timezone.now)
    age = models.PositiveIntegerField(null=True,validators=[validate_age])
    
    def clean(self) :
        if not self.joined_at:
            self.joined_at = timezone.now()
            
    def save(self,*args,**kwargs):
        self.full_clean()
        return super().save(*args,**kwargs)
    def __str__(self) :
        return self.username
    
    class Meta:
        ordering = ['-joined_at','username']
        constraints = [models.UniqueConstraint(fields=['username','email'],name='unique email/username')]
        verbose_name = 'user from app'
        db_table = 'users'
        
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def clean(self) :
        if len(self.post) < 10:
            raise ValidationError('POst length must be at least 10')
        
        for word in bad_word:
            if word in self.post:
                raise ValidationError('Post contains inappropriate word')
    
    def save(self,*args,**kwargs):#
        self.full_clean()
        return super().save(*args,**kwargs)
    
    def __str__(self) :
        return self.user.username
    
    class Meta :
        ordering =['created_at']
        verbose_name = 'user posts'
        db_table='post'