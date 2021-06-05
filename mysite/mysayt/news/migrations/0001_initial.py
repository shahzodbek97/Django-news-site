# Generated by Django 3.2.3 on 2021-06-02 07:19

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya nomi',
                'verbose_name_plural': 'Kategoriya nomlari',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Yangilik sarlavhasi')),
                ('content', models.TextField(blank=True, verbose_name='Yangilikning asosiy qismi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Rasm')),
                ('is_published', models.BooleanField(default=True, verbose_name='Nashir etilgan')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category')),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
                'ordering': ['-created_at'],
            },
        ),
    ]
