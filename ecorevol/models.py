from django.db import models

class Innovator(models.Model):
    fname = models.CharField(max_length=100, default=0)
    lname = models.CharField(max_length=50, default=0)
    email = models.CharField(primary_key=True, unique=True, max_length=50, default=0)
    password = models.CharField(max_length=100, default=0)
    companyname = models.CharField(max_length=50, default=0)
    project_list = models.PositiveIntegerField(blank=True, default=0)
    address = models.CharField(max_length=50, default=0)
    noofprojects = models.PositiveIntegerField(default=0)
    desc = models.CharField(max_length=100, default=0)
    education = models.CharField(max_length=50, default=0)
    interest = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.fname

class Investor(models.Model):
    fname = models.CharField(max_length=100, default=0)
    lname = models.CharField(max_length=50, default=0)
    email = models.CharField(primary_key=True, unique=True, max_length=50, default=0)
    password = models.CharField(max_length=50, default=0)
    age = models.PositiveIntegerField(default=0)
    investment_amount = models.PositiveIntegerField(default=0)
    contactno = models.PositiveBigIntegerField(default=0)
    project_list = models.CharField(max_length=50, default=0)
    companyname = models.CharField(max_length=50, default=0)
    address = models.CharField(max_length=50, default=0)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Project(models.Model):
    pid = models.PositiveIntegerField(primary_key=True, unique=True, max_length=50)
    pname = models.CharField(max_length=200)
    owner_uname = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=50, default=None)
    funding_goal = models.DecimalField(max_digits=8, decimal_places=8)
    amtraised = models.PositiveBigIntegerField(default=0)
    noofinvestors = models.PositiveIntegerField(default=0)
    is_sdg = models.BooleanField(default=False)
    partner = models.CharField(max_length=80)
    img1 = models.ImageField(upload_to='', max_length=100)
    img2 = models.ImageField(upload_to='', max_length=100)
    img3 = models.ImageField(upload_to='', max_length=100)
    img4 = models.ImageField(upload_to='', max_length=100)
    video = models.FileField(upload_to='', max_length=100)
    
    def __str__(self):
        return self.pname
