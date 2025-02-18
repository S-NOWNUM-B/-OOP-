from functools import wraps


class authorize:
    def __init__(self, role):
        self.role = role

    def __call__(self, cls):
        class Wrapped(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.role = self.__class__.role

        Wrapped.role = self.role
        return Wrapped


def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not hasattr(self, 'role'):
                raise AttributeError("Пользователь не имеет атрибута 'role'")
            if self.role != required_role:
                raise PermissionError(f"Доступ запрещён! Требуется роль: {required_role}")
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


@authorize("admin")
class AdminUser:
    @require_role("admin")
    def delete_user(self):
        return "Пользователь удалён"


admin = AdminUser()
print(admin.delete_user())  # Работает


@authorize("user")
class RegularUser:
    @require_role("admin")
    def delete_user(self):
        return "Пользователь удалён"


user = RegularUser()
print(user.delete_user())