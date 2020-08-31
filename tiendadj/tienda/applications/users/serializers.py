from rest_framework import serializers


class LoginSocialSerializer(serializers.Serializer):
    # this serializer is going to recieve a token, so we struvture a serielizer for that
    token_id = serializers.CharField(required=True)