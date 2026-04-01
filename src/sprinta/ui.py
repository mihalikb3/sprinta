from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class SprintaDashboard(App):
    """A Textual app to display the training plan dashboard."""

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Welcome to Sprinta! Your AI Running Coach.", id="welcome")
        yield Footer()

def run_dashboard():
    app = SprintaDashboard()
    app.run()

if __name__ == "__main__":
    run_dashboard()
