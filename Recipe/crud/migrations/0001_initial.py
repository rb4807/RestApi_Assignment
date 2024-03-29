# Generated by Django 5.0.2 on 2024-03-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=150, null=True)),
                ('recipe', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='dish')),
                ('ingredients', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('vegetarian', 'Vegetarian'), ('non_vegetarian', 'Non-Vegetarian')], max_length=50)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('juices', 'Juices')], max_length=50)),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('average_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('total_reviews', models.IntegerField(default=0)),
            ],
        ),
    ]
