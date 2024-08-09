"""
Module: plots
Module for plots widget
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


class Plots(QWidget):
    """
    Plots widget
    """

    def __init__(self, input_data, title="Графики"):
        super().__init__()

        self.data_per_slice = input_data
        self.setWindowTitle(title)
        self.browser = QWebEngineView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        self.resize(1500, 850)
        self.init_plots()

    def init_plots(self):
        """
        Initialize plots
        """
        df = pd.DataFrame.from_dict(self.data_per_slice)
        print(df.columns)
        fig = make_subplots(
            rows=2,
            cols=2,
            start_cell="top-left",
            subplot_titles=(
                "Среднее отклонение, мм",
                "Максимальное отклонение, мм",
                "Процент отклонений > 0.5 мм",
                "Процент отклонений > 1 мм",
            ),
        )

        # Add traces
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Mean difference, mm"],
                name="Среднее отклонение, мм",
                mode="markers",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Max difference, mm"],
                name="Максимальное отклонение, мм",
                mode="markers",
            ),
            row=1,
            col=2,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Percentage of differences > 0.5 mm"],
                name="Процент отклонений > 0.5 мм",
                mode="markers",
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Percentage of differences > 1 mm"],
                name="Процент отклонений > 1 мм",
                mode="markers",
            ),
            row=2,
            col=2,
        )

        # Update axes titles for each subplot
        fig.update_xaxes(title_text="Номер среза", row=1, col=1)
        fig.update_yaxes(title_text="мм", row=1, col=1)
        fig.update_xaxes(tick0=40, dtick=5, row=1, col=1)

        fig.update_xaxes(title_text="Номер среза", row=1, col=2)
        fig.update_yaxes(title_text="мм", row=1, col=2)
        fig.update_xaxes(tick0=40, dtick=5, row=1, col=2)

        fig.update_xaxes(title_text="Номер среза", row=2, col=1)
        fig.update_yaxes(title_text="%", row=2, col=1)
        fig.update_xaxes(tick0=40, dtick=5, row=2, col=1)

        fig.update_xaxes(title_text="Номер среза", row=2, col=2)
        fig.update_yaxes(title_text="%", row=2, col=2)
        fig.update_xaxes(tick0=40, dtick=5, row=2, col=2)

        fig.update_layout(
            title="Графики отклонений", legend_title="Легенда", font=dict(size=14)
        )

        fig.update_traces(marker_size=6)
        self.browser.setHtml(fig.to_html(include_plotlyjs="cdn"))


if __name__ == '__main__':
    df = pd.read_json('C:\\dev\\git\\MRIphantom_desktop\\studies\\1221124\\slice_difference_stats.json').T
    app = QApplication()
    plots_widget = Plots(df)
    plots_widget.show()
    app.exec()