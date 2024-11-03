# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    cat_name_en = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to="images/categories/%y/%m/%d")
    def __str__(self):
        return self.cat_name_en

class Product(models.Model):
    pr_id = models.AutoField(primary_key=True)
    # pr_id = models.AutoField(primary_key=True, editable=False)
    pr_name = models.CharField(max_length=50)
    pr_name_en = models.CharField(max_length=50)
    pr_image= models.ImageField(upload_to="images/product/%y/%m/%d")
    pr_cost = models.IntegerField()
    pr_detail = models.CharField(max_length=150)
    pr_detail_en = models.CharField(max_length=150)
    cat_fk = models.ForeignKey(Categories, on_delete=models.RESTRICT)
    def __str__(self):
        return self.pr_name_en

# class Users(models.Model):
#     # user_id = models.AutoField(primary_key=True, editable=False)
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=100)
#     user_email = models.CharField(max_length=100)
#     user_verficode = models.IntegerField()
#     user_aprove = models.IntegerField()
#     date_create = models.DateTimeField()
#     user_password = models.CharField(max_length=100)

    # class Meta:
    #     managed = False
    #     db_table = 'users'

class Favorite(models.Model):
    # fav_no = models.AutoField(primary_key=True, editable=False)
    fav_no = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)
    pr_fk = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    quantity=models.IntegerField()
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE)
    pr_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class Coupon(models.Model):
    co=models.AutoField(primary_key=True)
    co=models.CharField(max_length=50)
    co_count=models.IntegerField()
    co_discount=models.IntegerField()
    co_expiredate=models.DateTimeField()


# class MyUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         if not email:
#             raise ValueError('The Email field must be set')

#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)  # تعيين كلمة المرور بشكل آمن
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)

# # نموذج المستخدم المخصص
# class MyUser(AbstractBaseUser):
    # username = models.CharField(max_length=255, unique=True)
    # email = models.EmailField(max_length=255, unique=True)
    # first_name = models.CharField(max_length=255, blank=True, null=True)
    # last_name = models.CharField(max_length=255, blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    # objects = MyUserManager()

    # def __str__(self):
    #     return self.username

    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser

    # def has_module_perms(self, app_label):
    #     return self.is_superuser


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=Users)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=Product)
# def product_created(sender, instance, created, **kwargs):
#     if created:
#         print(f"================================== Product success fully added ===========================.")

# @receiver(post_delete, sender=Product)  # الإشارة مرتبطة بنموذج Product فقط
# def product_deleted(sender, instance, **kwargs):
#     print(f"================================== Product success fully deleted ===========================.")