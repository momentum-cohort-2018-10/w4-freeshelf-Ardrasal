# Generated by Django 2.1.3 on 2018-11-23 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_added', models.DateField()),
                ('category', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='freeshelf.Book')),
                ('type', models.ManyToManyField(to='freeshelf.Book')),
            ],
        ),
    ]