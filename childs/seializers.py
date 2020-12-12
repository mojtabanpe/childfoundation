from childs.models import News, Office
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    slug = serializers.CharField()
    writer = serializers.IntegerField()
    body = serializers.CharField()
    image = serializers.CharField()
    publish_date = serializers.DateTimeField()
    created_date = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    status = serializers.CharField()   

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.writer = validated_data.get('writer', instance.writer)
        instance.body = validated_data.get('body', instance.body)
        instance.image = validated_data.get('image', instance.image)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.last_update = validated_data.get('last_update', instance.last_update)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def create(self, validated_data):
        return News.objects.create(**validated_data)

class OfficeSerializer(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    ave = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    fax = serializers.CharField()
    email = serializers.EmailField()
    website = serializers.URLField()
    another_phone = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.ave = validated_data.get('ave', instance.ave)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.fax = validated_data.get('fax', instance.fax)
        instance.email = validated_data.get('email', instance.email)
        instance.another_phone = validated_data.get('website', instance.website)
        instance.another_phone = validated_data.get('another_phone', instance.another_phone)
        instance.save()
        return instance

    def create(self, validated_data):
        return Office.objects.create(**validated_data)