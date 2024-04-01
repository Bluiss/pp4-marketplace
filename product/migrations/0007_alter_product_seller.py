from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='product_products',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
