"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Banking Kata Python."""


if __name__ == "__main__":
    main(prog_name="banking-kata-python")  # pragma: no cover
