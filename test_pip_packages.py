import subprocess
import os
import threading
import socket
from typing import NoReturn

try:
    import sys # TODO: See if this takes too much time

    script_directory = os.path.dirname(os.path.abspath(__file__))
    requirements_file = os.path.join(script_directory, "requirements.txt")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "-q", "-r", requirements_file])


    from pygls.server import LanguageServer
    from tools.ls_tools import ServerFunctions
    from servable.spelling import ServableSpelling
    from servable.servable_wb import wb_line_diagnostic
    from servable.verse_validator import ServableVrefs
    from servable.servable_embedding import ServableEmbedding
    import genetok
    import flask # forces install if it is not installed
    import flask_cors # forces install if it is not installed
except ImportError:
    import sys
    script_directory = os.path.dirname(os.path.abspath(__file__))
    requirements_file = os.path.join(script_directory, "requirements.txt")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "-q", "-r", requirements_file])
    exit()
