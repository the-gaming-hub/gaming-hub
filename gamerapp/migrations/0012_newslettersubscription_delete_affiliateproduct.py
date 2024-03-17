# Generated by Django 4.2.4 on 2024-03-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamerapp', '0011_sub_subcategory_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('subscribed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AffiliateProduct',
        ),
    ]