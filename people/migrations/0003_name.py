# Generated by Django 2.1.4 on 2019-02-02 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('people', '0002_person_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('birth_name', 'Birth name'), ('married_name', 'Married name'),
                                                   ('also_known_as', 'Also known as'),
                                                   ('adoptive_name', 'Adoptive name'), ('formal_name', 'Formal name'),
                                                   ('religious_name', 'Religious name')], max_length=255, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
            ],
        ),
    ]
