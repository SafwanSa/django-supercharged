import os
import uuid
import jwt
from datetime import datetime, timedelta
import math
import random
from django.urls import reverse
from django.utils.html import format_html



class RandomFileName(object):
    """
        Random file names for user generated contents
    """

    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)



class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4(), ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)



def generate_token(user_id) -> str:
    payload = {
        "token_type": "verify",
        "exp": (datetime.now() + timedelta(hours=48)).timestamp(),
        "user_id": user_id
    }
    return jwt.encode(payload, "djsaf", algorithm="HS256")



def generate_otp() -> str:
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def to_list(string: str) -> list:
    return string.replace(
        '[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')


def to_string(_list: list) -> str:
    return '[' + ','.join(_list) + ']'


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """
    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


def general_linkify(obj):
    linked_obj = obj
    if linked_obj is None:
        return '-'
    app_label = linked_obj._meta.app_label
    model_name = linked_obj._meta.model_name
    view_name = f'admin:{app_label}_{model_name}_change'
    link_url = reverse(view_name, args=[linked_obj.pk])
    return format_html('<a href="{}">{}</a>', link_url, linked_obj)