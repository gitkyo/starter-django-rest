from django.contrib.auth.models import User, Group
from .models import Question, Choice
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, QuestionSerializer, ChoiceSerializer
# from quickstart import views

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    
    """
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer 
    permission_classes = [permissions.IsAuthenticated]

class ChoiceViewSet(viewsets.ModelViewSet):
    """
    
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 
    permission_classes = [permissions.IsAuthenticated]
