# Generated by Django 3.2.16 on 2022-11-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='versao',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
