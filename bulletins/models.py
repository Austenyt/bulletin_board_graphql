from django.db import models


class Bulletin(models.Model):
    """
    Модель для объявления.

    Атрибуты:
        title (CharField): Название объявления.
        description (TextField): Описание объявления (необязательное поле).
        price (DecimalField): Цена объявления.
        created_at (DateTimeField): Дата и время создания объявления (автоматически устанавливается).
        hashtags (TextField): Хэштеги для объявления, введенные через запятую (необязательное поле).
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Название объявления",
        help_text="Укажите название объявления",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание объявления",
        help_text="Укажите описание объявления",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.TextField(blank=True, default='', help_text="Введите хэштеги через запятую")

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения.

        Преобразует строку хэштегов в формат, который требуется, перед сохранением
        экземпляра модели. Удаляет дублирующиеся символы '#' и сохраняет хэштеги
        в виде строки, разделенной запятыми.

        Аргументы:
            *args: Позиционные аргументы.
            **kwargs: Именованные аргументы.
        """
        # Преобразуем строку хэштегов в формат, который вам нужен, если необходимо
        if isinstance(self.hashtags, str):
            hashtags_list = [tag.strip() for tag in self.hashtags.split(',') if tag.strip()]
            # Удаляем дублирующийся символ '#'
            hashtags_list = [f'#{tag.lstrip("#")}' for tag in hashtags_list]
            self.hashtags = ', '.join(hashtags_list)  # Сохраняем как строку
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращает строковое представление объекта Bulletin.

        Возвращает название объявления, что позволяет удобно отображать
        экземпляры модели в интерфейсах, таких как админка Django.

        Возвращает:
            str: Название объявления.
        """
        return self.title

    class Meta:
        """
        Метаданные модели Bulletin.

        Атрибуты:
            verbose_name (str): Человекочитаемое название модели в единственном числе.
            verbose_name_plural (str): Человекочитаемое название модели во множественном числе.
        """
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
