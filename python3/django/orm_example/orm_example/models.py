from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    id = models.UUIDField(primary_key=True)

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return "I, {}, {} years old, was born on {}!" \
            .format(self.name, self.age, self.birthday)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'birthday']