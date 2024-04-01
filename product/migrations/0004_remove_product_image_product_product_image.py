import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=cloudinary.models.CloudinaryField(
                default='placeholder',
                max_length=255,
                verbose_name='image',
            ),
        ),
    ]
