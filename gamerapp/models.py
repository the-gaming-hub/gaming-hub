from django.db import models
from django.utils.text import slugify

# Create your models here.

class AffiliateProduct(models.Model):
    name = models.CharField(max_length=128)
    model = models.CharField(max_length=64)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL, null = True)
    image = models.ImageField(upload_to='images/')
    review = models.CharField(max_length=2048)
    main_link = models.URLField(max_length=128 , null = True, blank=True)
    amazon_link = models.URLField(max_length=128 , null = True, blank=True)
    slug = models.SlugField(blank = True , null = True)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(AffiliateProduct , self).save(*args , **kwargs)
    
    def __str__(self):
        return str(self.name)+'-'+str(self.model)
    
    
class Type(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank = True , null = True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Type , self).save(*args , **kwargs)

    def __str__(self):
        return self.name 


    
class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank = True , null = True)
    
    
    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category , self).save(*args , **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
class Sub_Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank = True , null = True)
    
    
    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Sub_Category , self).save(*args , **kwargs)
    
    def __str__(self):
        return self.name
    
class Sub_SubCategory(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank = True , null = True)
    
    
    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Sub_Category , self).save(*args , **kwargs)
    
    def __str__(self):
        return self.name
    
    
    
class Review(models.Model):
    topic = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/')
    main_category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null = True)
    sub_category = models.ForeignKey('Sub_Category' , on_delete=models.SET_NULL , null = True)
    sub_subcategory = models.ForeignKey('Sub_SubCategory' , on_delete=models.SET_NULL , null = True, blank=True)
    intro = models.CharField(max_length=256 , null = True)
    slug = models.SlugField(blank = True , null = True)
    date_created = models.DateTimeField(auto_now=True)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.topic)
        super(Review , self).save(*args , **kwargs)
    
    def __str__(self):
        return self.topic