from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, TextChoices
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# class Role(TextChoices):
#     SHOP_ADMIN = "SHOP_ADMIN", "shop admin"
#     CATEGORY_ADMIN = "CATEGORY_ADMIN", "category admin"
#     PRODUCT_ADMIN = "PRODUCT_ADMIN", "product admin"
#

class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore



    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username, "role": self.role})
