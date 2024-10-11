from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

def validate_phone(value):
    """Проверка формата телефона."""
    return RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Введите корректный номер телефона")
    )(value)
