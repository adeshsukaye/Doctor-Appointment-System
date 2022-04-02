# Generated by Django 4.0.3 on 2022-03-07 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=150)),
                ('Maritial_Status', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapp.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=150)),
                ('Maritial_Status', models.CharField(max_length=50)),
                ('Degree', models.CharField(max_length=50)),
                ('ExpertIn', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Doctor_Status', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapp.usermaster')),
            ],
        ),
    ]