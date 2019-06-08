from django.db import models
import pendulum
from abstract.models import FactoryModel, OwnedModel

# Create your models here.

class FriendQuerySet(models.QuerySet):
    def with_overdue(self):
        return self.annotate(
            ann_overdue=models.Case(
                models.When(
                    borrowed__created_at__lte=pendulum.now().subtract(months=2),
                    then=True),
                default=models.Value(False),
                output_field=models.BooleanField()
            )
        )


class Friend(OwnedModel):
    name = models.CharField(max_length=100)
    objects = FriendQuerySet.as_manager()

    @property
    def has_overdue(self):
        if hasattr(self, 'ann_overdue'): # in case we deal with annotated object
            return self.ann_overdue
        return self.borrowed_set.filter(
            returned__isnull=True, when=pendulum.now().subtract(months=2)
        ).exists()


class Belonging(OwnedModel):
    name = models.CharField(max_length=100)


class Borrowed(FactoryModel):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    returned = models.DateTimeField(null=True, blank=True)
