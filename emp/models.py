from django.db import models

# Create your models here.
#Model name and class name should be different

class Emp(models.Model):
    name = models.CharField(max_length=50)
    empId = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=False)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonial/")
    rating = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name