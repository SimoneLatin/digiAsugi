# Generated by Django 3.2.9 on 2022-02-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tessera', models.CharField(max_length=20)),
                ('positivit√†', models.BooleanField()),
                ('questionario', models.BooleanField()),
            ],
        ),
    ]
