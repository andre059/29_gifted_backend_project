from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from events_app.validators import validate_name_or_surname, validate_no_mixed_scripts, validate_email, validate_phone

NULLABLE = {"blank": True, "null": True}


def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return (
        f"{__name__.split('.', maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
    )


class Event(models.Model):

    name_of_event = models.CharField(
        # возможно, тут достаточно 200
        max_length=300,
        verbose_name="Название мероприятия",
        help_text="Текст не более 300 символов",
    )
    description_of_event = models.TextField(
        verbose_name="Описание мероприятия", help_text="Текст без ограничений"
    )
    address_of_event = models.CharField(
        max_length=500,
        verbose_name="Адрес проведения мероприятия",
        **NULLABLE,
        help_text="Текст не более 500 символов",
    )
    date_time_of_event = models.DateTimeField(
        verbose_name="Дата и время проведения мероприятия", **NULLABLE
    )
    end_of_event = models.DateTimeField(
        verbose_name="Дата и время завершения мероприятия", **NULLABLE
    )

    @property
    def content_short(self) -> str:
        if len(self.description_of_event) < 40:
            return self.description_of_event
        return self.description_of_event[:40] + "..."

    def __str__(self):
        return self.name_of_event

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"


class EventPhoto(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="photo")
    link = models.ImageField(upload_to=docs_path, **NULLABLE)

    def __str__(self):
        return f"Фото для {self.event}"

    class Meta:
        verbose_name = "фотография мероприятия"
        verbose_name_plural = "фотографии мероприятия"


class EventVideo(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="video")
    link = models.FileField(upload_to=docs_path, **NULLABLE)

    def __str__(self):
        return f"Видео для {self.event}"

    class Meta:
        verbose_name = "видео мероприятия"
        verbose_name_plural = "видео мероприятия"


class EventLinkVideo(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="link_video"
    )
    link_video = models.TextField(verbose_name="Ссылка на видео")
    date = models.DateField(
        auto_now_add=True, verbose_name="Дата добавления", **NULLABLE
    )

    def __str__(self):
        return f"Ссылка на видео для {self.event}"

    class Meta:
        verbose_name = "ссылка на видео мероприятия"
        verbose_name_plural = "ссылки на видео мероприятия"


class Registration(models.Model):
    """Модель для записи на мероприятие"""

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations", verbose_name="Мероприятие")

    first_name = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1, _("Имя должно быть не менее 1 символа")),
            MaxLengthValidator(64, _("Имя должно быть не более 64 символов")),
            validate_name_or_surname,
            validate_no_mixed_scripts,
        ],
        verbose_name="Имя",
    )

    last_name = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1, _("Фамилия должна быть не менее 1 символа")),
            MaxLengthValidator(64, _("Фамилия должна быть не более 64 символов")),
            validate_name_or_surname,
            validate_no_mixed_scripts,
        ],
        verbose_name="Фамилия",
    )

    phone = models.CharField(
        max_length=20,
        validators=[
            validate_phone,
        ],
        verbose_name="Телефон",
    )

    email = models.EmailField(
        unique=True,
        validators=[
            MaxLengthValidator(254, _("Email не может быть длиннее 254 символов")),
            validate_email,
        ],
        verbose_name="Электронная почта",
    )

    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время регистрации"
    )

    terms_agreed = models.BooleanField(
        default=False,
        verbose_name="Согласие с условиями"
    )

    def __str__(self):
        return f"Регистрация на {self.event} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Регистрация на мероприятие"
        verbose_name_plural = "Регистрация на мероприятия"


@receiver(post_delete, sender=EventPhoto)
@receiver(post_delete, sender=EventVideo)
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
