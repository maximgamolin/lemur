from core.models import User
from stock.models import Dataset, DatasetPermissions
from stock.consts import PermissionsType
from market.models import UserPurchases
from market.consts import UserPaymentStatus
from django.db.models import Q


class DatasetUserAccess:

    def __init__(self, user: User):
        self._user = user

    def public_and_free(self):
        return Q(perms__is_public=True, pricing__is_free=True)

    def my(self):
        if self._user.is_anonymous:
            return Q()
        return Q(author=self._user)

    def was_paid(self):
        if self._user.is_anonymous:
            return Q()
        ids = UserPurchases.objects.filter(
            user=self._user, is_active=True, status=UserPaymentStatus.DONE.value
        ).values_list('dataset_id', flat=True)
        return Q(id__in=ids)

    def permitted(self):
        if self._user.is_anonymous:
            return Q()
        ids = DatasetPermissions.objects.filter(
            is_public=False, type=PermissionsType.ONLY.value, users=self._user
        ).values_list('dataset_id', flat=True)
        return Q(id__in=ids)

    def block_permitted(self):
        if self._user.is_anonymous:
            return Q()
        ids = DatasetPermissions.objects.filter(
            is_public=False, type=PermissionsType.EXCLUDE.value, users=self._user
        ).values_list('dataset_id', flat=True)
        return Q(id__in=ids)

    @property
    def available_datasets(self):
        return Dataset.objects\
            .filter(self.public_and_free() | self.my() | self.was_paid() | self.permitted())\
            .exclude(self.block_permitted())
