from django.db import models

NULLABLE = {"blank": True, "null": True}


class Link(models.Model):
    LEVEL = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Укажите название"
    )
    email = models.EmailField(
        max_length=100,
        verbose_name="Почта",
        help_text="Укажите email"
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Укажите страну"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Укажите город"
    )
    street = models.CharField(
        max_length=100,
        verbose_name="Улица",
        help_text="Укажите улицу"
    )
    house_number = models.CharField(
        max_length=10,
        verbose_name="Номер дома",
        help_text="Укажите номер дома"
    )
    level = models.PositiveIntegerField(
        choices=LEVEL,
        verbose_name="Уровень сети",
        default=0
    )
    supplier = models.ForeignKey(
        'self',
        verbose_name="Поставщик",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название продукта",
        help_text="Укажите название продукта"
    )
    product_model = models.CharField(
        max_length=255,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта"
    )
    release_date = models.DateField(
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок"
    )
    supplier = models.ForeignKey(
        'Link',
        verbose_name="Поставщик",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (f"{self.name} - {self.product_model}"
                f"Поставщик - {self.supplier}")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
