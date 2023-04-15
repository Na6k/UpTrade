from django.db import models



class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="MenuName")


    class Meta:
        db_table = "menu_name"
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
            return self.name



class MenuItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="ItemName")
    slug = models.SlugField(null=True, unique=True)
    parent = models.ForeignKey("self", verbose_name="ItemBelongs", on_delete=models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, verbose_name="menu_id", null= True, blank= True)

    class Meta:
        db_table = "menu_items"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.name} {self.parent.name if self.parent is not None else None} {self.menu}"    
# Create your models here.