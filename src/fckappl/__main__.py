import typer

app = typer.Typer()


@app.command()
def init():
    """Initialize the fckappl package."""
    print("Initializing the fckappl package... (unimplemented)")


@app.command()
def run():
    """Run the fckappl package."""
    print("Running the fckappl package... (unimplemented)")


if __name__ == "__main__":
    app() 