# Generated by Django 2.0.5 on 2018-05-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_concluido',
            field=models.DateTimeField(null=True),
        ),
    ]