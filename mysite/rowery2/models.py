from django.db import models
#from django.forms import CharField

class Typeofbike(models.Model):
    typename=models.CharField(max_length=200)
    
    def __str__(self):
        return self.typename


class Parts(models.Model):
    derailleur=models.CharField(max_length=200)
   
    def __str__(self):
        return self.derailleur

class Bike(models.Model):
    bikename=models.CharField(max_length=200, null=True)
    typeofbike=models.ForeignKey(Typeofbike, on_delete=models.CASCADE)
    derailleur=models.ManyToManyField(Parts)
    description=models.TextField()

    def __str__(self):
        return self.bikename