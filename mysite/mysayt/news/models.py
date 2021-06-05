from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Yangilik sarlavhasi')
    content = models.TextField(blank=True, verbose_name='Yangilikning asosiy qismi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Rasm', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Nashir etilgan')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Kategoriya')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Kategoriya nomi')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya nomi'
        verbose_name_plural = 'Kategoriya nomlari'
        ordering = ['title']
