from django.contrib import admin
from .models import Product, Category, Size, File, Specification,Banner


# Register your models here.


class FileAdminInline(admin.TabularInline):
    model = File
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [FileAdminInline, ]
    filter_horizontal = ('sizes', 'specification')


admin.site.register(Size)
admin.site.register(Product, ProductAdmin)


class ParentCategoryFilter(admin.SimpleListFilter):
    title = 'Parent Category'
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        categories = Category.objects.filter(parent__isnull=True)
        return [(c.id, str(c)) for c in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent_id=self.value())
        else:
            return queryset


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_filter = (ParentCategoryFilter,)
    search_fields = ('parent__title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Specification)
admin.site.register(Banner)
