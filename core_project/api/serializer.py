from rest_framework import serializers
from .models import *
import re




class stu_serilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['id']
        # fields = ['name', 'age', 'father_name']
    
    def validate(self, data):
        if 'age' in data and data['age'] <18:
                raise serializers.ValidationError({
                    'error': "Age cannot be less then 18"
                })
        elif 'name' in data and data['name']:
                for n in data['name']:
                    if n.isdigit():
                        raise serializers.ValidationError({
                    'error': "Name can have number it it"
                })

        return super().validate(data)




class std_mark_serializers(serializers.ModelSerializer):
     std = stu_serilizer()
     class Meta:
          model = StudentMark
          exclude = ['id']