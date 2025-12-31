import click

@click.command()
@click.argument("name")
def run_project(name):
    """Run project services"""
    click.echo(f"Running project {name} (Docker support coming soon)")
