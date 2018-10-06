from jinja2 import Template

with open('one_file.j2') as f:
    template = Template(f.read())

print(template.render(name='John'))