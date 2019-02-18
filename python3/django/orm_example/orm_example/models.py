from django.db import models
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DetailView, DeleteView


class Person(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.CharField(max_length=20)

    def __str__(self):
        return f"I, " + self.name + ", " + str(self.age) + " years old, was born on " + str(self.birthday) + "!"


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'birthday']


class PersonDetail(DetailView):
    model = Person
    template_name = "person_detail.html"


class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'age', 'birthday']
    template_name = "person_update.html"

    def get_success_url(self):
        # Give them the detail about the person once they update them.
        return reverse('person-detail', kwargs={'pk': self.object.pk})


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')
    template_name = "person_delete.html"

    def get_success_url(self):
        return reverse('person-list')
