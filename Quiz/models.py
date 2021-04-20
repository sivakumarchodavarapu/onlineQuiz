from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.course_name

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=30, null=True)
    topic = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.topic

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=30, null=True)
    option2 = models.CharField(max_length=30, null=True)
    option3 = models.CharField(max_length=30, null=True)
    option4 = models.CharField(max_length=30, null=True)
    answer = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.question

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cat = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=10, null=True)
    add1 = models.CharField(max_length=100, null=True)
    add2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    img = models.FileField(null=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name



class QuizResult(models.Model):
    bhu = models.ForeignKey(UserDetail, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    result = models.CharField(max_length=30, null=True)
    date1 = models.DateField(null=True)
    marks = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.topic.topic+" "+self.topic.course.course_name


class FinalResult(models.Model):
    quiz = models.ForeignKey(QuizResult, on_delete=models.CASCADE, null=True)
    que = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    your_ans = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.que.question










