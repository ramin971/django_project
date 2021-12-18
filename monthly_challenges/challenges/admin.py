from django.contrib import admin
from .models import Book,Author,Address,Country
# Register your models here.
#
# class PublishedInline(admin.TabularInline):
#     model = Book.published_countries.through

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('author','rating')
    list_display = ('title','rating','author','is_bestselling')
    # inlines = [PublishedInline]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address')
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)