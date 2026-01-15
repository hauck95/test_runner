import os
from cica import config


class Finder:

    def set_test(self) -> None:
        # project_dir = os.path.dirname(os.path.abspath(__file__)) #This is a weird solution, but it works for now
        # file_path = os.path.join(project_dir, "_recent_test")
        os.system(f"cd {config.suite_path}")
        os.system(f"cd {config.suite_path} && realpath $(fzf) > /tmp/cica_recent_test")
        with open("/tmp/cica_recent_test", "r") as f:
            new_test = f.read().strip()
        print(f"New test file set: {new_test}")

    # def find_tests(self) -> None:
        #TODO: fzf integration for finding tests
        # file_path = os.system("realpath $(fzf)")
        # print("File above is selected.")
        # self.write_recent_test_file(name=str(file_path))
