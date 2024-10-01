from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from . models import Job
from . forms import ApplicationForm, UserRegistrationForm, JobForm

# Create your views here.
def is_company(user):
    return user.userprofile.is_company


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserRegistrationForm()
        return render(request, 'Job/register.html', {'form':form})  

def LoginView(request):
    if request.method == 'POST':
        pasS              



def JobList(request):
    jobs = Job.objects.all()
    return render(request, 'Job/job_listing.html', {'jobs': jobs})


def ApplyForJob(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit = False)
            application.user = request.user
            application.job = application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()        
    return render(request, 'Job/apply_for_job.html',{'form':form, 'job':job} )
