# Generated by Django 2.1 on 2020-02-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_student_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='avatar.jpg', max_length='100', upload_to='avatar/'),
        ),
    ]