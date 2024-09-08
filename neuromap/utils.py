
def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_admin or user.is_superuser)