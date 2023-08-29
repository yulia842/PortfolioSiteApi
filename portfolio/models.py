from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Skill(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40 )
    description = models.TextField(max_length=400)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        project_name = str(self.name) if self.name else "No Project"
        description = str(self.description) if self.description else "No description"
        skills_str = " ".join([skill.name for skill in self.skills.all()])
        return f"{project_name}, {description}, {skills_str}"

    
    def num_of_ratings(self):
        ratings = ProjectRating.objects.filter(project=self)
        return len(ratings)

    def avg_ratings(self):
        sum = 0
        ratings = ProjectRating.objects.filter(project=self)
        for rating in ratings:
            sum += rating.stars
        if (len(ratings) > 0):
            return (sum / len(ratings))
        else:
            return 0


class ProjectRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'project'),)
        index_together = (('user', 'project'),)

    def __str__(self):
        project_name = str(self.project) if self.project else "No Project"
        user_name = str(self.user) if self.user else "No User"
        stars_count = str(self.stars) if self.stars else "No Stars"
        return f"{project_name}, {user_name}, {stars_count}"

class Education(models.Model):
    institution = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    projects = models.ManyToManyField(Project)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        institution_name = str(self.institution) if self.institution else "No Institution"
        description_name = str(self.description) if self.description else "No Description"
        projects_str = ", ".join([project.name for project in self.projects.all()]) 
        skills_str = ", ".join([skill.name for skill in self.skills.all()])
        return f"{institution_name}, {description_name},skills: {skills_str},projects: {projects_str}"