from rest_framework import serializers
from studying.models import CourseListener

from account.serializers import UserInfoSerializer


class CourseListenerSerializer(serializers.ModelSerializer):
    listener = UserInfoSerializer()

    class Meta:
        model = CourseListener
        fields = '__all__'
