# Generated by Django 2.2.7 on 2020-09-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kombat', '0006_kanospecialattack'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadebasicattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='jadespecialattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='jadestringattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='kanobasicattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='kanospecialattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='kanostringattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='nightwolfbasicattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='nightwolfspecialattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='nightwolfstringattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='subzerobasicattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='subzerospecialattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='subzerostringattack',
            name='Buttons',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
