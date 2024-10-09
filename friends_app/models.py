from django.db import models
from django.core.validators import RegexValidator
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .utils import docs_path

GENDER = {
    "male": "Мужской",
    "female": "Женский",
}


class Abstract(models.Model):
    time_create = models.DateTimeField(
        verbose_name="Создано",
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        verbose_name="Изменено",
        auto_now=True,
    )
    is_published = models.BooleanField(
        verbose_name="Актуально на сайте",
        default=True,
        help_text="Если уже неактуально, но может понадобиться, снимите флажок",
    )

    class Meta:
        abstract = True


class Friend(Abstract):
    name = models.CharField(
        # валидатор только слово из букв и "-", исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я-]+$")],
        max_length=100,
        verbose_name="Имя",
        help_text="Только буквы и '-' не более 100 символов",
    )
    last_name = models.CharField(
        # валидатор только слово из букв и "-", исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я-]+$")],
        max_length=100,
        verbose_name="Фамилия",
        help_text="Только буквы и '-' не более 100 символов",
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
        verbose_name="Пол",
        help_text="Выберите пол",
        default="male",
    )
    description = models.TextField(
        verbose_name="Роль в проекте",
        help_text="Текст, не более 300 символов",
        max_length=300,
    )
    link = models.ImageField(
        upload_to=docs_path,
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Добавьте фото (необязательно)",
    )

    class Meta:
        verbose_name = "Человека"
        verbose_name_plural = "Люди"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Company(Abstract):
    name = models.CharField(
        # валидация не нужна, в имени компании могут быть и цифры и другие знаки
        verbose_name="Название",
        max_length=300,
        help_text="Текст не более 300 символов",
    )
    link = models.ImageField(
        upload_to=docs_path,
        blank=True,
        null=True,
        verbose_name="Логотип",
        help_text="Добавьте логотип (необязательно)",
    )
    description = models.TextField(
        verbose_name="Чем была полезна:",
        help_text="Текст, не более 300 символов",
        max_length=300,
    )

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"


class Volunteer(models.Model):
    name = models.CharField(
        # валидатор только слово из букв и "-", исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я-]+$")],
        max_length=100,
        verbose_name="Имя",
        help_text="Только буквы и '-' не более 100 символов",
    )
    last_name = models.CharField(
        # валидатор только слово из букв и "-", исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я-]+$")],
        max_length=100,
        verbose_name="Фамилия",
        help_text="Только буквы и '-' не более 100 символов",
    )
    email = models.EmailField(
        verbose_name="email",
        help_text="Введите email: example@mail.com",
        max_length=254,
    )
    link = models.ImageField(
        upload_to=docs_path,
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Добавьте фото (необязательно)",
    )
    is_accept = models.BooleanField(
        verbose_name="Принято пользовательское соглашение",
        default=True,
    )

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"

    def __str__(self):
        return f"{self.name}"


@receiver(post_delete, sender=Friend)
@receiver(post_delete, sender=Company)
@receiver(post_delete, sender=Volunteer)
def delete_mediafile_on_delete(sender, instance, **kwargs):
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
