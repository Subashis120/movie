# Generated by Django 3.2.9 on 2021-11-12 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0002_alter_movie_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='CatID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_api.category'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_api.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='UID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_api.users'),
        ),
        migrations.AlterField(
            model_name='review',
            name='MID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_api.movie'),
        ),
        migrations.AlterField(
            model_name='review',
            name='UID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_api.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='EMAIL',
            field=models.EmailField(max_length=255),
        ),
    ]