# Generated by Django 4.1.7 on 2023-04-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.bookmark'),
        ),
        migrations.AlterField(
            model_name='post',
            name='folder',
            field=models.ManyToManyField(blank=True, to='forum.folder'),
        ),
    ]