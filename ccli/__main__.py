import click
from pathlib import Path
import jinja2    

templateLoader = jinja2.FileSystemLoader(searchpath="/home/brian/sandbox/cloudup-cli/ccli/templates")
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)

types = ['string', 'number', 'integer', 'boolean', 'array', 'object']

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
@click.option('--description', default="Test term", help="Describe the term.")
@click.option('--format', help='Suggested formatting.')
@click.option('--type', prompt="Data type", help="A term's data type.", type=click.Choice(types, case_sensitive=False))
def term(name, **kwargs):
    filename = name + '.json'
    path = Path.cwd() / 'terms' / filename
    
    if path.exists():
        click.echo('Term exists, exiting.')
        return False

    click.echo('Creating term `{name}`, described as `{description}`'.format(name=name, description=kwargs['description']))
    template = templateEnv.get_template('term.json')
    body = template.render(kwargs, name=name)
    path.write_text(body)


@click.command()
def schema():
    click.echo('Creating Schema')

@click.command()
def schema_term():
    click.echo('Adding term to schema')

@click.command()
def api():
    click.echo('Creating API definition')

@click.command()
def api_endpoint():
    click.echo('Adding endpoint to API')

@click.command()
def handler():
    click.echo('Adding new handler')

@click.command()
def endpoint_handler():
    click.echo('Connecting endpoint handler')

cli.add_command(term)
cli.add_command(schema)
cli.add_command(schema_term)
cli.add_command(api)
cli.add_command(api_endpoint)
cli.add_command(handler)
cli.add_command(endpoint_handler)

if __name__ == '__main__':
    cli()