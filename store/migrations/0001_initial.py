# Generated by Django 3.1 on 2020-08-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=256)),
                ('business_day', models.CharField(blank=True, max_length=50, null=True)),
                ('opening_hour', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
    ]
