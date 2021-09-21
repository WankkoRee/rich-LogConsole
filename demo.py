import time

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel

from LogConsole import LogConsoleScroll, LogConsoleOverwrite

if __name__ == '__main__':
    layout = Layout()
    layout.split_row(
        Layout(name="scroll"),
        Layout(name="overwrite"),
    )
    scroll = LogConsoleScroll()
    layout["scroll"].update(Panel(scroll, title="scroll", subtitle="滚动刷新"))
    overwrite = LogConsoleOverwrite(showPos=True)
    layout["overwrite"].update(Panel(overwrite, title="overwrite", subtitle="覆写刷新"))
    with Live(layout, refresh_per_second=10):
        for i in range(1, 101):
            scroll.log(("0000" + str(i))[-4:])
            overwrite.log(("0000" + str(i))[-4:])
            i += 1
            time.sleep(0.1)
