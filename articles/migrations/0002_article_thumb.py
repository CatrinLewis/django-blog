# Generated by Django 3.2 on 2021-04-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='defaul.png', upload_to=''),
        ),
    ]
