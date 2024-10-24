from rest_framework import serializers
class InvoiceFAQSerializer(serializers.Serializer):
    title = serializers.CharField()
    details = serializers.ListField(child=serializers.CharField())
