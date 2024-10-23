from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import render
from django.views.generic import TemplateView

from AppName.viewmodels.product_viewmodel import ProductViewModel


# /views.py - Через класс - = ПРИМЕР =
from ProjectName import settings


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        lang_code = request.GET.get('lang', None)
        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)

        # Проверяем, есть ли параметр lang и отличается ли он от текущего языка
        if lang_code and lang_code in dict(settings.LANGUAGES).keys() and lang_code != current_lang:
            # Сразу активируем новый язык, чтобы он применился в ответе
            translation.activate(lang_code)

            # Сохраняем новый язык в куку
            response = HttpResponseRedirect(f"{request.path}?{request.META.get('QUERY_STRING', '')}")
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
            return response
        else:
            # Если язык уже установлен или параметра lang нет, используем язык из куки
            translation.activate(current_lang)
            return super().get(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'about.html'


class ProductsView(TemplateView):
    template_name = 'products.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class FAQView(TemplateView):
    template_name = 'faq.html'
