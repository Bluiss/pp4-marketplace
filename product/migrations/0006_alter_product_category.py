# Generated by Django 4.2.9 on 2024-03-10 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(
                blank=True,
                choices=[
                    ('Cleanser', 'cleanser'),
                    ('Moisturizer', 'moisturizer'),
                    ('Serum', 'serum'),
                    ('Sunscreen', 'sunscreen'),
                    ('Mask', 'mask'),
                    ('Toner', 'toner'),
                    ('Exfoliant', 'exfoliant'),
                    ('Eye Cream', 'eye_cream')
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
