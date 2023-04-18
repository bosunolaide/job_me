from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from core.decorators import login_required, organization_required
from .forms import NewCVForm, EditCVForm
from .models import Category, Location, Library

# Create your views here.

def cvs(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    location_id = request.GET.get('location', 0)
    locations = Location.objects.all()
    cvs = Library.objects.filter(is_employed=False)

    if category_id:
        cvs = cvs.filter(category_id=category_id)

    if location_id:
        cvs = cvs.filter(location_id=location_id)

    if query:
        cvs = cvs.filter(Q(job_title__icontains=query) | Q(full_name__icontains=query))

    return render(request, 'library/cvs.html', {
        'cvs': cvs,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'locations': locations,
        'location_id': int(location_id)
    })

def detail(request, pk):
    cv = get_object_or_404(Library, pk=pk)
    related_cvs = Library.objects.filter(category=cv.category, is_employed=False).exclude(pk=pk)[0:3]

    return render(request, 'library/detail.html', {
        'cv': cv,
        'related_cvs': related_cvs
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewCVForm(request.POST, request.FILES)

        if form.is_valid():
            cv = form.save(commit=False)
            cv.created_by = request.user
            cv.save()

            return redirect('library:detail', pk=cv.id)
    else:
        form = NewCVForm()

    return render(request, 'library/form.html', {
        'form': form,
        'title': 'New CV',
    })

@login_required
def edit(request, pk):
    cv = get_object_or_404(Library, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditCVForm(request.POST, request.FILES, instance=cv)

        if form.is_valid():
            form.save()

            return redirect('library:detail', pk=cv.id)
    else:
        form = EditCVForm(instance=cv)

    return render(request, 'library/form.html', {
        'form': form,
        'title': 'Edit CV',
    })

@login_required
def delete(request, pk):
    cv = get_object_or_404(Library, pk=pk, created_by=request.user)
    cv.delete()

    return redirect('dashboard:index')
