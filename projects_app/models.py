from django.core.validators import RegexValidator
from django.db import models


NULLABLE = {'blank': True, 'null': True}


def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return (
        f"{__name__.split('.', maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
    )


class Project(models.Model):
    name = models.CharField(# валидатор только слово из букв, исключая остальные символы
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=50,  # думаю, имя не должно быть длиннее
        verbose_name="Наименование проекта",
        help_text="Только буквы не более 50 символов")
    preview = models.ImageField(upload_to=docs_path, verbose_name='фотография', **NULLABLE)
    content = models.TextField(null=False, blank=True, db_index=True, verbose_name='содержимое')


    @property
    def content_short(self) -> str:
        if len(self.content) < 150:
            return self.content
        return self.content[:150] + '...'


    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
