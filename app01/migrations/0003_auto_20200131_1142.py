# Generated by Django 2.1 on 2020-01-31 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200128_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('email', models.EmailField(max_length=100)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '学生管理',
                'verbose_name_plural': '学生管理',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=10, verbose_name='性别'),
        ),
    ]