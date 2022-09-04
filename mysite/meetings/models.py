from django.db import models
from django.urls import reverse


class People(models.Model):
    person_gender = models.CharField(max_length=10, verbose_name='Пол')
    person_firstname = models.CharField(max_length=50, verbose_name='Имя', blank=True)
    person_lastname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True)
    person_shortname = models.CharField(max_length=50, verbose_name='Короткое имя')
    person_email_adress = models.EmailField(verbose_name='Электронный адрес', blank=True)
    person_phone_number = models.CharField(max_length=12, verbose_name='Номер телефона', blank=True)
    person_information = models.CharField(max_length=500, verbose_name='Обо мне', blank=True)
    person_interests = models.CharField(max_length=500, verbose_name='Хобби', blank=True)
    person_found = models.CharField(max_length=10, verbose_name='Кого ищу')
    person_photo = models.ImageField(upload_to='photos/%Y/&m/%d/', verbose_name='Фото', blank=True)

    def get_absolute_url(self):
        return reverse('view_people', kwargs={"pk": self.pk})

    def __str__(self):
        return self.person_shortname
