"""yourscript chaine re"""

import click

@click.command()
@click.option('-s','--string-to-echo')
def echo(string_to_echo):
    click.echo(string_to_echo)
def cli():
    """Example Script"""
    click.echo("lai bari lai ")
