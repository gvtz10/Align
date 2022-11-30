from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Use built-in User class
# Custom db column name using db_column option
    
class File(models.Model):
    name = models.CharField("file name", max_length=64)
    upload = models.FileField()
    is_proj = models.BooleanField("project file", default=False)
    is_act = models.BooleanField("action file", default=False)
    # is_proj and is_act cannot both be false


class Tag(models.Model):
    name = models.CharField("tag name", max_length=32)
    is_proj = models.BooleanField("project tag", default=False)
    is_act = models.BooleanField("action tag", default=False)
    is_file = models.BooleanField("file tag", default=False)
    user = models.ManyToManyField(User)
    # is_proj, is_act, and is_file cannot all be false
                
class Project(models.Model):
    VISIBILITY_CHOICES = [
        (True, "public"),
        (False, "private"),
        ]
    STATUS_CHOICES = [
        (True, "open"),
        (False, "closed"),
        ]
    description = models.TextField()
    visibility = models.BooleanField(default=False, choices=VISIBILITY_CHOICES)
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)
    users = models.ManyToManyField(User, verbose_name="Team members")  # need form to choose multiple users.
    files = models.ManyToManyField(File, verbose_name="Project files", blank=True) # need form to upload or choose file.
    tags = models.ManyToManyField(Tag, verbose_name="Project tags", blank=True)
    # See forms for manytomany field: https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024

    def get_user_list(self):
        user_set = self.users.all()
        return [user.username for user in user_set]

    def get_tag_list(self):
        tag_set = self.tags.all()
        return [tag.name for tag in tag_set]
        
    
    
class Action(models.Model):
    VISIBILITY_CHOICES = [
        (True, "public"),
        (False, "private"),
        ]
    STATUS_CHOICES = [
        (True, "open"),
        (False, "closed"),
        ]
    description = models.TextField()
    visibility = models.BooleanField(default=False, choices=VISIBILITY_CHOICES)
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    p_project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="parent project", null=True, blank=True)
    p_action = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="parent action", null=True, blank=True)
    files = models.ManyToManyField(File, verbose_name="Action files", blank=True) # form to upload or choose file
    tags = models.ManyToManyField(Tag, verbose_name="Action tags", blank=True)
    
    def get_tag_list(self):
        tag_set = self.tags.all()
        return [tag.name for tag in tag_set]
    