# from django.contrib.auth.decorators import login_required
from core.decorators import login_required
from django.shortcuts import render, get_object_or_404

from job.models import Job

@login_required
def index(request):
    jobs = Job.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'jobs': jobs,
    })
