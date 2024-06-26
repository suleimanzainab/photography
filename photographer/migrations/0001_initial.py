# Generated by Django 3.2 on 2023-06-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('province', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('streetNumber', models.CharField(max_length=200)),
                ('years_experience', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Photographer',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('activity_type', models.CharField(max_length=200)),
                ('canBeRequested', models.BooleanField(default=False)),
                ('photographer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photographer.photographer')),
            ],
            options={
                'db_table': 'Activity',
            },
        ),
    ]
