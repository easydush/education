from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
