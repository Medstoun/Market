from rest_framework.permissions import BasePermission

from .models import Ad
from users.models import UserRoles


class IsOwnerOrAdmin(BasePermission):
    message = 'Fail access'

    def has_permission(self, request, view):
        try:
            ad = Ad.objects.get(id=view.kwargs['pk'])
        except Ad.DoesNotExist:
            return False

        if request.user.id == ad.author.id:
            return True
        elif request.user.role == UserRoles.ADMIN.value:
            return True
        return False
