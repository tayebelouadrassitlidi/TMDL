# Generated by Django 4.2.4 on 2023-12-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normaldemonlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normallevel',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('Hard Demon', 'Hard Demon'), ('Insane Demon', 'Insane Demon'), ('Extreme Demon', 'Extreme Demon')], max_length=255),
        ),
        migrations.AlterField(
            model_name='normallevel',
            name='duration',
            field=models.CharField(blank=True, choices=[('Tiny', 'Tiny'), ('Short', 'Short'), ('Medium', 'Medium'), ('Long', 'Long'), ('XL', 'XL')], max_length=255),
        ),
        migrations.AlterField(
            model_name='normallevel',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='normallevel',
            name='publisher',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]