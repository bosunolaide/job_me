# from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from core.decorators import login_required, organization_required

from .forms import NewJobForm, EditJobForm
from .models import Category, Location, Job

def jobs(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    location_id = request.GET.get('location', 0)
    locations = Location.objects.all()
    jobs = Job.objects.filter(is_filled=False)

    if category_id:
        jobs = jobs.filter(category_id=category_id)
    
    if location_id:
        jobs = jobs.filter(location_id=location_id)

    if query:
        jobs = jobs.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'job/jobs.html', {
        'jobs': jobs,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'locations': locations,
        'location_id': int(location_id)
    })

def detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    related_jobs = Job.objects.filter(category=job.category, is_filled=False).exclude(pk=pk)[0:3]

    return render(request, 'job/detail.html', {
        'job': job,
        'related_jobs': related_jobs
    })


@organization_required
def new(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST, request.FILES)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('job:detail', pk=job.id)
    else:
        form = NewJobForm()

    return render(request, 'job/form.html', {
        'form': form,
        'title': 'New Job',
    })


@organization_required
def edit(request, pk):
    job = get_object_or_404(Job, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditJobForm(request.POST, request.FILES, instance=job)

        if form.is_valid():
            form.save()

            return redirect('job:detail', pk=job.id)
    else:
        form = EditJobForm(instance=job)

    return render(request, 'job/form.html', {
        'form': form,
        'title': 'Edit Job',
    })


@organization_required
def delete(request, pk):
    job = get_object_or_404(Job, pk=pk, created_by=request.user)
    job.delete()

    return redirect('dashboard:index')
