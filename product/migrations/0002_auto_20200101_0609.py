# Generated by Django 2.2.2 on 2020-01-01 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=128, verbose_name='プラン名')),
                ('price', models.PositiveIntegerField(verbose_name='価格')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
