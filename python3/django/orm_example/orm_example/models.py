from django.db import models
from django.forms import ModelForm


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
