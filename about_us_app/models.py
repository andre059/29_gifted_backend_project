from django.db import models

class TeamMember(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фотография")
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    role = models.CharField(max_length=100, verbose_name="Роль в проекте")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.role}"
