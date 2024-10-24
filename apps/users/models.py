from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


# Create your models here.

class User(AbstractUser, TimeStampedModel):
    """Default user for TwoScoPoe. The default user type is  common."""

    class Types(models.TextChoices):
        SUPERUSER = "SUPERUSER", "Superuser"
        COMMON = "COMMON", "Common"
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

    base_type = Types.COMMON

    email = models.EmailField(_("email address"), unique=True)
    type = models.CharField(
        _("User Type"), max_length=50, choices=Types.choices, default=base_type
    )
    profile_image = models.ImageField(upload_to='users/profileImages', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = self.Types.SUPERUSER
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)
