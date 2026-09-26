import typer

from .calculator import calculation
from .converter import convert as convert_value

app = typer.Typer()


@app.command()
def calc(expression: str) -> None:
    try:
        result = calculation(expression)
        typer.echo(result)
    except ValueError as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=2)


@app.command()
def convert(
    value: float,
    from_unit: str = typer.Option(..., "--from"),
    to_unit: str = typer.Option(..., "--to"),
) -> None:
    try:
        result = convert_value(value, from_unit, to_unit)
        typer.echo(result)
    except ValueError as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=2)


def main() -> None:
    app()


if __name__ == "__main__":
    main()