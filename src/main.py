from robot import run

class Main:
    def run_suite(self) -> None:
        run(config.path)

if __name__ == "__main__":
    app = Main()
    app.run_suite()
