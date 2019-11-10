from django.contrib import admin
from .models import Author

class AuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","name"]
    class Meta:
        Model = Author
admin.site.register(Author,AuthorModel)