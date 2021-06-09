from django.db import models

from core.models import Course, Answer

from account.models import User


class CourseListener(models.Model):
    course = models.ForeignKey(Course, related_name='listeners', on_delete=models.CASCADE)
    listener = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.user} | {self.course}'

    class Meta:
        unique_together = ('course', 'listener')


class ListenerAnswer(models.Model):
    listener = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.listener} answered {self.answer} for {self.answer.question.title}'
