from django.db import models

# Create your models here.

# Creating Company Model


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('Non IT', 'Non IT'),
                                                     ("Mobiles Phones",
                                                      'Mobile Phones'),
                                                     ('Electronics',
                                                      'Electronics'),
                                                     ('Other', 'Other'),


                                                     ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '--' + self.location


# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('Project Manager', 'Project Manager'),
        ('Software Developer', 'Software Developer'),
        ('Team Leader', 'Team Leader'),
        ('Tester', 'Tester'),
        ('Digital Marketing', 'Digital Marketer'),
        ('Content Writer', 'Content Writer'),
        ('Graphic Designer', 'Graphic Designer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('HR', 'HR'),
        ('Accountant', 'Accountant'),
        ('Sales', 'Sales'),
        ('Other', 'Other'),
    ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
