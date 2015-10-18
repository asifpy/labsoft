from functools import wraps

from labsoft.core.utils.loggedinuser import LoggedInUser


def add_created_user(f):
    '''Decorate pre_save signal for adding created user'''

    @wraps(f)
    def wrapper(sender, instance, **kwargs):
        if not instance:
            setattr(instance, 'created_by', LoggedInUser().current_user)
        return f(sender, instance, **kwargs)
    return wrapper


def add_updated_user(f):
    '''Decorate pre_save signal for adding updated user'''
    @wraps(f)
    def wrapper(sender, instance, **kwargs):
        setattr(instance, 'updated_by', LoggedInUser().current_user)
        return f(sender, instance, **kwargs)
    return wrapper
