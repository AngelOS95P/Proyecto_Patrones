# Generated by Django 3.2.14 on 2022-07-28 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_alter_teacher_idnumber'),
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.student'),
        ),
    ]
