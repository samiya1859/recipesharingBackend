from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.category

class RecipeModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ingredients = models.TextField()
    procedure = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe/images')

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    commentor = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES,max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.commentor.username} :  {self.recipe.title}"

