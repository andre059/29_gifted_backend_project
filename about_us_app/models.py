from django.db import models
from config.utils import (
    charfield_only_limit_digits,
    charfield_specific_length_without_valid,
    charfield_validator_letters_and_extra,
    imagefield,
    charfield_with_choices,
    filefield,
    textfield_specific_length,
)


# Виды документов
CHOISE = {
    "1": "Документы",
    "2": "Отчетность",
    "3": "Уставные документы",
}


class Abstract(models.Model):
    time_create = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Изменено", auto_now=True)
    is_published = models.BooleanField(
        verbose_name="Актуально на сайте",
        default=True,
        help_text="Если уже неактуально, но может понадобиться, снимите флажок",
    )

    class Meta:
        abstract = True


class TeamMember(Abstract):
    name = charfield_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = charfield_validator_letters_and_extra("Фамилия", 100, ("-",))
    surname = charfield_validator_letters_and_extra(
        "Отчество", 100, (" ",), nullable=True
    )
    role = charfield_specific_length_without_valid("Роль в проекте", 100)
    link = imagefield("Фото", nullable=True)

    class Meta:
        verbose_name = "Члена команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.role}"


class Document(Abstract):
    name = charfield_specific_length_without_valid("Название", 255)
    category = charfield_with_choices("Категория", CHOISE)
    link = filefield("Документ")
    description = textfield_specific_length("Описание", 1000)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return f"{self.name}"


class OrganizationDetail(Abstract):
    name = charfield_specific_length_without_valid("Название", 255)
    legal_address = charfield_specific_length_without_valid("Юридический адрес", 255)
    address = charfield_specific_length_without_valid("Физический адрес", 255)

    # ОГРН ― это код из 13 цифр, разделенных на шесть групп. Пример: 1 21 55 73 93522 0
    ogrn_number = charfield_only_limit_digits("ОГРН", 13)
    # Всего у ИНН юридических лиц десять цифр
    inn_number = charfield_only_limit_digits("ИНН", 10)
    # КПП состоит из 9 знаков
    kpp_number = charfield_only_limit_digits("КПП", 9)
    # номер банковского расчётного счёта представляет собой двадцатизначное число
    current_account = charfield_only_limit_digits("Расчетный счет", 20)
    # БИК — это девятизначный уникальный номер, который есть у каждого банковского отделения на территории России.
    bik = charfield_only_limit_digits("БИК", 9)
    # В России номера корреспондентских счетов состоят из 20 десятичных разрядов
    correspondent_account = charfield_only_limit_digits("Корр. счет", 20)

    director = charfield_validator_letters_and_extra("ФИО директора", 255, ("-", " "))
    link = imagefield("QR-код банка", nullable=True)

    class Meta:
        verbose_name = "Реквизиты организации"
        verbose_name_plural = "Реквизиты организации"

    def __str__(self):
        return f"{self.name}"
