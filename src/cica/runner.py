import os
from cica import config

class Runner():

    def run_suite(self):
        if not os.path.exists("/tmp/cica_recent_test"):
            print("First you need to set a test to run using 'cica find'")
        else:
            with open("/tmp/cica_recent_test", "r") as f:
                recent_test = f.read().strip()
            args = " ".join(config.args)
            os.system(f"robot {args} {recent_test}")
