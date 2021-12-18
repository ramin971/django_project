from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=80)
    code=models.CharField(max_length=2)
    def __str__(self):
        return "{}({})".format(self.name,self.code)
    class Meta:
        verbose_name_plural="Countries"



class Address(models.Model):
    city=models.CharField(max_length=50)
    street=models.CharField(max_length=80)
    postal_code=models.CharField(max_length=10)
    def __str__(self):
        return self.city +'_'+ self.street + '('+self.postal_code +')'
    class Meta:
        verbose_name_plural="Address Entries"


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    def full_name(self):
        return self.first_name+"_"+self.last_name
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title= models.CharField(max_length=40)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(null=False,db_index=True)
    published_countries=models.ManyToManyField(Country)
    def __str__(self):
        return "{} ".format(self.title)

    # def save(self,*args,**kwargs):
    #     self.slug=slugify(self.title)
    #     super().save(*args,**kwargs)
