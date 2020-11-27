# Generated by Django 3.0.6 on 2020-06-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WORLD', 'WORLD'), ('TECHNOLOGY', 'TECHNOLOGY'), ('DESIGN', 'DESIGN'), ('BUSSINESS', 'BUSSINESS'), ('POLITICS', 'POLITICS'), ('HEALTH', 'HEALTH'), ('TRAVEL', 'TRAVEL')], max_length=40),
        ),
    ]