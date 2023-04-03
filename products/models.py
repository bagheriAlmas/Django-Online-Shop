from django.db import models
from django.template.defaultfilters import slugify


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/categories', default='category_default.png')
    highlight = models.BooleanField(default=False)
    is_enable = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, default="slug", editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        else:
            return self.title

    def save(self, *args, **kwargs):
        if self.parent:
            self.slug = slugify(self.parent.title + "-" + self.title)
        else:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)


class Specification(models.Model):
    title = models.CharField(max_length=50)
    is_enable = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True, default="slug", editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Specification, self).save(*args, **kwargs)


class Product(models.Model):
    PRODUCT_RATE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField()
    colors = models.CharField(max_length=30, null=True, blank=True)
    specification = models.ManyToManyField(Specification)
    rate = models.CharField(max_length=5, choices=PRODUCT_RATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="")
    price = models.FloatField()
    sizes = models.ManyToManyField(Size, blank=True)
    slug = models.SlugField(max_length=200, unique=True, default="slug", editable=False)

    def __str__(self):
        return self.name + " -> " + self.brand

    @property
    def image_upload_path(self):
        return f'{self.category.title}/{self.brand}/{self.name}/'

    def save(self, *args, **kwargs):
        self.image.upload_to = self.image_upload_path
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class File(models.Model):
    product = models.ForeignKey('Product', related_name='Files', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='products/files/%y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='products/banners/')
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
