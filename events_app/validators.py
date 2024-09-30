import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

# from events_app.models import Registration


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


def validate_comment(value):
    """Проверка допустимых символов в комментарии."""
    # Проверка на допустимые символы: кириллица, латиница, цифры, пробел, спец символы
    if not re.match(r'[a-zA-ZА-Яа-я\s\d.,?!();+=*—«»\-@%$\'\"]+$', value):

        raise ValidationError(_("В комментарии допустимы только кириллица, латиница, цифры, пробел, спец символы."))
    return value
