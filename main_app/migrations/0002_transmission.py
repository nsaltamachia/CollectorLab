# Generated by Django 4.2.7 on 2023-11-17 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tran', models.CharField(choices=[('2A', '2spd automatic'), ('3A', '3spd automatic'), ('3M', '3spd manual'), ('4M', '4spd manual')], default='3A', max_length=2)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]