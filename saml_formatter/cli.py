import base64
from typing import Annotated

from lxml import etree
import rich
import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def format(
    input_: Annotated[
        str,
        typer.Argument(
            ..., help="Base64 encoded SAML request or response", metavar="input"
        ),
    ],
):
    """Base64 decode and then format a SAML request or response."""

    decoded = base64.b64decode(input_).decode()

    try:
        tree = etree.fromstring(decoded)
    except etree.XMLSyntaxError as e:
        rich.print(f"Error parsing XML: {e}")
        raise typer.Exit(code=1)

    pretty_xml = etree.tostring(tree, pretty_print=True).decode()
    rich.print("\n\n", pretty_xml)


if __name__ == "__main__":
    app()
