
import click
import os
from base64 import urlsafe_b64encode as encode
from jinja2 import Environment, PackageLoader, select_autoescape, Template

env = Environment(
    loader=PackageLoader('nsite', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

@click.command()
@click.argument("domain")
@click.argument("sitename")
def newsite(domain,sitename):
    slug = encode(os.urandom(9)).decode('ascii')
    click.echo(slug)
    docroot = os.path.join("var/www/{}/public".format(slug))
    siteetc = "etc/nginx/sites-available"

    l = locals().copy()
    print(l)
    for template,target in (('index.html','{{docroot}}/{{template}}'),
                            ('site.nginx', '{{siteetc}}/{{domain}}'),
                            ):
        ft = Template(target)
        l['template']=template
        path = ft.render(**l)
        os.makedirs(os.path.dirname(path),exist_ok=True)
        text = env.get_template(template).render(**l)
        print(path)
        print(text)
        with open(path,"w") as of:
            of.write(text)
