# Generated by Django 2.1.5 on 2019-01-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190107_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]
