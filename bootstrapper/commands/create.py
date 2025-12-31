import click

@click.command()
@click.argument("name")
@click.option("--type", type=click.Choice(["backend", "frontend", "fullstack"]), required=True, help="Type of project to create")
@click.option("--docker", is_flag=True, help="Include Docker setup")
def create(name, type, docker):
    """Create a new project"""
    click.echo(f"Creating {type} project named {name} with docker={docker}")
