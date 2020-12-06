# Generated by Django 3.1.3 on 2020-12-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Student ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=8, verbose_name='Gender')),
                ('dept', models.CharField(choices=[('Faculty of Engineering', 'Department of Computing')], default=None, max_length=50, verbose_name='Department')),
                ('major', models.CharField(default=None, max_length=50, verbose_name='Major')),
                ('password', models.CharField(default='111', max_length=50, verbose_name='Password')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Teacher ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=8, verbose_name='Gender')),
                ('dept', models.CharField(choices=[('Faculty of Engineering', 'Department of Computing')], default=None, max_length=50, verbose_name='Department')),
                ('password', models.CharField(default='111', max_length=50, verbose_name='Password')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
                'db_table': 'teacher',
            },
        ),
    ]
