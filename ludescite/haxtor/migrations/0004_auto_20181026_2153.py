# Generated by Django 2.1.1 on 2018-10-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haxtor', '0003_auto_20181026_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCat',
            field=models.CharField(choices=[('1', 'kids'), ('2', 'coder')], max_length=254),
        ),
    ]
