# Generated by Django 2.2.17 on 2021-03-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloApenasParaTeste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500, verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Texto',
                'verbose_name_plural': 'Textos',
            },
        ),
    ]
