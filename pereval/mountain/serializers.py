from rest_framework import serializers
from .models import Users, Coords, Pereval, Level, Image
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone',)


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter_lev', 'spring_lev', 'summer_lev', 'autumn_lev',)


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Image
        fields = ('image', 'title')


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    tourist_id = UserSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)
    status = serializers.CharField(default='NW')

    class Meta:
        model = Pereval
        depth = 1
        fields = ('id', 'status', 'tourist_id', 'add_time', 'beauty_title', 'title', 'other_titles', 'connect', 'coord_id', 'level', 'images', )

    def create(self, validated_data, **kwargs):
        tourist_id = validated_data.pop('tourist_id')
        coord_id = validated_data.pop('coord_id')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        tourist_id, created = Users.objects.get_or_create(**tourist_id)

        coord_id = Coords.objects.create(**coord_id)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, tourist_id=tourist_id, coord_id=coord_id, level=level)

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            Image.objects.create(image=image, pereval_id=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.tourist_id
            data_user = data.get('tourist_id')
            validating_user_fields = [
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
            ]

            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено':'Нельзя изменять данные пользователя'})
        return data


