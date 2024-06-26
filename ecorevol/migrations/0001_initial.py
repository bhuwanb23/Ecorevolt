# Generated by Django 4.0.6 on 2024-05-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Innovator',
            fields=[
                ('fname', models.CharField(default=0, max_length=100)),
                ('lname', models.CharField(default=0, max_length=50)),
                ('email', models.CharField(default=0, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(default=0, max_length=100)),
                ('companyname', models.CharField(default=0, max_length=50)),
                ('project_list', models.PositiveIntegerField(blank=True, default=0)),
                ('address', models.CharField(default=0, max_length=50)),
                ('noofprojects', models.PositiveIntegerField(default=0)),
                ('desc', models.CharField(default=0, max_length=100)),
                ('education', models.CharField(default=0, max_length=50)),
                ('interest', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('fname', models.CharField(default=0, max_length=100)),
                ('lname', models.CharField(default=0, max_length=50)),
                ('email', models.CharField(default=0, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(default=0, max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('investment_amount', models.PositiveIntegerField(default=0)),
                ('contactno', models.PositiveBigIntegerField(default=0)),
                ('project_list', models.CharField(default=0, max_length=50)),
                ('companyname', models.CharField(default=0, max_length=50)),
                ('address', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pid', models.PositiveIntegerField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('pname', models.CharField(max_length=200)),
                ('owner_uname', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(default=None, max_length=50)),
                ('funding_goal', models.DecimalField(decimal_places=8, max_digits=8)),
                ('amtraised', models.PositiveBigIntegerField(default=0)),
                ('noofinvestors', models.PositiveIntegerField(default=0)),
                ('is_sdg', models.BooleanField(default=False)),
                ('partner', models.CharField(max_length=80)),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
                ('img4', models.ImageField(upload_to='')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
    ]
