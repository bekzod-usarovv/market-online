
from django.db import models
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Davlat'
        verbose_name_plural = 'Davlatlar'

    def __str__(self):
        return self.name


class Manufactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nomi')
    description = models.TextField()
    country = models.ForeignKey('Country' on_delete=models.PROTECT,
                                verbose_name='Ishlab chiqarilgan')


    class Meta:
        verbose_name = 'Ishlab chiqarilgan Zavod'
        verbose_name_plural = 'Ishlab chiqarilgan Zavodlar'

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('Category',
                               verbose_name='Ota kategoriya', on_delete=models.PROTECT)
    name = models.CharField(max_length=264, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Categoriya'
        verbose_name_plural = 'Categiriyalar'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Kategoriya', null=True)
    manufactory = models.ForeignKey(Manufactory, on_delete=models.PROTECT, related_name='manufactory',
                                    verbose_name='Ishlab chiqarilgan Korxona', null=True)
    conutry = models.ForeignKey(Country, on_delete=models.PROTECT,
                                verbose_name='Ishlab chiqarilgan Davlatlar', null=True)
    sale_count = models.DecimalField(max_digits=17, decimal_places=2, default=0,
                                     verbose_name='Skidka narxi', null=True)
    view_count = models.PositiveBigIntegerField(default=0,
                                                verbose_name='Ko\'rganlar soni', null=True)
    is_active = models.BooleanField(default=True,
                                    verbose_name='Holat active', null=True)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.name


class Charactory(models.Model):
    name = models.CharField(max_length=264, verbose_name='Nome')

    class Meta:
        verbose_name='Xil (xususiyati)'



class ProductMedi(models.Model):
    product = models.ForeignKey(Product, models.PROTECT, verbose_name='productmedia', related_name='jhh')
    media = models.FileField(upload_to='product/media', verbose_name='Video/Rasm')






































# class Category(models.Model):
#     parent = models.ForeignKey("Category", verbose_name="Otasi", on_delete=models.CASCADE,
#                                null=True, blank=True, related_name="childes")
#     name = models.CharField(verbose_name="Nomi", max_length=255)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Categoriya"
#         verbose_name_plural = "Categiriyalar"


# class Product(models.Model):
#     category = models.ForeignKey("Category", verbose_name="Kategoriyasi",
#                                  on_delete=models.PROTECT, related_name="products")
#     name = models.CharField(verbose_name="Nomi", max_length=255)
#     full_name = models.CharField(max_length=255, verbose_name="To'liq nomi", null=True)
#     price = models.DecimalField(verbose_name="Narxi", max_digits=17, decimal_places=2, null=True)
#     description = models.TextField(verbose_name="Masulot haqida ma'lumot")

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Maxsulot"
#         verbose_name_plural = "Maxsulotlar"
