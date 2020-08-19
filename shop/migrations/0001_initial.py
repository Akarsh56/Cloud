# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-19 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('parent_cat', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='Media/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_location', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
        ),
    ]
