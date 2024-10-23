# AppName/urls.py
from django.urls import path
from AppName.views import IndexView, AboutView, ProductsView, ContactView, FAQView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),               # Главная страница
    path('about/', AboutView.as_view(), name='about'),       # Страница "О проекте"
    path('products/', ProductsView.as_view(), name='products'),  # Страница продуктов
    path('contact/', ContactView.as_view(), name='contact'),   # Страница контактов
    path('faq/', FAQView.as_view(), name='faq'),             # Страница FAQ
]
