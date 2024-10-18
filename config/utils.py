import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import RegexValidator
from rest_framework import serializers
from config.settings import MAX_UPLOAD_SIZE
from django.template.defaultfilters import filesizeformat

NULLABLE = {"blank": True, "null": True}


def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return f"{instance._meta.app_label}/{instance.__class__.__name__}/{filename}"


def charfield_only_limit_digits(name: str, number: int) -> models.CharField:
    """
    Создает поле CharField только с цифрами с ограничением по количеству цифр
    """
    return models.CharField(
        validators=[RegexValidator(regex=r"\d{" + f"{number}" + "}")],
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Состоит из {number} цифр",
    )


def charfield_specific_length_without_valid(name: str, number: int) -> models.CharField:
    """
    Создает поле CharField определенной длины, без валидации
    """
    return models.CharField(
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Текст не более {number} символов",
    )


def charfield_validator_letters_and_extra(
    name: str, number: int, extra=(), nullable=False
) -> models.CharField:
    """
    Создает поле CharField с валидатором: только буквы и символы из extra, исключая остальные символы
    """
    # если необязательное поле и может быть пустым, то True
    text = "(необязательно)" if nullable else ""
    nullable = NULLABLE if nullable else {}

    return models.CharField(
        validators=[
            RegexValidator(regex=r"^[a-zA-Zа-яА-Я" + f"{''.join(extra)}" + "]+$")
        ],
        max_length=number,
        verbose_name=f"{name}",
        help_text=f"Только буквы и {extra} не более {number} символов {text}",
        **nullable,
    )


def imagefield(name: str, nullable=False) -> models.ImageField:
    """
    Создает поле ImageField
    """
    # если необязательное поле и может быть пустым, то True
    text = "(необязательно)" if nullable else ""
    nullable = NULLABLE if nullable else {}

    return models.ImageField(
        upload_to=docs_path,
        verbose_name=f"{name}",
        help_text=f"Добавьте {name} {text}",
        **nullable,
    )


def charfield_with_choices(name: str, choice: dict) -> models.CharField:
    """
    Создает поле CharField с choices
    """
    return models.CharField(
        verbose_name=f"{name}",
        choices=choice,
    )


def filefield(name: str) -> models.FileField:
    """
    Создает поле FileField
    """
    return models.FileField(
        verbose_name=f"{name}",
        upload_to=docs_path,
        help_text=f"Добавьте {name}",
    )


def textfield_specific_length(name: str, number: int) -> models.TextField:
    """
    Создает поле TextField определенной длины
    """
    return models.TextField(
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Не более {number} символов",
    )


def emailfield(text: str) -> models.EmailField:
    """
    Создает поле EmailField
    """
    return models.EmailField(
        verbose_name=f"email {text}",
        help_text="Введите email: example@mail.com",
        max_length=254,
    )


def phonenumberfield(name: str, nullable=False) -> PhoneNumberField:
    """
    Создает поле PhoneNumberField
    """
    # если необязательное поле и может быть пустым, то True
    text = "(необязательно)" if nullable else ""
    nullable = NULLABLE if nullable else {}
    return PhoneNumberField(
        region="RU",
        verbose_name=f"{name}",
        help_text=f"Введите {name} {text}",
        **nullable,
    )


def check_file(self):
    """
    Ограничение размера загружаемого файла
    """
    if self.size > MAX_UPLOAD_SIZE:
        raise serializers.ValidationError(
            f"Пожалуйста, не превышайте размер файла {filesizeformat(MAX_UPLOAD_SIZE)}. Текущий размер файла {filesizeformat(self.size)}"
        )
    return self


@receiver(post_delete)
def delete_mediafile_on_delete(sender, instance, **kwargs):
    """
    Удаляет медиафайл с именем переменной link из папки проекта при удалении записи в БД
    """
    # важно!!! все переменные, сохраняющие файл в БД должны иметь имя link
    if "link" in instance.__class__.__dict__.keys():
        # Получаем путь ссылки
        link_path = instance.link.path
        # Проверяем, существует ли файл по указанному пути
        if os.path.isfile(link_path):
            try:
                os.remove(link_path)
                return f"Файл {link_path} успешно удален"
            except Exception as e:
                return f"Ошибка при удалении файла {link_path}: {e}"
        else:
            return f"Файл {link_path} не найден"

def urlfield(name: str, nullable=False) -> models.URLField:
    """
    Создает поле URLField
    """
    nullable = NULLABLE if nullable else {}
    return models.URLField(
        verbose_name=name,
        **nullable,
    )

def datetimefield(name: str, auto_now_add=False, auto_now=False) -> models.DateTimeField:
    """
    Создает поле DateTimeField
    """
    return models.DateTimeField(
        verbose_name=name,
        auto_now_add=auto_now_add,
        auto_now=auto_now
    )

