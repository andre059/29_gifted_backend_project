from django.db import models
from config.utils import (
    char_field_only_limit_digits,
    char_field_specific_length_without_valid,
    char_field_validator_letters_and_extra,
    image_field,
    char_field_with_choices,
    file_field,
    text_field_specific_length,
    datetime_field, boolean_field
)


CHOISE = {
    "1": "Документы",
    "2": "Отчетность",
    "3": "Уставные документы",
}


class Abstract(models.Model):
    time_create = datetime_field("Создано", auto_now_add=True)
    time_update = datetime_field("Изменено", auto_now=True)
    is_published = boolean_field("Актуально на сайте",
        default=True,
        help_text="Если уже неактуально, но может понадобиться, снимите флажок",
    )

    class Meta:
        abstract = True


class TeamMember(Abstract):
    name = char_field_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = char_field_validator_letters_and_extra("Фамилия", 100, ("-",))
    surname = char_field_validator_letters_and_extra(
        "Отчество", 100, (" ",), nullable=True
    )
    role = char_field_specific_length_without_valid("Роль в проекте", 100)
    link = image_field("Фото", nullable=True)

    class Meta:
        verbose_name = "Члена команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.role}"


class Document(Abstract):
    name = char_field_specific_length_without_valid("Название", 255)
    category = char_field_with_choices("Категория", CHOISE)
    link = file_field("Документ")
    description = text_field_specific_length("Описание", 1000)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return f"{self.name}"


class OrganizationDetail(Abstract):
    name = char_field_specific_length_without_valid("Название", 255)
    legal_address = char_field_specific_length_without_valid("Юридический адрес", 255)
    address = char_field_specific_length_without_valid("Физический адрес", 255)

    ogrn_number = char_field_only_limit_digits("ОГРН", 13)
    inn_number = char_field_only_limit_digits("ИНН", 10)
    kpp_number = char_field_only_limit_digits("КПП", 9)
    current_account = char_field_only_limit_digits("Расчетный счет", 20)
    bik = char_field_only_limit_digits("БИК", 9)
    correspondent_account = char_field_only_limit_digits("Корр. счет", 20)

    director = char_field_validator_letters_and_extra("ФИО директора", 255, ("-", " "))
    link = image_field("QR-код банка", nullable=True)

    class Meta:
        verbose_name = "Реквизиты организации"
        verbose_name_plural = "Реквизиты организации"

    def __str__(self):
        return f"{self.name}"
