# Generated by Django 4.0.5 on 2022-07-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='retal_period',
            new_name='rental_period',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='retal_price_day',
            new_name='rental_price_day',
        ),
        migrations.AlterField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('availble', 'availble'), ('rental', 'retal'), ('sold', 'sold')], max_length=50),
        ),
    ]
