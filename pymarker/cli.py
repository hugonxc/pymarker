import click
from .core import generate_marker, generate_patt

@click.command()
@click.argument('filename')
@click.option('--patt','-p', is_flag=True, default=False)
@click.option('--marker','-m', is_flag=True, default=False)
@click.option('--border-size', '-b', default=50) # 50% is based on template hiro marker
@click.option('--output','-o', default=None, type=str)
def generate_patt_and_marker(filename, patt, marker, border_size, output):
    click.echo("-- Starting PyMarker Generator --".format(filename))
    if (patt and marker) or (not patt and not marker):
        generate_patt(filename, output)
        generate_marker(filename, border_size, output)
        click.echo("Generating patt and marker for {}".format(filename))
    elif marker:
        generate_marker(filename, border_size, output)
        click.echo("Generating marker for {}".format(filename))
    elif patt:
        generate_patt(filename, output)
        click.echo("Generating patt for {}".format(filename))

    click.echo("Done.")

def main():
    generate_patt_and_marker()

if __name__ == "__main__":
    main()