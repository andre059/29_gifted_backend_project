from django.db import models
from django.core.validators import RegexValidator
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

NULLABLE = {"blank": True, "null": True}


# def feedback_preview_path(filename: str) -> str:
#     """Функция для создания кастомной папки сохранения изображений"""
#     return f"preview/feedback/{filename}"


def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return (
        f"{__name__.split('.', maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
    )


class Feedback(models.Model):
    name = models.CharField(
        # валидатор только слово из букв, исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=50,  # думаю, имя не должно быть длиннее
        verbose_name="Имя",
        help_text="Только буквы не более 50 символов",
    )
    lastname = models.CharField(
        # валидатор только слово из букв, исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=50,  # думаю, фамилия не должна быть длиннее
        verbose_name="Фамилия",
        help_text="Только буквы не более 50 символов",
    )
    # отчество не требуется по ТЗ
    # surname  = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    preview = models.ImageField(
        upload_to=docs_path, verbose_name="Фотография", **NULLABLE
    )
    # может быть для date_create все же надо "blank": False ??? и auto_now_add=True ???
    date_create = models.DateTimeField(verbose_name="Дата создания", **NULLABLE)
    content = models.TextField(
        null=False,
        blank=True,
        db_index=True,
        verbose_name="Содержимое",
        help_text="Текст без ограничений",
    )

    @property
    def content_short(self) -> str:
        if len(self.content) < 40:
            return self.content
        return self.content[:40] + "..."

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


@receiver(post_delete, sender=Feedback)
def delete_mediafile_on_delete(sender, instance, **kwargs):
    """
    Удаляет медиафайл из папки при удалении записи в БД
    """
    # print(instance.link)
    if instance.preview:
        # Получаем путь ссылки
        link_path = instance.preview.path
        # Проверяем, существует ли файл по указанному пути
        if os.path.isfile(link_path):
            try:
                os.remove(link_path)
                return f"Файл {link_path} успешно удален"
            except Exception as e:
                return f"Ошибка при удалении файла {link_path}: {e}"
        else:
            return f"Файл {link_path} не найден"
