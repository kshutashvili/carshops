# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Почта должна быть заполнена."))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)



DROPSHIPPING_CHOICES = (
    ('1','Только дропшиппинг'),
    ('2','Иногда планирую'),
    ('3','Нет'))

class User(AbstractUser):
    username = ''
    first_name = models.CharField(_("Имя"),
                                  max_length=64)
    last_name = models.CharField(_("Фамилия"),
                                 max_length=64)
    email = models.EmailField(_("Электронная почта"),
                              unique=True)
    phone_regex = RegexValidator(regex=r'^\+{0,1}\d{9,15}$',
                                 message=_("Номер может быть введён в одном из форматов: "
                                          "+380111111111, 380111111111, "
                                          "80111111111, 0111111111"))
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=16,
                                    unique=True)
    site = models.CharField(_("Сайт"),
                            max_length=128,
                            null=True,
                            blank=True)
    information = models.TextField(_("Информация о деятельности"),
                                   null=True,
                                   blank=True)
    dropshipp = models.CharField(_("Система дропшиппинг"),
                                 choices=DROPSHIPPING_CHOICES,
                                 max_length=32,
                                 null=True,
                                 blank=True)
    is_active = models.BooleanField(_("Активированный"),
                                    default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __unicode__(self):
        return self.email



