from rest_framework import serializers
from . models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobApplication
        fields='__all__'

    # to handle capitilize status
    def to_internal_value(self, data):
        if 'status' in data and isinstance(data['status'], str):
            data['status'] = data['status'].lower()
        return super().to_internal_value(data)
    