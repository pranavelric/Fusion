from django.contrib import admin

from .models import Employee,EmpConfidentialDetails,EmpDependents,EmpTraining,ForeignService

# Register your models here.

admin.site.register(Employee)
admin.site.register(EmpConfidentialDetails)
admin.site.register(EmpDependents)
admin.site.register(EmpTraining)
admin.site.register(ForeignService)