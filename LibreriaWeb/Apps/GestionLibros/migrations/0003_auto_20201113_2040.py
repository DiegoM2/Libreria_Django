# Generated by Django 3.1.2 on 2020-11-13 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionLibros', '0002_auto_20201113_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GestionLibros.autor'),
        ),
    ]
