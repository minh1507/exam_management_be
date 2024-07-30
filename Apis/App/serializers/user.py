from rest_framework import serializers
from App.models.user import User, Password, Profile
from App.commons.message import KeyMessage, ContentMessage
from App.commons.util import MessageUtil
from App.commons.util import StringUtil
from .role import RoleSerializer

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'role')

class UserDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'deletedAt')

class UserValidate():
    def run(value, type):
        messages = MessageUtil()
        match type:
            case "create":
                if value.get('name') is None or value.get('name') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.NAME.value)
                if value.get('name') is not None and (value.get('name')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.NAME.value)
                if User.objects.filter(name=value.get('name')).exists():
                    messages.push(ContentMessage.EXISTED.value, KeyMessage.NAME.value)
                if value.get('code') is None or value.get('code') == "":
                    messages.push(ContentMessage.REQUIRED.value, KeyMessage.CODE.value)
                if value.get('code') is not None and (value.get('code')).isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.CODE.value)
                return messages.get()
            case "pk":
                if value.isnumeric() == True:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                if StringUtil.is_valid_uuid(value) == False:
                    messages.push(ContentMessage.INVALID.value, KeyMessage.ID.value)
                return messages.get()
                

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['hash']

    def create(self, validated_data):
        instance = Password.objects.create(**validated_data)
        return instance.id
    
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname']

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
    
class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    role = serializers.CharField(max_length=100)

    def to_data(self):
            return self.data
    
class UserChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']