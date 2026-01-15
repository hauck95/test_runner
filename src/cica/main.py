import typer

from cica.finder import Finder
from cica.runner import Runner

app = typer.Typer()

class Main:

    @app.command()
    def find() -> None:
        finder = Finder()
        finder.set_test()

    @app.command()
    def run() -> None:
        runner = Runner()
        runner.run_suite()

if __name__ == "__main__":
    main = Main()
    app()
