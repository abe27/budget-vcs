from django.db import models


# Create your models here.
class ProductType(models.Model):
    # FcCode = models.CharField(max_length=1, db_column="FCCODE", verbose_name="FCCODE")
    #
    # def __str__(self) -> str:
    #     return f"{self.FcCode}"

    class Meta:
        db_table = "PRODTYPE"
        app_label = "formulavcst"
        verbose_name = "ข้อมูล Product Type"
        verbose_name_plural = "Product Type"
