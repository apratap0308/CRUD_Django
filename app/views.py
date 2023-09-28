from app.models import Candidate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CREATE
class Create(CreateView):
    model= Candidate
    fields= '__all__'
    success_url = reverse_lazy('read')

# READ 
class Read(ListView):
    model= Candidate
    queryset = Candidate.objects.all()

#UPDATE 
class Update(UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')


#DELETE
class Delete(DeleteView):
    queryset = Candidate.objects.all()
    success_url = reverse_lazy('read')


