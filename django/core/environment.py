# -*- coding: utf-8 -*-
import os

from dotenv import dotenv_values

env = {**dotenv_values(dotenv_path=os.path.join(os.getcwd(), "..", ".env"), verbose=True), **os.environ}

__all__ = ["env"]
