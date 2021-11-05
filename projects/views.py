from django.shortcuts import render


def projects(request):
    context = {
        'page': 'projects',
        'number': 12
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single_project.html')
