from djoser.serializers import UserSerializer

from .models import User


class UserInfoSerializer(UserSerializer):
    class Meta(UserSerializer):
        model = User
        fields = ('id', 'name', 'email', 'is_student',)
