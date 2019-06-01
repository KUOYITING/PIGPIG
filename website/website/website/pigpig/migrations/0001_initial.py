# Generated by Django 2.0 on 2019-05-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('english', models.CharField(max_length=20)),
                ('taste', models.TextField()),
                ('cooking', models.TextField()),
                ('recipename', models.CharField(max_length=20)),
                ('recipename2', models.CharField(max_length=20)),
                ('recipe', models.TextField()),
                ('pic1', models.CharField(max_length=50)),
                ('pic2', models.CharField(max_length=50)),
                ('pic3', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
            ],
        ),
    ]
