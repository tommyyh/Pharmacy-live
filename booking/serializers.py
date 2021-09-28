from django.db.models import fields
from rest_framework import serializers
from .models import Public, Workplace

class PublicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Public
    fields = '__all__'

class WorkplaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Workplace
    fields = '__all__'