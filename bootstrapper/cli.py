# bootstrapper/cli.py

import click
from bootstrapper.commands import create, list_cmd, run

@click.group()
def main():
    """Project Bootstrapper CLI: Scaffold Python backend & React frontend projects"""
    pass

# Add commands to the CLI
main.add_command(create.create)
main.add_command(list_cmd.list_templates)
main.add_command(run.run_project)
