from rest_framework import serializers
from App.models import User, Password
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def to_data(self):
            return self.data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['hash']

    def create(self, validated_data):
        instance = Password.objects.create(**validated_data)
        return instance.id
                
class LoginValidate():
    def run(value):
        messages = MessageUtil()
        if value.get('username') is None or value.get('username') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.USERNAME.value)
        if value.get('password') is None or value.get('password') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.PASSWORD.value)
        return messages.get()
        
                
        