# Generated by Django 3.1 on 2020-08-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0003_auto_20200819_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastroast',
            name='totalvotes',
        ),
        migrations.AlterField(
            model_name='boastroast',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boastroast',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
