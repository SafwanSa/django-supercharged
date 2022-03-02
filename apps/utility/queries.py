from .models import *

def get_config_with(key: str, type: str):
    try:
        value = Config.objects.get(key=key)
        if type.lower() == 'string':
            return value.value
        elif type.lower() == 'boolean':
            return value._boolean
        elif type.lower() == 'int':
            return value._int
        elif type.lower() == 'float':
            return value._float
        else:
            # This should not happen
            raise ValueError('You should pass a valid type.')
    except Config.DoesNotExist:
        # This should not happen
        raise ValueError('The key', key, 'does not have a value.')
