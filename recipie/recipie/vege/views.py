from django.shortcuts import render,redirect
from vege.models import *
from django.http import HttpResponse
# Create your views here.


def recipie(request):
    if request.method=='POST':
        data = request.POST
        print(data)

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        print(receipe_name,receipe_description,receipe_image)
        return redirect('/')
        if request.GET.get('search'):
            queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    queryset = Receipe.objects.all()
 
    return render(request,'recipie.html',context={'receipes':queryset})



def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # Update fields with new values
        if receipe_name:
            queryset.receipe_name = receipe_name
        if receipe_description:
            queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/')  # Ensure this redirects to the correct view, adjust if needed

    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)

