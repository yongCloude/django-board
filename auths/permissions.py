from rest_framwork import permissions


class CustomReadOnly(permissions.BasePermission) :
    """
        GET : Everyone, PUT/PATCH : authenticated only
    """    
    
    def has_object_permission(self, request, view, obj) :
        if request.method in permissions.SAFE_METHODS :
            return True
        return obj.user == request.user