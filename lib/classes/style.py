from rich.console import Console, ConsoleOptions
from rich.align import Align

class Style:
    def __init__(self, console, options):
        self.console = console
        self.options = options

    @property
    def console(self):
        return self._console
    @console.setter
    def console(self, console):
        self._console = console

    @property
    def options(self):
        return self._options
    @options.setter
    def options(self, options):
        self._options = options

    def __rich_console__(
        self, console: Console, options:ConsoleOptions
    ):
        width = options.max_width
        height = options.height or 1
        
        return Align.center(
            self.label, vertical="middle", style=self.style, width=width, height=height
        )