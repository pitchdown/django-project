# Generated by Django 5.1.2 on 2024-10-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genre',
            field=models.CharField(choices=[('Rap/Hip-Hop', 'Rap/Hip-Hop'), ('Rock', 'Rock'), ('Metal', 'Metal'), ('Soul/Funk', 'Soul/Funk'), ('Jazz', 'Jazz'), ('Blues', 'Blues'), ('Country', 'Country'), ('Pop', 'Pop'), ('Electronic', 'Electronic'), ('R&B', 'R&B'), ('Instrumental', 'Instrumental')], default='', max_length=50),
        ),
    ]
