
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
@click.option('-t','--target',default=None)
@click.option('-n/','--dryrun/--live',default=False)
def newsite(domain,sitename,target,dryrun):
    if target is None:
        target = '/' if os.getuid()==0 else '.'

    live = not dryrun

    slug = encode(os.urandom(9)).decode('ascii')
    click.echo(slug)
    docroot = os.path.join(target,'var/www/',slug,'public')
    siteetc = os.path.join(target,"etc/nginx/sites-available")

    l = locals().copy()
    print(l)
    for template,target in (('index.html','{{docroot}}/{{template}}'),
                            ('site.nginx', '{{siteetc}}/{{domain}}'),
                            ):
        ft = Template(target)
        l['template']=template
        path = ft.render(**l)
        if live:
            os.makedirs(os.path.dirname(path),exist_ok=True)
        else:
            print("mkdir -p '{}'".format(path))

        text = env.get_template(template).render(**l)
        if live:
            with open(path,"w") as of:
                of.write(text)
        else:
            print('''cat >'{}' <<EOF\n{}\nEOF'''.format(path,text))
