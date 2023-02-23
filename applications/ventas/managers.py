from django.db import models


class ProductManager(models.Manager):

    def get_products(self, kword, categoria):
        if len(categoria) > 0:
            return self.filter(category__category = categoria, product__icontains=kword, public = True)
        else:
            return self.filter(product__icontains=kword)


class CategoryManager(models.Manager):
    
    def get_category_product(self):

        return self.all()