from django.contrib import admin
from .models import Shop,Product, Category
from rest_framework import permissions
# from django.http import HttpResponse


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "id", )
    list_display_links = ("id", "title")
    list_per_page = 10

    search_fields = ("title", "id")
    readonly_fields = ("id", )

    actions = ("mske_perfect", )

    def make_perfect(self, request, queryset):
        queryset.update(description="It will be perfect shop")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "shop", )
    list_filter = ("shop", "id")
    list_select_related = ("shop", )
    list_per_page = 10

    search_fields = ("title", "shop")
    readonly_fields = ("shop", "id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "amount")
    list_filter = ("amount", "price", )
    list_per_page = 10
    list_select_related = ("category", )

    autocomplete_fields = ("category", )

    search_fields = ("title", "price","description")
    readonly_fields = ("category", )

    actions = ("make_hundred",)

    def make_hundred(self, request, queryset):
        queryset.update(amount=100)


class HasRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_roles = getattr(view, 'required_roles', [])
        if request.user.role.filter(name__in=required_roles).exists():
           return True
        return False




















# rasm joylashtirish
    # def headshot_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #     )
    #     )

        #it is necessary
    # def children_display(self, obj):
    #     return ", ".join([
    #         child.name for child in obj.shop.all()
    #     ])



# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


#change admin header
# admin.site.site_header = "Sakhib Admin panel"
# admin.site.index_title = "Admin settings"


# @admin.register(Product)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = (Product, )

import csv


# class ProductAdmin(admin.TabularInline):
#     model = Product




# @admin.register(Category)
# class CategoryInline(admin.ModelAdmin):
    # inlines = [ProductAdmin]


# admin.site.register(Product)
# admin.site.register(ProductAdmin)



# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("title", "active", "category")
#     list_filter = ("category", "amount")
#     list_per_page = 10
#
#     search_fields = ("price", "title")
#
#     actions = ("make_true", "export_as_csv")
#     list_select_related = ("category", )

    # list_filter = ("price")
    # list_display_links = ("price",)
    # def get_queryset(self, request


#it is update queryset fields
    # def make_true(self, request, queryset):
    #     queryset.update(price=1)
    #     self.message_user(request, f'{rows_updated} products were successfully marked as active.')
    # make_true.short_description = "Mark selected products as active"


#export csv files from django
    # def export_as_csv(self, request, queryset):
    #     meta = self.model._meta
    #     field_names = [field.name for field in meta.fields]
    #
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    #     writer = csv.writer(response)
    #
    #     writer.writerow(field_names)
    #     for obj in queryset:
    #         row = writer.writerow([getattr(obj, field) for field in field_names])
    #
    #     return response


#writing permissions
    # def has_add_permission(self, request):
    #     return request.user.is_staff
    #
    # def has_change_permission(self, request, obj=None):
    #     safe_methods = ("PUT", "PATCH")
    #         if request.method in safe_methods:
    #             return  True


 # IN Order to delete action
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'make_true' in actions:
    #         del actions['make_true']
    #     return actions

#very nice operation

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Shop)
# admin.site.register(Category)


