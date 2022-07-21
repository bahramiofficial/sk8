from rest_framework import serializers


class UserNameRelationalField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{self.first_name} {self.last_name} - {value.mobile} -'
