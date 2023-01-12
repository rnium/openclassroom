from django.db import models
from django.utils import timezone

from classroom.models import Classroom
import uuid
from os.path import join, basename
from pathlib import Path


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
    # files properties
    @property
    def preClassFiles(self):
        qs = self.preclassfile_set.all()
        return qs
    
    @property
    def inClassFiles(self):
        qs = self.inclassfile_set.all()
        return qs
    
    @property
    def postClassFiles(self):
        qs = self.postclassfile_set.all()
        return qs
    
    @property
    def hasPreClassFiles(self):
        return bool(len(self.preClassFiles))
    
    @property
    def hasInClassFiles(self):
        return bool(len(self.inClassFiles))
    
    @property
    def hasPostClassFiles(self):
        return bool(len(self.postClassFiles))

    @property
    def preClassTuto(self):
        qs = self.preclasstutorial_set.all().order_by('added')
        return qs

    # tutorial properties
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

    # tests
    @property
    def preClassUpcomingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(preclass=True, schedule__gt=timenow).order_by('schedule')
    
    @property
    def preClassOngoingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(preclass=True, schedule__lte=timenow, expiration__gt=timenow).order_by('schedule')
    
    @property
    def preClassPreviousTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(preclass=True, expiration__lt=timenow).order_by('schedule')
    
    @property
    def has_pre_class_tests(self):
        return bool(len(self.preClassUpcomingTest) + len(self.preClassPreviousTest))
    
    @property
    def has_pre_class_ongoing_test(self):
        return bool(len(self.preClassOngoingTest))
    
    # in class tests
    @property
    def inClassUpcomingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(inclass=True, schedule__gt=timenow).order_by('schedule')
    
    @property
    def inClassOngoingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(inclass=True, schedule__lte=timenow, expiration__gt=timenow).order_by('schedule')
    
    @property
    def inClassPreviousTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(inclass=True, expiration__lt=timenow).order_by('schedule')
    
    @property
    def has_in_class_tests(self):
        return bool(len(self.inClassUpcomingTest) + len(self.inClassPreviousTest))
    
    @property
    def has_in_class_ongoing_test(self):
        return bool(len(self.inClassOngoingTest))
    
    # post class tests
    @property
    def postClassUpcomingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(postclass=True, schedule__gt=timenow).order_by('schedule')
    
    @property
    def postClassOngoingTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(postclass=True, schedule__lte=timenow, expiration__gt=timenow).order_by('schedule')
    
    @property
    def postClassPreviousTest(self):
        timenow = timezone.now()
        return self.weeklytest_set.filter(postclass=True, expiration__lt=timenow).order_by('schedule')
    
    @property
    def has_post_class_tests(self):
        return bool(len(self.postClassUpcomingTest) + len(self.postClassPreviousTest))
    
    @property
    def has_post_class_ongoing_test(self):
        return bool(len(self.inClassOngoingTest))
    
    
    

class PreClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'preclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    must_study = models.BooleanField(default=False)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        name_str = basename(self.attached_file.name)
        return name_str.replace('_', ' ')
    
    @property
    def css_class(self):
        css_classes = {
            ".pdf": "bx bxs-file-pdf",
            ".pptx":"bx bx-slideshow",
            ".jpg": "bx bxs-file-image",
            ".png": "bx bxs-file-image",
            ".docx": "bx bxs-file-doc",
            ".zip": "bx bxs-file-archive",
            ".txt": "bx bxs-file-txt",
            ".py": "bx bxl-python",
            ".pyw": "bx bxl-python"
        }
        file_extention = Path(self.filename).suffix
        if file_extention in css_classes:
            return css_classes[file_extention]
        else:
            return "bx bxs-file-blank"        


class InClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'inclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    must_study = models.BooleanField(default=False)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        name_str = basename(self.attached_file.name)
        return name_str.replace('_', ' ')
    
    @property
    def css_class(self):
        css_classes = {
            ".pdf": "bx bxs-file-pdf",
            ".pptx":"bx bx-slideshow",
            ".jpg": "bx bxs-file-image",
            ".png": "bx bxs-file-image",
            ".docx": "bx bxs-file-doc",
            ".zip": "bx bxs-file-archive",
            ".txt": "bx bxs-file-txt",
            ".py": "bx bxl-python",
            ".pyw": "bx bxl-python"
        }
        file_extention = Path(self.filename).suffix
        if file_extention in css_classes:
            return css_classes[file_extention]
        else:
            return "bx bxs-file-blank"
    

class PostClassFile(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.weekly.classroom.id), 'weekly', str(self.weekly.id), 'inclass', filename)

    weekly = models.ForeignKey(Weekly, on_delete=models.CASCADE)
    must_study = models.BooleanField(default=False)
    attached_file = models.FileField(upload_to=filepath, max_length=1000)

    @property
    def filename(self):
        name_str = basename(self.attached_file.name)
        return name_str.replace('_', ' ')

    @property
    def css_class(self):
        css_classes = {
            ".pdf": "bx bxs-file-pdf",
            ".pptx":"bx bx-slideshow",
            ".jpg": "bx bxs-file-image",
            ".png": "bx bxs-file-image",
            ".docx": "bx bxs-file-doc",
            ".zip": "bx bxs-file-archive",
            ".txt": "bx bxs-file-txt",
            ".py": "bx bxl-python",
            ".pyw": "bx bxl-python"
        }
        file_extention = Path(self.filename).suffix
        if file_extention in css_classes:
            return css_classes[file_extention]
        else:
            return "bx bxs-file-blank"


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