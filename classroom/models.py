from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.http import FileResponse
import uuid
from os.path import join, basename
from django.utils import timezone


class Classroom(models.Model):
    def get_uuid():
        return uuid.uuid4().hex

    id = models.CharField(
        max_length=50,
        primary_key = True,
        default = get_uuid,
        editable = False,
    )
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=20)
    teachers = models.ManyToManyField(User, related_name='teacher')
    students = models.ManyToManyField(User, related_name='student', blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.id}"

    @property
    def num_students(self):
        return self.students.count()
    
    @property
    def teacher_name(self):
        teachers = self.teachers.all()
        if len(teachers) > 0:
            teacher1 = teachers[0]
            first_name = teacher1.first_name
            if first_name:
                return first_name
            else:
                return teacher1.username
        else:
            return None

    @property
    def active_status_css_class(self):
        if self.active:
            return "online"
        else:
            return "offline"
    
    @property
    def last_post_time(self):
        if self.classroompost_set.count() > 0:
            post = self.classroompost_set.latest('posted')
            return post.posted
        else:
            return False
    
    @property
    def upcoming_events(self):
        timenow = timezone.now()
        exams = self.test_set.filter(schedule__gt=timenow).order_by("schedule")
        assignments = self.task_set.filter(deadline__gt=timenow).order_by('deadline')
        num_events = len(exams) + len(assignments)
        hasevents = bool(num_events)
        return {'hasevents':hasevents, 'num_events':num_events, 'exams':exams, 'assignments':assignments}
    
    @property
    def ongoing_tests(self):
        timenow = timezone.now()
        tests = self.test_set.filter(schedule__lte=timenow, expired=False).order_by("-created")
        return tests

    @property
    def weeklies(self):
        qs = self.weekly_set.all().order_by('created')
        return qs
    
    @property
    def num_weeklies(self):
        return self.weeklies.count()
    
    @property
    def has_weeklies(self):
        return bool(self.num_weeklies)
    
    @property
    def num_posts(self):
        return self.classroompost_set.count()
    
    @property
    def assigned_tasks(self):
        return self.task_set.all()
    
    @property
    def assigned_group_tasks_list(self):
        tasks = self.assigned_tasks
        return [task for task in tasks if task.is_group_task]
    
    @property
    def assigned_indiv_tasks_list(self):
        tasks = self.assigned_tasks
        return [task for task in tasks if not task.is_group_task]
    
    @property
    def num_tasks(self):
        return self.assigned_tasks.count()
    
    @property 
    def num_group_tasks(self):
        return len(self.assigned_group_tasks_list)
        
    @property 
    def num_indiv_tasks(self):
        return len(self.assigned_indiv_tasks_list)
    
    @property
    def assigned_tasks_total_marks(self):
        tasks = self.assigned_tasks
        marks = tasks.aggregate(models.Sum('marks'))['column__sum']
        return marks
    
    @property
    def group_tasks_total_marks(self):
        tasks = self.assigned_group_tasks_list
        marks = sum([task.marks for task in tasks])
        return marks
    
    @property
    def indiv_tasks_total_marks(self):
        tasks = self.assigned_indiv_tasks_list
        marks = sum([task.marks for task in tasks])
        return marks
    



class PostTopic(models.Model):
    name = models.CharField(max_length=100)
    str_id = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def num_posts(self):
        return self.classroompost_set.count()
    
    @property
    def has_posts(self):
        return bool(self.num_posts)
    
    @property
    def posts(self):
        return self.classroompost_set.order_by('-posted')


class ClassroomPost(models.Model):
    def get_uuid():
        return uuid.uuid4().hex

    id = models.CharField(
        max_length=50,
        primary_key = True,
        default = get_uuid,
        editable = False,
    )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    description = models.CharField(max_length=9999)
    topics = models.ManyToManyField(PostTopic)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post id-{self.id} of: {self.classroom}"
    
    @property
    def num_comments(self):
        return self.comment_set.count()

    @property
    def num_attachments(self):
        return self.postattachment_set.count()

    @property
    def has_comments(self):
        if self.num_comments > 0:
            return True
        else:
            return False
    
    @property
    def has_topics(self):
        if self.topics.count() > 0:
            return True
        else:
            return False
    

    @property
    def has_attachments(self):
        if self.num_attachments > 0:
            return True
        else:
            return False   


class PostAttachment(models.Model):
    def filepath(self, filename):
        return join("attachments", str(self.classroom_post.classroom.id), filename)

    classroom_post = models.ForeignKey(ClassroomPost, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=filepath)

    @property
    def filename(self):
        return str(basename(self.attached_file.name))


    
class Comment(models.Model):
    def get_uuid():
        return uuid.uuid4().hex

    id = models.CharField(
        max_length=50,
        primary_key = True,
        default = get_uuid,
        editable = False,
    )
    post = models.ForeignKey(ClassroomPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    comment_text = models.CharField(max_length=9999)
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment object({self.id}) of post:<{self.post.id}>"

    @property
    def is_thread(self):
        # a thread is a type of comment which has no parent comment (not a reply comment)
        if self.parent is None:
            return True
        else:
            return False

    @property
    def has_replies(self):
        num_replies = self.reply.count()
        if num_replies > 0:
            return True
        else:
            return False
    
    @property
    def cssClass(self):
        if self.author in self.post.classroom.teachers.all():
            # user-teacher class has a teacher badge in it
            return "username user-teacher"
        else:
            return "username"
    
    @property
    def replies(self):
        return self.reply.all().order_by("comment_time")


class Assignment(models.Model):
    def get_uuid():
        return uuid.uuid4().hex

    id = models.CharField(
        max_length=50,
        primary_key = True,
        default = get_uuid,
        editable = False,
    )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    instructions = models.TextField(null=True, blank=True)
    submission_deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)


class AssignmentAttachment(models.Model):
    def filepath(self, filename):
        return join("attachments/assignments", str(self.assignment.classroom.id), filename)

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=filepath)

    @property
    def filename(self):
        return str(basename(self.attached_file.name))
    
    
class AssessmentMeta(models.Model):
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)
    attendance_marks = models.FloatField(default=10)
    classtest_marks = models.FloatField(default=10)
    group_task_marks = models.FloatField(default=5)
    indiv_task_marks = models.FloatField(default=5)
    weekly_test_marks = models.FloatField(default=10)
    
    def __str__(self):
        return f"{self.classroom.id} - Assessment meta"
    
    
class Assessment(models.Model):
    meta = models.ForeignKey(AssessmentMeta, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_score = models.FloatField(null=True, blank=True)
    classtest_score = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"User-{self.student.id} assessment of classroom {self.meta.classroom.id}"
    
    
    @property
    def group_task_score(self):
        students_gw_total_score = self.student.account.group_task_total_points(self.meta.classroom)
        group_tasks_total_marks = self.meta.classroom.group_tasks_total_marks
        score_per_mark = students_gw_total_score/group_tasks_total_marks
        obtained_score = score_per_mark*self.meta.group_task_marks
        return obtained_score
    
    @property
    def indiv_task_score(self):
        students_iw_total_score = self.student.account.indiv_task_total_points(self.meta.classroom)
        indiv_tasks_total_marks = self.meta.classroom.indiv_tasks_total_marks
        score_per_mark = students_iw_total_score/indiv_tasks_total_marks
        obtained_score = score_per_mark*self.meta.indiv_task_marks
        return obtained_score
        

    # @property
    # def indiv_task_score(self):
        