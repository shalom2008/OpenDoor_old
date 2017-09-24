# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_qty', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='')),
                ('price', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='')),
                ('discount', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='InvoiceHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=14, unique=True, verbose_name='')),
                ('order_date', models.DateField(blank=True, null=True, verbose_name='')),
                ('submit_date', models.DateField(verbose_name='')),
                ('confirm_date', models.DateField(verbose_name='')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='')),
                ('end', models.DateField(blank=True, null=True, verbose_name='')),
                ('creator', models.CharField(blank=True, max_length=32, null=True, verbose_name='')),
                ('modifier', models.CharField(blank=True, max_length=32, null=True, verbose_name='')),
                ('create_time', models.DateTimeField(blank=True, null=True, verbose_name='')),
                ('modify_time', models.DateTimeField(blank=True, null=True, verbose_name='')),
                ('status', models.CharField(choices=[('open', '开立'), ('submit', '提交'), ('confirm', '审核'), ('cancel', '作废')], max_length=1, verbose_name='')),
                ('desc', models.CharField(blank=True, max_length=128, null=True, verbose_name='')),
                ('address', models.CharField(max_length=256, verbose_name='地址')),
                ('fax_number', models.CharField(max_length=64, verbose_name='传真号码')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Brand')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Customer')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Department')),
                ('order_taker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_order_taker', to='basedata.Staff')),
                ('sale_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.SaleType')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_salesman', to='basedata.Staff')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Tax')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='invoice_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.InvoiceHeader'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basedata.Material'),
        ),
    ]
