# Generated by Django 4.2.7 on 2023-12-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0007_coursemodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='type',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermidiate', 'Intermidiate'), ('Advanced', 'Advanced')], default='Major', max_length=25),
        ),
    ]
