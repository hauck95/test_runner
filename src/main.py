import runner
import typer

class Main():

    app = typer.Typer()

    @app.command()
    def find():
        print("Finding tests...")

    @app.command()
    def again():
        print("Running tests again...")

if __name__ == "__main__":
    main = Main()
    main.app()
