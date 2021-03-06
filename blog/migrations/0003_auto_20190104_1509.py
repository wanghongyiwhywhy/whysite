# Generated by Django 2.1.4 on 2019-01-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190103_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='upload/', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_type',
            field=models.CharField(choices=[('normal', '普通'), ('star', '精选')], default='mormal', max_length=10, verbose_name='类型'),
        ),
    ]
