from rest_framework import viewsets, status
from .models import Contact
from .serializers import ContactFormSerializer
from django.core.mail import send_mail
from rest_framework.response import Response

from rest_framework.decorators import action

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactFormSerializer

    @action(methods=['POST'],detail=False)
    def send_contact_form(self,request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            
            subject = f'New contact from {name}'
            message = f'From: {email}\n\nMessage:\n\n{message}'
            from_email = email
            recipient_list = ['contactform842@gmail.com']
            send_mail(subject, message, from_email, recipient_list)

            return Response({"detail": "Contact form sent successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)