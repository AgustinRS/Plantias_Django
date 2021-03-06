# Generated by Django 4.0.5 on 2022-07-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('idDescuento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreDescuento', models.CharField(max_length=30)),
                ('porcetajeDescuento', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='modelo',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
