# Generated by Django 3.2.3 on 2021-05-22 17:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('created', models.DateField(auto_now_add=True)),
                ('principal', models.CharField(max_length=64)),
                ('principal_address', models.CharField(blank=True, max_length=128, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TIS_app.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('latin_name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('crown_width', models.PositiveIntegerField()),
                ('roloff', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=(0, '0'))),
                ('is_existing', models.BooleanField(default=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TIS_app.inventory')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TIS_app.species')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TIS_app.tree')),
            ],
        ),
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(600)])),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TIS_app.tree')),
            ],
        ),
    ]
