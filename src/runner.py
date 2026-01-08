from robot import run
import config

class Runner:

    def run_test(self) -> None:
        run(config.suite_path + " " + config.args)
