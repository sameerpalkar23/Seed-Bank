# Generated by Django 4.0.3 on 2022-04-14 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala'), ('Uttarpradesh', 'Uttar Pradesh'), ('Rajasthan', 'Rajasthan'), ('Bihar', 'Bihar'), ('Gujarat', 'Gujarat'), ('Bengal', 'Bengal'), ('Tamil Nadu', 'Tamil Nadu'), ('Punjab', 'Punjab')], max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala'), ('Uttarpradesh', 'Uttar Pradesh'), ('Rajasthan', 'Rajasthan'), ('Bihar', 'Bihar'), ('Gujarat', 'Gujarat'), ('Bengal', 'Bengal'), ('Tamil Nadu', 'Tamil Nadu'), ('Punjab', 'Punjab')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('catagory', models.CharField(choices=[('CP', 'C.P SEEDS'), ('ES', 'EAGLE SEEDES'), ('GH', 'GOODWILL HEALTH'), ('BS', 'BAYERN SEEDS'), ('N', 'NATURALS'), ('MH', 'Maharashta'), ('KL', 'Kerala'), ('UP', 'Utter Pradesh'), ('BR', 'Bihar'), ('RS', 'Rajasthan')], max_length=3)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('staus', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packes'), ('On THe Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
