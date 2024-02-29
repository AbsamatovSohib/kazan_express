# from rest_framework import permissions
#
#
# class HasRolePermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         required_roles = getattr(view, 'required_roles', [])
#         if request.user.role.filter(name__in=required_roles).exists():
#            return True
#         return False

#
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.category.shop.owner:
#             return True
#         return False
