from django.db import models

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')

    class Meta:
        db_table = 'restaurant_store_category'
        verbose_name = 'store category'
        verbose_name_plural ='store categories'
        ordering = ['-id']

    def __str__(self):
        return self.name
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(StoreCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store')
    tagline = models.CharField(max_length=225)
    amount = models.FloatField()
    time = models.IntegerField()

    class Meta:
        db_table = 'restaurant_store'
        verbose_name = 'store'
        verbose_name_plural ='stores'
        ordering = ['-id']

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')
    store = models.ForeignKey(Store,on_delete=models.CASCADE)


    class Meta:
        db_table = 'restaurant_slider'
        verbose_name = 'slider'
        verbose_name_plural ='slider'
        ordering = ['-id']

    def __str__(self):
        return self.name
    


class Food_Category(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)


    

    class Meta:
        db_table = 'restaurant_food_category'
        verbose_name = 'food_category'
        verbose_name_plural ='food_category'
        ordering = ['-id']

    def __str__(self):
        return self.name

class Foods(models.Model):
    is_veg = models.BooleanField(default=False)
    food_name = models.CharField(max_length=100)
    amount = models.FloatField()
    image = models.ImageField(upload_to='foods')
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    food_category = models.ForeignKey(Food_Category,on_delete=models.CASCADE)

        

    class Meta:
        db_table = 'restaurant_foods'
        verbose_name = 'foods'
        verbose_name_plural ='foods'
        ordering = ['-id']

    def __str__(self):
        return self.food_name