from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static

from robot import run


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def run_tests(self) -> None:
        run("/home/chickfas/Documents/programs/robot_tests")

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Button(label="Hello"),
                )
            )

    def on_button_pressed(self, event: Button.Pressed):
        self.run_tests()


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())
