# Create your views here.
from random import randrange

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request):
    return HttpResponse('<p>Hello! I am the index.</p>'
                        '<p>Below are some URLs of interest:</p>'
                        '<ul>'
                        '    <li><a href="/math">math</a> has some cool math.</li>'
                        '    <li><a href="/templating">templating</a> uses Django\'s templating engine.</li>'
                        '</ul>')


def math(request):
    numbers = [randrange(0, 100) for _ in range(0, 10)]

    smallest = min(numbers)
    largest = max(numbers)

    html = "<p>I generated a list of random numbers. Here they are:</p>" \
           "<ul>"

    for number in numbers:
        html += "<li>{n}</li>".format(n=number)

    html += "</ul>"

    html += "<p>The largest is {l} and the smallest is {s}.</p>".format(l=largest, s=smallest)

    return HttpResponse(html)


def templating(request: HttpRequest):

    return render(request, "templating.html", {
        "cool_data": 0xFFFF,
        "cool_list": [1, 2, 3, "A", "B", "C"],
        "cool_dict": {
            "apples": "citrus",
            "bananas": "mealy",
            "cakes": "sweet"
        },
    })
