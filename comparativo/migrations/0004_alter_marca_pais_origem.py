# Generated by Django 3.2.16 on 2022-11-02 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparativo', '0003_auto_20221102_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='pais_origem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comparativo.pais'),
        ),
    ]
