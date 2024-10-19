from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from config.utils import char_field_specific_length_without_valid, char_field_address_specific_length_with_nullability, \
    text_field_specific_length, datetime_field_with_nullability, char_field_length_validation, email_field_validation, \
    text_field_validation, datetime_field, boolean_field, phone_number_field, image_field, file_field, url_field



class Event(models.Model):

    name_of_event = char_field_specific_length_without_valid("Название мероприятия", 300,)
    description_of_event = text_field_specific_length("Описание мероприятия", 2000)
    address_of_event = char_field_address_specific_length_with_nullability("Адрес проведения мероприятия", 500,)
    date_time_of_event = datetime_field_with_nullability("Дата и время проведения мероприятия",)
    end_of_event = datetime_field_with_nullability("Дата и время завершения мероприятия")

    @property
    def event_description(self):
        return self._description_of_event

    @event_description.setter
    def event_description(self, value):
        self._description_of_event = value

    @property
    def content_short(self) -> str:
        if len(self.event_description) < 40:
            return self.event_description
        return self.event_description[:40] + "..."

    def __str__(self):
        return self.name_of_event

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"


class EventPhoto(models.Model):

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="photo",
        )
    link = image_field("Фото мероприятия", nullable=True)

    def __str__(self):
        return f"Фото для {self.event}"

    class Meta:
        verbose_name = "фотография мероприятия"
        verbose_name_plural = "фотографии мероприятия"


class EventVideo(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="video")
    link = file_field("Видео мероприятия", nullable=True)

    def __str__(self):
        return f"Видео для {self.event}"

    class Meta:
        verbose_name = "видео мероприятия"
        verbose_name_plural = "видео мероприятия"


class EventLinkVideo(models.Model):

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="link_video"
    )
    link_video = url_field("Ссылка на видео")

    def __str__(self):
        return f"Ссылка на видео для {self.event}"

    class Meta:
        verbose_name = "ссылка на видео мероприятия"
        verbose_name_plural = "ссылки на видео мероприятия"


class Registration(models.Model):
    """Модель для записи на мероприятие"""

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, 
        related_name="registrations", verbose_name="Мероприятие",
        )
    first_name = char_field_length_validation("Имя", 64)
    last_name = char_field_length_validation("Фамилия", 64)
    phone = phone_number_field('Телефон')
    email = email_field_validation("Электронная почта")
    comment = text_field_validation("Комментарий", )
    timestamp = datetime_field("Дата и время регистрации", auto_now_add=True,)
    terms_agreed = boolean_field("Согласие с условиями")

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
