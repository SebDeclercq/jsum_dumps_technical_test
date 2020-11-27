from collections.abc import Iterable

def convert_special_object(obj):
    """ Convert objects such as None, True and False
    to their string values: null, true and false.
    """

    if obj is None:
        return "null"
    elif obj is True:
        return "true"
    elif obj is False:
        return "false"

def is_special_object(obj):
    """Is an object None, True or False"""
    return any([(obj is None), (obj is True), (obj is False)])

def json_dumps(obj, nested=False):
    """Dump recursively an object into is string representation.

    json_dumps(1)
    >>> '1'

    json_dumps([1, 2])
    >>> "['1', '2']"

    json_dumps([1, {2: True}])
    >>> "['1', {'2': 'true'}]"
    """
    if isinstance(obj, Iterable) and (not isinstance(obj, str)):
        if isinstance(obj, list):
            return str(manage_list(obj)) if not nested else manage_list(obj)
        if isinstance(obj, dict):
            return str(manage_dict(obj)) if not nested else manage_dict(obj)
    elif is_special_object(obj):
        return convert_special_object(obj)
    return str(obj)


def manage_list(obj):
    """Turn a list info his string representation."""
    copy_obj = []

    for elem in obj:
        # If the list is nested
        if isinstance(elem, Iterable):
            copy_obj.append(json_dumps(elem, nested=True))
        elif is_special_object(elem):
            copy_obj.append(convert_special_object(elem))
        else:
            copy_obj.append(str(elem))

    return copy_obj

def manage_dict(obj):
    """Turn a dict into his string representation."""
    copy_obj = {}

    for key, value in obj.items():
        # If the dict is nested
        if isinstance(value, Iterable):
            copy_obj.update({str(key): json_dumps(value, nested=True)})
        else:
            if is_special_object(key):
                key = convert_special_object(key)
            if is_special_object(value):
                value = convert_special_object(value)

            copy_obj.update({str(key): str(value)})

    return copy_obj