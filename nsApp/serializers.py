from nsApp.models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # nested serializer
    books = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = '__all__'
