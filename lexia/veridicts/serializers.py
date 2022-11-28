import datetime
from rest_framework import serializers
from .models import Veridicts

class VeridictSerializer(serializers.ModelSerializer):
    veridict_number = serializers.CharField(max_length=20, required=True)
    court_name = serializers.CharField(max_length=100, required=True)
    veridict_date = serializers.DateField(default=datetime.date.today, required=True)
    upload_date = serializers.DateTimeField(auto_now_add=True, required=True)
    pdf_file = serializers.FileField(default=None, upload_to="veridicts/", required=True)

    class Meta:
        model = Veridicts
        fields = ('__all__')