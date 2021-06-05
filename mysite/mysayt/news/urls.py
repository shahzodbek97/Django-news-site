from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),    # funktsiya uchun
    path('', HomeNews.as_view(), name='home'),  # class uchun

    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Kategoriya'}), name='category'),

    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),

    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
