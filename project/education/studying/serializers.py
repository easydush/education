from rest_framework import serializers
from studying.models import CourseListener


class CourseListenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseListener
        fields = '__all__'
