from django.db import models
from django.core.validators import RegexValidator
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .utils import docs_path

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
    name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=100,
        verbose_name="Имя",
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    last_name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=100,
        verbose_name="Фамилия",
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    role = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я ]+$")],
        max_length=100,
        verbose_name="Роль в проекте",
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    link = models.ImageField(
        upload_to=docs_path,
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Добавьте фото (необязательно)",
    )

    class Meta:
        verbose_name = "Члена команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.role}"


# class CategoryDocument(Abstract):
#     name = models.CharField(
#         validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я ]+$")],
#         verbose_name="Категория",
#         max_length=20,
#         null=False,
#         help_text="Текст не более 20 символов",
#     )

#     class Meta:
#         verbose_name = "Категорию документов"
#         verbose_name_plural = "Категории документов"

#     def __str__(self):
#         return f"{self.name}"


class Document(Abstract):
    name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я ]+$")],
        verbose_name="Название",
        max_length=100,
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    category = models.CharField(verbose_name="Категория", null=False, choices=CHOISE)
    link = models.FileField(
        verbose_name="Ссылка",
        upload_to=docs_path,
        help_text="Добавьте документ (обязательно)",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Текстовое поле без ограничений"
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return f"{self.name}"


class OrganizationDetail(Abstract):
    name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я ]+$")],
        verbose_name="Название",
        max_length=100,
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    legal_address = models.CharField(
        verbose_name="Юридический адрес",
        max_length=200,
        help_text="Текст не более 200 символов",
    )
    address = models.CharField(
        verbose_name="Физический адрес",
        max_length=200,
        help_text="Текст не более 200 символов",
    )
    # ОГРН ― это код из 13 цифр, разделенных на шесть групп. Пример: 1 21 55 73 93522 0
    ogrn_number = models.CharField(
        validators=[RegexValidator(regex=r"\d{13}")],
        verbose_name="ОГРН",
        max_length=13,
        help_text="Состоит из 13 цифр",
    )
    # Всего у ИНН юридических лиц десять цифр
    inn_number = models.CharField(
        validators=[RegexValidator(regex=r"\d{10}")],
        verbose_name="ИНН",
        max_length=10,
        help_text="Состоит из 10 цифр",
    )
    # КПП состоит из 9 знаков
    kpp_number = models.CharField(
        validators=[RegexValidator(regex=r"\d{9}")],
        verbose_name="КПП",
        max_length=9,
        help_text="Состоит из 9 цифр",
    )
    # номер банковского расчётного счёта представляет собой двадцатизначное число
    current_account = models.CharField(
        validators=[RegexValidator(regex=r"\d{20}")],
        verbose_name="Расчетный счет",
        max_length=20,
        help_text="Состоит из 20 цифр",
    )

    # БИК — это девятизначный уникальный номер, который есть у каждого банковского отделения на территории России.
    bik = models.CharField(
        validators=[RegexValidator(regex=r"\d{9}")],
        verbose_name="БИК",
        max_length=9,
        help_text="Состоит из 9 цифр",
    )
    # В России номера корреспондентских счетов состоят из 20 десятичных разрядов
    correspondent_account = models.CharField(
        validators=[RegexValidator(regex=r"\d{20}")],
        verbose_name="Корр. счет",
        max_length=20,
        help_text="Состоит из 20 цифр",
    )
    director = models.CharField(
        validators=[RegexValidator(regex=r"\D")],
        verbose_name="Директор",
        max_length=100,
        help_text="Текст не более 100 символов (цифры запрещены)",
    )
    link = models.ImageField(
        verbose_name="QR-код банка",
        upload_to=docs_path,
        blank=True,
        help_text="Отправляет на страницу, откуда можно сделать пожертвование на нужды организации (необязательно)",
    )

    class Meta:
        verbose_name = "Реквизиты организации"
        verbose_name_plural = "Реквизиты организации"

    def __str__(self):
        return f"{self.name}"


@receiver(post_delete)
def delete_mediafile_on_delete(instance, **kwargs):
    """
    Удаляет медиафайл из папки при удалении записи в БД
    """
    if instance.link:
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
