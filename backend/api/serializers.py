from django.contrib.auth.models import User
from rest_framework import serializers

#verifica que los datos vayan correctos para crear usuario
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        extra_kwargs={"password":{"write_only": True}}
    #crea el usuario
    def create(self,valided_data):
        user=User.objects.create_user(**valided_data)
        
        return user