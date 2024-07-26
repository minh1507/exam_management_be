from rest_framework import serializers
from App.models import User, Password
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def to_data(self):
            return self.data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['hash']

    def create(self, validated_data):
        instance = Password.objects.create(**validated_data)
        return instance.id

class RegisterValidate():
    def run(value):
        messages = MessageUtil()
        if value.get('username') is None or value.get('username') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.USERNAME.value)
        if value.get('username') is not None and (value.get('username')).isnumeric() == True:
            messages.push(ContentMessage.INVALID.value, KeyMessage.USERNAME.value)
        if value.get('username') is not None and len(value.get('username'))<6:
            messages.push(ContentMessage.INVALID_USERNAME.value, KeyMessage.USERNAME.value)
        if User.objects.filter(username=value.get('username')).exists():
            messages.push(ContentMessage.EXISTED.value, KeyMessage.USERNAME.value)
        if value.get('password') is None or value.get('password') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.PASSWORD.value)
        if value.get('password') is not None and StringUtil.validate_password(value.get('password')) != True:
            messages.push(ContentMessage.INVALID_PASSWORD.value, KeyMessage.PASSWORD.value)
        return messages.get()
                
class LoginValidate():
    def run(value):
        messages = MessageUtil()
        if value.get('username') is None or value.get('username') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.USERNAME.value)
        if value.get('password') is None or value.get('password') == "":
            messages.push(ContentMessage.REQUIRED.value, KeyMessage.PASSWORD.value)
        return messages.get()
        
                
        