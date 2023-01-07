from django.db import models
from classroom.models import Classroom
import uuid
from os.path import join, basename



class Weekly(models.Model):
    def get_uuid():
        return uuid.uuid4().hex

    id = models.CharField(
        max_length=50,
        primary_key = True,
        default = get_uuid,
        editable = False,
    )
    weeknum = models.IntegerField(unique=True)
    topic = models.CharField(max_length=100, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    pre_class_instruction = models.CharField(max_length=2000, blank=True, null=True)
    in_class_instruction = models.CharField(max_length=2000, blank=True, null=True)
    post_class_instruction = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.classroom.id} - week{self.weeknum}"
    
    @property
    def preClassTuto(self):
        qs = self.preclasstutorial_set.all().order_by('added')
        return qs
    
    @property
    def inClassTuto(self):
        qs = self.inclasstutorial_set.all().order_by('added')
        return qs

    @property
    def postClassTuto(self):
        qs = self.postclasstutorial_set.all().order_by('added')
        return qs
    
    @property
    def hasPreClassTuto(self):
        qs = self.preclasstutorial_set.all().order_by('added')
        return bool(len(qs))
    
    @property
    def hasInClassTuto(self):
        qs = self.inclasstutorial_set.all().order_by('added')
        return bool(len(qs))
    
    @property
    def hasPostClassTuto(self):
        qs = self.postclasstutorial_set.all().order_by('added')
        return bool(len(qs))


class PreClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'preclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        return str(basename(self.attached_file.name))


class InClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'inclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        return str(basename(self.attached_file.name))


class PostClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'inclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        return str(basename(self.attached_file.name))


class PreClassTutorial(models.Model):
    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    yt_id = models.CharField(max_length=20) # yt_id = YouTube ID
    description = models.CharField(max_length=1000, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)


class InClassTutorial(models.Model):
    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    yt_id = models.CharField(max_length=20)
    description = models.CharField(max_length=1000, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)


class PostClassTutorial(models.Model):
    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    yt_id = models.CharField(max_length=20)
    description = models.CharField(max_length=1000, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)