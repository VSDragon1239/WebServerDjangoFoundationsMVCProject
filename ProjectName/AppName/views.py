from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import render
from django.views.generic import TemplateView

from AppName.viewmodels.product_viewmodel import ProductViewModel


# /views.py - Через класс - = ПРИМЕР =
from ProjectName import settings


def set_template_lang(lang_code):
    if lang_code == 'ru-ru':
        lang = 'ru'
    elif lang_code == 'en-us':
        lang = 'en'
    else:
        lang = 'en'
    return lang


class IndexView(TemplateView):
    template_name = 'index.html'

    lang = 'en'
    p_x = ''

    def get(self, request, *args, **kwargs):
        lang_code = request.GET.get('lang', None)
        lang_path = request.path

        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)

        self.p_x = request.GET.get('x', None)

        if lang_path == '/ru-ru/' and current_lang != 'ru-ru':
            lang_code = 'ru-ru'
        elif lang_path == '/en-us/' and current_lang != 'en-us':
            lang_code = 'en-us'
        else:
            print('3', lang_code, current_lang, lang_path)

        lang_code_string = f'{lang_code}'

        # Проверяем, есть ли параметр lang и отличается ли он от текущего языка
        if lang_code and lang_code in dict(settings.LANGUAGES).keys() and lang_code != current_lang:
            # Сразу активируем новый язык, чтобы он применился в ответе
            translation.activate(lang_code)

            # Сохраняем новый язык в куку
            response = HttpResponseRedirect(f"/{lang_code_string}?{request.META.get('QUERY_STRING', '')}")
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

            # Обновляем страницу
            self.lang = set_template_lang(lang_code)

            return response
        else:
            # Если язык уже установлен или параметра lang нет, используем язык из куки
            translation.activate(current_lang)

            # Обновляем страницу
            self.lang = set_template_lang(current_lang)

            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param_lang"] = self.lang
        context["p_x"] = self.p_x
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(IndexView, self).render_to_response(context, **response_kwargs)


class AboutView(TemplateView):
    template_name = 'about.html'
    lang = 'en'

    def get(self, request, *args, **kwargs):
        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)
        self.lang = set_template_lang(current_lang)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param_lang"] = self.lang
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(AboutView, self).render_to_response(context, **response_kwargs)


class ProductsView(TemplateView):
    template_name = 'products.html'
    lang = 'en'

    def get(self, request, *args, **kwargs):
        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)
        self.lang = set_template_lang(current_lang)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param_lang"] = self.lang
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(ProductsView, self).render_to_response(context, **response_kwargs)


class ContactView(TemplateView):
    template_name = 'contact.html'
    lang = 'en'

    def get(self, request, *args, **kwargs):
        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)
        self.lang = set_template_lang(current_lang)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param_lang"] = self.lang
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(ContactView, self).render_to_response(context, **response_kwargs)


class FAQView(TemplateView):
    template_name = 'faq.html'
    lang = 'en'

    def get(self, request, *args, **kwargs):
        current_lang = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE)
        self.lang = set_template_lang(current_lang)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param_lang"] = self.lang
        return context

    def render_to_response(self, context, **response_kwargs):
        return super(FAQView, self).render_to_response(context, **response_kwargs)

