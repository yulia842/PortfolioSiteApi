from rest_framework.response import  Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Skill, Project, ProjectRating, Education
from .serializers import SkillSerializer, ProjectSerializer, ProjectRatingSerializer, EducationSerializer
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
      
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    authentication_classes = (TokenAuthentication ,)

    @action(methods=['POST'], detail=False)
    def add_skill(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = SkillSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()         
        return Response({"detail": "Skill saved.", "data" : serializer.data}, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=True)
    def remove_skill(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        skill = Skill.objects.get(id=pk)
        skill.delete()
        return Response({"detail": "Skill deleted."}, status=status.HTTP_200_OK)
    
    @action(methods=['PUT'], detail=True)
    def update_skill(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        skill = Skill.objects.get(id=pk)
        serializer = SkillSerializer(skill,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Skill updated."}, status=status.HTTP_200_OK)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication, )

    @action(methods=['POST'], detail=True)
    def rate_project(self, request,pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        if 'stars' in request.data:
            project = Project.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print(project.name,",",stars, user)

            try:
                rating = ProjectRating.objects.get(user=user.id, project = project.id)
                rating.stars = stars
                rating.save()
                serializer = ProjectRatingSerializer(rating, many=False)
                response = {'message':'Updated ratings', 'data' : serializer.data}
                return Response(response, status = status.HTTP_200_OK)
            
            except:
                rating = ProjectRating.objects.create(user=user, project=project, stars=stars)
                serializer = ProjectRatingSerializer(rating, many=False)
                response = {'message':'Created ratings', 'data' : serializer.data}
                return Response(response, status = status.HTTP_200_OK)
        
        else:
            response = {'message':'Stars are required'}
            return Response(response, status = status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['POST'], detail=False)
    def add_project(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProjectSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()         
        return Response({"detail": "Project saved.", "data" : serializer.data}, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=True)
    def remove_project(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({"detail": "Project Deleted."}, status=status.HTTP_200_OK)
    
    @action(methods=['PUT'], detail=True)
    def update_project(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Skill updated."}, status=status.HTTP_200_OK)    

class ProjectRatingViewSet(viewsets.ModelViewSet):
    queryset = ProjectRating.objects.all()
    serializer_class = ProjectRatingSerializer
    authentication_classes = (TokenAuthentication, )
    def update(self, request, *args, **kwargs):
        response = {"massage" : "Can't UPDATE!"}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        response = {"massage" : "Can't CREATE!"}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    authentication_classes = (TokenAuthentication, )

    @action(methods=['POST'], detail=False)
    def add_education(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer =EducationSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()         
        return Response({"detail": "Education saved.", "data" : serializer.data}, status=status.HTTP_201_CREATED)

    @action(methods=['DELETE'], detail=True)
    def remove_education(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        education = Education.objects.get(id=pk)
        education.delete()
        return Response({"detail": "Education Deleted."}, status=status.HTTP_200_OK)
    
    @action(methods=['PUT'], detail=True)
    def update_education(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        education = Education.objects.get(id=pk)
        serializer = EducationSerializer(education,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Education updated."}, status=status.HTTP_200_OK)    