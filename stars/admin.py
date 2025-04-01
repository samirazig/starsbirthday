from django.contrib import admin
from .models import Star  # Импортируем вашу модель

# Регистрируем модель
admin.site.register(Star)

admin.site.site_header = "Моя Админка"          # Заголовок на странице входа
admin.site.site_title = "Административный сайт" # Заголовок вкладки браузера
admin.site.index_title = "Добро пожаловать!"    # Подзаголовок на главной админки