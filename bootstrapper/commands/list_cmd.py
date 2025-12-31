import click

@click.command()
def list_templates():
    """List available project templates"""
    click.echo("Available templates: backend, frontend, fullstack")
