# Generated by Django 2.2 on 2021-06-21 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210621_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Tile'),
        ),
    ]