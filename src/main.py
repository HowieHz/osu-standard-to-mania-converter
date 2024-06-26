import multiprocessing
import os

from cli import cli_main
from webui import webui_main

if __name__ == "__main__":
    multiprocessing.freeze_support()
    ret: str = cli_main()
    if ret == "enter-webui":
        os.environ["WEBUI_FLAG"] = "True"
        webui_main(port=28099)
