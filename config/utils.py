import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from config.settings import IMAGE_AND_DOCS_UPLOAD_SIZE, VIDEO_UPLOAD_SIZE
from config.validators import validate_no_mixed_scripts, validate_name_or_surname, \
    validate_number_of_spaces_or_dashes, validate_email, validate_comment
from django.core.exceptions import ValidationError

NULLABLE = {"blank": True, "null": True}


def validate_file_size(value):
    if value.size > IMAGE_AND_DOCS_UPLOAD_SIZE * 1024 * 1024:
        raise ValidationError(f"Размер файла не должен превышать {IMAGE_AND_DOCS_UPLOAD_SIZE} МБ")
    
def validate_video_size(value):
    if value.size > VIDEO_UPLOAD_SIZE * 1024 * 1024:
        raise ValidationError(f"Размер файла не должен превышать {VIDEO_UPLOAD_SIZE} МБ")
    
def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return f"{instance._meta.app_label}/{instance.__class__.__name__}/{filename}"


def char_field_only_limit_digits(
        name: str, number: int
        ) -> models.CharField:
    """
    Создает поле CharField только с цифрами с ограничением по количеству цифр
    """
    return models.CharField(
        validators=[RegexValidator(regex=r"\d{" + f"{number}" + "}")],
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Состоит из {number} цифр",
    )


def char_field_specific_length_without_valid(name: str, number: int) -> models.CharField:
    """
    Создает поле CharField определенной длины, без валидации
    """
    return models.CharField(
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Текст не более {number} символов",
    )
def char_field_with_default(
        name: str, number: int, default: str
        ) -> models.CharField:
    """
    Создает поле CharField определенной длины, без валидации
    """
    return models.CharField(
        verbose_name=f"{name}",
        max_length=number,
        default=default,
        help_text=f"Текст не более {number} символов",
    )


def char_field_validator_letters_and_extra(
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


def image_field(name: str, nullable=False) -> models.ImageField:
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
        validators=[validate_file_size],
    )




def char_field_with_choices(name: str, choice: dict) -> models.CharField:
    """
    Создает поле CharField с choices
    """
    return models.CharField(
        verbose_name=f"{name}",
        choices=choice,
    )
def char_field_for_payment(name: str, max_length: int) -> models.CharField:
    return models.CharField(
        max_length=max_length, unique=True,
        verbose_name=name,
        help_text="ID платежа, пример: 6dec59c0-c176-4132-85b1-a161e5c4bd7f",
    )


def file_field(name: str, nullable=False) -> models.FileField:
    """
    Создает поле FileField
    """
    
    text = "(необязательно)" if nullable else ""
    nullable = NULLABLE if nullable else {}

    return models.FileField(
        upload_to=docs_path,
        verbose_name=f"{name}",
        help_text=f"Добавьте {name} {text}",
        **nullable,
        validators=[validate_file_size],
    )
def video_field(name: str, nullable=False) -> models.FileField:
    """
    Создает поле FileField
    """
    
    text = "(необязательно)" if nullable else ""
    nullable = NULLABLE if nullable else {}

    return models.FileField(
        upload_to=docs_path,
        verbose_name=f"{name}",
        help_text=f"Добавьте {name} {text}",
        **nullable,
        validators=[validate_video_size],
    )


def text_field_specific_length(name: str, number: int) -> models.TextField:
    """
    Создает поле TextField определенной длины
    """
    return models.TextField(
        verbose_name=f"{name}",
        max_length=number,
        help_text=f"Не более {number} символов",
    )

def text_field_validation(name: str) -> models.TextField:
    """
    Создает поле TextField для комментариев
    """
    return models.TextField(
        blank=True,
        verbose_name=name,
        validators=[
            MaxLengthValidator(1000, _("Комментарий не может быть длиннее 1000 символов.")),
            validate_no_mixed_scripts,
            validate_number_of_spaces_or_dashes,
            validate_comment,
        ]
    )


def email_field(text: str) -> models.EmailField:
    """
    Создает поле EmailField
    """
    return models.EmailField(
        verbose_name=f"email {text}",
        help_text="Введите email: example@mail.com",
        max_length=254,
    )


@receiver(post_delete)
def delete_mediafile_on_delete(sender, instance, **kwargs):
    """
    Удаляет медиафайл с именем переменной link из папки проекта при удалении записи в БД
    """
    # важно!!! все переменные, сохраняющие файл в БД должны иметь имя link
    if "link" in instance.__class__.__dict__.keys() and instance.link:
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


def char_field_address_specific_length_with_nullability(name: str, max_length: int) -> models.CharField:
    """
    Создает поле CharField определенной длины, с возможностью null и blank
    """
    return models.CharField(
        verbose_name=name,
        max_length=max_length,
        help_text=f"Текст не более {max_length} символов",
        **NULLABLE,
    )


def datetime_field_with_nullability(name: str) -> models.DateTimeField:
    """
    Создает поле DateTimeField с возможностью null и blank
    """
    return models.DateTimeField(
        verbose_name=name,
        **NULLABLE,
    )


def char_field_length_validation(name: str, max_length: int) -> models.CharField:
    """
    Создает поле CharField с дополнительными параметрами и валидаторами.
    """
    return models.CharField(
        verbose_name=name,
        max_length=max_length,
        validators=[
            MinLengthValidator(1, _("Имя должно быть не менее 1 символа")),
            MaxLengthValidator(max_length, _("Имя должно быть не более 64 символов")),
            validate_name_or_surname,
            validate_no_mixed_scripts,
            validate_number_of_spaces_or_dashes,
        ],
    )


def email_field_validation(name: str) -> models.EmailField:
    """
    Создает поле EmailField с валидаторами
    """
    return models.EmailField(
        verbose_name=name,
        validators=[
            MaxLengthValidator(254, _("Email не может быть длиннее 254 символов")),
            validate_email,
        ],
    )




def datetime_field(name: str, auto_now_add=False, auto_now=False) -> models.DateTimeField:
    """
    Создает поле DateTimeField
    """
    return models.DateTimeField(
        verbose_name=name,
        auto_now_add=auto_now_add,
        auto_now=auto_now
    )


def boolean_field(name: str, default: bool = True, help_text: str = None) -> models.BooleanField:
    """
    Создает поле BooleanField
    """
    return models.BooleanField(
        verbose_name=name,
        default=default,
        help_text=help_text,
    )


def phone_number_field(name: str, nullable=False) -> PhoneNumberField:
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
def url_field(name: str, nullable=False) -> models.URLField:
    """
    Создает поле URLField
    """
    nullable = NULLABLE if nullable else {}
    return models.URLField(
        verbose_name=name,
        **nullable,
        max_length=255,
        help_text="Введите ссылку, не более 255 символов",
    )

def decimal_field(name: str, max_digits: int = 10, decimal_places: int = 2) -> models.DecimalField:
    """
    Создает поле DecimalField
    """
    return models.DecimalField(
        verbose_name=name,
        max_digits=max_digits,
        decimal_places=decimal_places
    )