from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    自定义权限：管理员用户可以进行写操作，其他认证用户只能进行读操作。
    """

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        # 如果是读操作（GET、HEAD、OPTIONS），则允许所有认证用户访问
        if request.method in SAFE_METHODS:
            return True

        # 对于写操作，只有管理员用户才允许访问
        return request.user and request.user.is_staff
