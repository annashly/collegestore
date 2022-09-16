from django.db import models

DEPARTMENT_CHOICE = (
 ('Department of Economics','Department of Economics'),
 ('Department of English','Department of English'),
 ('Department of Physics','Department of Physics'),
 ('Department of Commerce','Department of Commerce'),
 ('Department of Computer Science','Department of Computer Science'),
)
PURPOSE_CHOICE = (
 ('Enquiry','Enquiry'),
 ('Place Order','Place Order'),
 ('Return','Return'),
)

class Membership(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 age = models.IntegerField()
 gender = models.CharField(max_length=100)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 address = models.CharField(max_length=100)
 department = models.CharField(choices=DEPARTMENT_CHOICE, max_length=50)
 course = models.CharField(max_length=50)
 purpose = models.CharField(choices=PURPOSE_CHOICE, max_length=50)
 materials_provide= models.FileField(upload_to='doc', blank=True)