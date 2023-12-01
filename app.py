import platform
import subprocess

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Environment stuff!"),
    ui.span("Python"),
    ui.output_text_verbatim("python"),
    ui.span("Quarto"),
    ui.output_text_verbatim("quarto"),
)


def server(input, output, session):
    @output
    @render.text
    def python():
        return platform.python_version()

    @output
    @render.text
    def quarto():
        batcmd="quarto --version"
        return subprocess.check_output(batcmd, shell=True).decode()


app = App(app_ui, server)
