from django.contrib import admin
from .models import Author,BookAuthor,Category,HaveToRead,Publisher
# Register your models here.

class AuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","name"]
    class Meta:
        Model = Author
admin.site.register(Author,AuthorModel)


class BookAuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 15
    class Meta:
        Model = BookAuthor

admin.site.register(BookAuthor,BookAuthorModel)


class CategoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 15
    class Meta:
        Model = Category

admin.site.register(Category,CategoryModel)

class PublisherModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 15
    class Meta:
        Model = Publisher

admin.site.register(Publisher,PublisherModel)


class HaveToReadModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__","details"]
    list_per_page = 10
    list_filter = ["posted_on","category"]
    class Meta:
        Model = HaveToRead
admin.site.register(HaveToRead,HaveToReadModel)

