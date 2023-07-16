# Generated by Django 4.1.5 on 2023-05-02 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name=' 📌 Title ')),
                ('desc', models.CharField(blank=True, default='', max_length=100, verbose_name='💬 Small Message?')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Others')], max_length=1, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=13)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=150, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('coaching_type_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientsapp.course')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
