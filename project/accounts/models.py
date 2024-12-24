from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)  
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("Name:"), max_length=50)
    number_phone    = models.CharField(_(" phone number"), max_length=50)
    address         = models.CharField(_("المحافظه"), max_length=30)
    address_detail  = models.CharField(_("العنوان بالتفصيل"), max_length=25)
    working_hours   = models.CharField(_("عدد ساعات العمل"), max_length=50)
    
    doctor          = models.CharField(_("دكتور ؟"),max_length=50,blank=True, null=True)
    Specialist_doctor = models.CharField(_("متخصص فى ؟"), max_length=50,blank=True, null=True)
    price = models.IntegerField(_("سعر الكشف"), blank=True, null=True)
    who_i = models.TextField(_("Who I am:"), max_length=250)
    price = models.IntegerField(_("Price:"), blank=True, null=True)
    image = models.ImageField(_("Profile Image"), blank=True, null=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' % (self.name)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)