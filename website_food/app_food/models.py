from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate =  models.FloatField()

    class Meta:
        ordering = ["food_name"]

    def __str__(self):
        return self.food_name

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.TextField()
    foodrecipe_ingredients = models.ManyToManyField(Food)

    class Meta:
        ordering = ["recipe_name"]

    def __str__(self):
        return self.recipe_name


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_description = models.CharField(max_length=200)
    userfood_fridge = models.ManyToManyField(Food)
    #userfood_shoppinglist = models.ManyToManyField(Food)
    userrecipe_savedrecipes = models.ManyToManyField(Recipes)

    class Meta:
        ordering = ["user_name"]

    def __str__(self):
        return self.user_name