# Generated by Django 4.0.5 on 2022-07-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0002_rename_retal_period_book_rental_period_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('availble', 'availble'), ('rental', 'rental'), ('sold', 'sold')], max_length=50),
        ),
    ]
