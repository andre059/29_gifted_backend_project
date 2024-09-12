import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models import Model
from django.utils.translation import gettext as _


def validate_no_mixed_scripts(value):
    """Проверка, что в строке не используется одновременно кириллица и латиница."""
    if re.search(r'[А-Яа-я]', value) and re.search(r'[a-zA-Z]', value):
        raise ValidationError(_("Нельзя использовать кириллицу и латиницу одновременно"))
    return value


def validate_name_or_surname(value):
    """Проверка имени или фамилии: допускается кириллица, латиница, пробел и тире."""
    return RegexValidator(
        regex=r'^[A-Za-zА-Яа-я\- ]+$',
        message=_("Имя может содержать только кириллицу, латиницу, пробел и тире")
    )(value)


def validate_number_of_spaces_or_dashes(value):
    """Проверка имени или фамилии: не более 2-х пробелов или тире подряд."""
    if re.search(r'[\s\-]{3}', value):
        raise ValidationError("Нельзя использовать больше 2-х пробелов или тире подряд.")
    return value


def validate_email(value):
    """Проверка формата email."""
    return RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message=_("Некорректный email адрес")
    )(value)


def validate_phone(value):
    """Проверка формата телефона."""
    return RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Введите корректный номер телефона")
    )(value)


# def validate_unique_comment(value):
#     """Проверка уникальности комментария в рамках модели Registration."""
#     if not isinstance(value, Model):
#         raise ValidationError(_("Комментарий уже существует."))
#
#     registration = value
#     if registration.pk is None:
#         # Если комментарий создается, проверка не нужна
#         if not registration.comment or registration.comment.strip() == '':
#             raise ValidationError(_("Комментарий не может быть пустым."))
#
#     # Проверяем, есть ли уже такой же комментарий в модели
#     existing_comments = registration.__class__.objects.exclude(pk=registration.pk).filter(comment=value.comment)
#     if existing_comments.exists():
#         raise ValidationError(_("Комментарий уже существует."))
#
#     return value

def validate_unique_comment(value):
    """Проверка уникальности комментария в рамках модели Registration."""
    # if not isinstance(value, Model):
    #     raise ValidationError(_("Неверный тип данных для комментария."))

    registration = value
    if registration.pk is None:
        # Если это новый объект, проверяем только, что комментарий не пустой
        if not registration.comment or registration.comment.strip() == '':
            raise ValidationError(_("Комментарий не может быть пустым."))

    # Проверяем, есть ли уже такой же комментарий в модели
    existing_comments = registration.__class__.objects.exclude(pk=registration.pk).filter(
        comment__iregex=r'^' + registration.comment.replace(' ', '') + '$'
    )
    if existing_comments.exists():
        raise ValidationError(_("Комментарий уже существует."))

    return value
