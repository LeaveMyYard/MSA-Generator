#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
    TEX compiler
"""
import sys
import os

import settings
from parts.generator import generate


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(
            os.path.join(f"{settings.overleaf_project_directory}", "main.tex"),
            "w",
            encoding="utf-8",
        )

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()

if __name__ == "__main__":
    generate()
