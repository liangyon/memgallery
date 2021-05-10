from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.


# user models
from django.urls import reverse


class MyUserManager(BaseUserManager):
    """
    manager object, held by users
    """

    def create_user(self, email, username, password=None):
        """
        Creates a User with the given email, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # can create new user using myuser.objects.create_user method, from manager object
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin


# ========================================================


# image models

class ImageModel(models.Model):
    """
    stores an image that directs to user
    """
    img = models.ImageField(upload_to="images/", default='default.jpg')
    img_text = models.CharField(max_length=100)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['img', 'img_text']

    def __str__(self):
        return self.img_text

    def get_absolute_url(self):
        """returns a url for an image
        """
        return reverse('image-detail', args=[str(self.id)])
