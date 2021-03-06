# Generated by Django 2.1 on 2020-01-28 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('hash_password', models.CharField(blank=True, max_length=128, null=True, verbose_name='哈希密码')),
                ('gender', models.CharField(choices=[('mail', '男'), ('female', '女')], default='男', max_length=10, verbose_name='性别')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='邮箱')),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册日期')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
