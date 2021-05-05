
from django.db import models

from education.settings import DEFAULT_MAX_LENGTH

from account.models import User


class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.title


class Unit(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH)
    text = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH)

    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(null=True, blank=True, max_length=DEFAULT_MAX_LENGTH)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.title
