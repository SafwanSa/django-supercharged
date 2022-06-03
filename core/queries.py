from .models import *
from django.db.models import Q
from typing import Iterable
from core.errors import Error, APIError
from core.models import BaseModel


class BaseQuery:

    @staticmethod
    def get_instance_by_id(model: BaseModel, id: int, with_deleted=False) -> BaseModel:
        try:
            if with_deleted:
                return model.objects_with_deleted.get(id=id)
            else:
                return model.objects.get(id=id)
        except model.DoesNotExist:
            raise APIError(Error.INSTANCE_NOT_FOUND, extra=[model._meta.object_name])

    @staticmethod
    def get_all_instances(model: BaseModel, with_deleted=False) -> Iterable[BaseModel]:
        if with_deleted:
            return model.objects_with_deleted.all()
        return model.objects.all()
