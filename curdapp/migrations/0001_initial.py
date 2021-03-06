# Generated by Django 2.2.3 on 2020-12-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_cost', models.IntegerField()),
                ('product_class', models.CharField(max_length=50)),
                ('product_weight', models.IntegerField()),
            ],
        ),
    ]
