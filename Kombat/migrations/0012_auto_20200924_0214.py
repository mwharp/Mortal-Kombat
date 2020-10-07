# Generated by Django 2.2.7 on 2020-09-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kombat', '0011_kanodirtbagattack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadebasicattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadebasicattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadebasicattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadespecialattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadespecialattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadespecialattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadestringattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadestringattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='jadestringattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanodirtbagattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanodirtbagattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanodirtbagattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanoripperattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanoripperattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanospecialattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanospecialattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanospecialattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanostringattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='kanostringattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfbasicattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfbasicattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfbasicattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfspecialattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfspecialattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfspecialattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfstringattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfstringattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='nightwolfstringattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerobasicattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerobasicattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerobasicattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerospecialattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerospecialattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerospecialattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerostringattack',
            name='Active',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerostringattack',
            name='HitAdv',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='subzerostringattack',
            name='Recovery',
            field=models.SmallIntegerField(),
        ),
    ]
