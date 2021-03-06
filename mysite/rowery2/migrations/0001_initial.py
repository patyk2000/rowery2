# Generated by Django 4.0.5 on 2022-06-14 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derailleur', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Typeofbike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikename', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('derailleur', models.ManyToManyField(to='rowery2.parts')),
                ('typeofbike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rowery2.typeofbike')),
            ],
        ),
    ]
