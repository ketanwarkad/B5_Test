# Generated by Django 3.2.6 on 2021-08-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20210809_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(db_table='emp_projects', to='app1.Employee'),
        ),
    ]