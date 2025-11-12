from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self): return self.name

class Activity(models.Model):
    STATUS = [('pendiente','Pendiente'),('en_progreso','En progreso'),('completada','Completada')]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=150)
    planned_start = models.DateField(null=True, blank=True)
    planned_end = models.DateField(null=True, blank=True)
    progress_percent = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='pendiente')

    def __str__(self): return f"{self.project} - {self.name}"

class ActivityLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    progress_percent = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self): return f"{self.activity} {self.date} {self.progress_percent}%"
