from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Events(models.Model):

    name_of_event = models.CharField(max_length=500, verbose_name='название мероприятия')
    description_of_event = models.TextField(verbose_name='описание мероприятия')
    address_of_event = models.CharField(max_length=500, verbose_name='адрес проведения мероприятия', **NULLABLE)
    date_time_of_event = models.DateTimeField(verbose_name='время проведения мероприятия', **NULLABLE)

    def __str__(self):
        return self.name_of_event

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'


class EventPhoto(models.Model):

    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to='events/photo/%Y/%m/%d', **NULLABLE)

    def __str__(self):
        return f'Фото для {self.event}'

    class Meta:
        verbose_name = 'фотография мероприятия'
        verbose_name_plural = 'фотографии мероприятия'


class EventVideo(models.Model):

    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='video')
    video = models.FileField(upload_to='events/video/%Y/%m/%d', **NULLABLE)

    def __str__(self):
        return f'Видео для {self.event}'

    class Meta:
        verbose_name = 'видео мероприятия'
        verbose_name_plural = 'видео мероприятия'


class EventLinkVideo(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='link_video')
    link_video = models.TextField(verbose_name='ссылка на видео')
    date = models.DateField(auto_now_add=True, verbose_name='дата добавления', **NULLABLE)

    def __str__(self):
        return f'Ссылка на видео для {self.event}'

    class Meta:
        verbose_name = 'ссылка на видео мероприятия'
        verbose_name_plural = 'ссылки на видео мероприятия'
