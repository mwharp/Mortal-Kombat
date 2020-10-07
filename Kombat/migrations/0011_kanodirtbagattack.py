# Generated by Django 2.2.7 on 2020-09-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kombat', '0010_kanoripperattack'),
    ]

    operations = [
        migrations.CreateModel(
            name='KanoDirtbagAttack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Move', models.CharField(max_length=50)),
                ('Buttons', models.CharField(default='N/A', max_length=50)),
                ('Startup', models.PositiveIntegerField()),
                ('Active', models.PositiveIntegerField()),
                ('Recovery', models.PositiveIntegerField()),
                ('HitAdv', models.PositiveIntegerField()),
                ('BlockAdv', models.SmallIntegerField()),
                ('FBlockAdv', models.SmallIntegerField()),
            ],
        ),
    ]
