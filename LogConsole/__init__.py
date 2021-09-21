from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from rich.text import Text


class LogConsoleScroll:
    """
    实现在一定高度自动滚动的rich日志类，建议配合Layout、Panel等组件使用
    """
    __log_lines: list
    __height: int

    def __init__(self):
        self.__log_lines = []
        self.__height = 1

    def __rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
        self.__height = options.height
        for _ in range(self.__height):
            if len(self.__log_lines) < _+1:
                yield ""
            else:
                yield self.__log_lines[_]
        # TODO 换成 rich._log_render.LogRender

    def log(self, log):
        height = self.__height
        self.__log_lines.append(log)
        self.__log_lines = self.__log_lines[-height:]


class LogConsoleOverwrite:
    """
    实现在一定高度自动覆写的rich日志类，建议配合Layout、Panel等组件使用
    """
    __log_lines: list
    __height: int
    __pos: int
    showPos: bool

    def __init__(self, showPos=True):
        self.__log_lines = []
        self.__height = 1
        self.__pos = 0
        self.showPos = showPos

    def __rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
        self.__height = options.height
        if self.showPos:
            grid = Table.grid()
            grid.add_column(style="bold magenta", width=3)
            grid.add_column()
        for _ in range(self.__height):
            if len(self.__log_lines) < _+1:
                if self.showPos:
                    grid.add_row()
                else:
                    yield ""
            else:
                if self.showPos:
                    if (_ + 1) % self.__height == self.__pos:
                        grid.add_row(" > ", self.__log_lines[_])
                    else:
                        grid.add_row("   ", self.__log_lines[_])
                else:
                    yield self.__log_lines[_]
        if self.showPos:
            yield grid
        # TODO 换成 rich._log_render.LogRender

    def log(self, log):
        height = self.__height
        pos = self.__pos
        if len(self.__log_lines) > height:
            self.__log_lines = self.__log_lines[:height]

        if len(self.__log_lines) < height:
            self.__log_lines.append(log)
        elif len(self.__log_lines) == height:
            self.__log_lines[pos] = log
        else:
            raise Exception("非法状态")
        self.__pos = (pos + 1) % height
