from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_image_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cleanser', 'Cleanser'),
                    ('moisturizer', 'Moisturizer'),
                    ('serum', 'Serum'),
                    ('sunscreen', 'Sunscreen'),
                    ('mask', 'Mask'),
                    ('toner', 'Toner'),
                    ('exfoliant', 'Exfoliant'),
                    ('eye_cream', 'Eye Cream')
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
