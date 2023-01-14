from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidators
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(querset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        styles = {'input_type':'password'},
    )
    password_confirm = serializers.CharField(
        write_only = True,
        required = True,
        style = {'input_type':'password'},
    )
    class Meta: 
        model = User
        fields = [
            'username',
            'name',
            'surname',
            'email',
            'password',
            'password_confirm',
        ]

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializer.ValidationError(
                {'message':'The passwords did not match! Please try again.'}
            )
        return data
    
    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password_confirm')
        user = User.objects.create('**validated_date')
        user.set_password('password')
        user.save()
        return user
