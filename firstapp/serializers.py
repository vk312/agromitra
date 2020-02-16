from rest_framework import serializers
from .models import Farmer,AgriExpert,AgriAssistant,States,Cities,Talukas
from phone_field import PhoneField


class FarmerSerializer(serializers .ModelSerializer):
    class Meta:
        model = Farmer

        #can show only selected fields
        fields = ['id','farmer_name','phone','mpin','aadhar_no']
        #fields = '__all__'   #returns all fields__


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriExpert

        # can show only selected fields
        fields = ['id', 'expert_name', 'phone', 'mpin', 'aadhar_no','occupation',"field_of_interest"]


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriAssistant

        # can show only selected fields
        fields = ['id', 'assistant_name', 'phone', 'mpin', 'aadhar_no','taluka','city','state','latitude','longitude']


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States

        # can show only selected fields
        fields = ('id', 'state_name')


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities

        # can show only selected fields
        fields = ('id', 'city_name','state_id')


class TalukasSerializer(serializers.ModelSerializer):
    #city_id= serializers.RelatedField(many=True,read_only= True ,required=False)

    class Meta:
        model = Talukas

        # can show only selected fields
        fields = ('id', 'taluka_name','city_id')

    # def create(self, validated_data):
    #     city_id = validated_data.pop('city_id')
    #     instance = Talukas.objects.create(**validated_data)
    #
    #     for city_id in city_id:
    #         Cities.objects.create(Talukas=instance, **city_id)
    #
    #     return instance
    #
