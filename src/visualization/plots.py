"""
Module: plots
Module for plots widget
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout
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
        df = pd.DataFrame.from_dict(self.data_per_slice).T
        fig = make_subplots(rows=2, cols=3, start_cell="top-left",
                            subplot_titles=(
                                'Среднее отклонение, мм',
                                'Максимальное отклонение, мм',
                                'Минимальное отклонение, мм',
                                'Среднеквадратичное отклонение, мм',
                                'Число отклонений > 0.5 мм',
                                'Число отклонений > 1 мм'
                                ))
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Mean difference, mm'],
                                 name='Среднее отклонение, мм',
                                 mode='markers'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Max difference, mm'],
                                 name='Максимальное отклонение, мм',
                                 mode='markers'), row=1, col=2)
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Min difference, mm'],
                                 name='Минимальное отклонение, мм',
                                 mode='markers'), row=1, col=3)
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Std, mm'],
                                 name='Среднеквадратичное отклонение',
                                 mode='markers'), row=2, col=1)
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Number of differences > 0.5 mm'],
                                 name='Число отклонений > 0.5 мм',
                                 mode='markers'), row=2, col=2)
        fig.add_trace(go.Scatter(x=df.index,
                                 y=df['Number of differences > 1 mm'],
                                 name='Число отклонений > 1 мм',
                                 mode='markers'), row=2, col=3)
        fig.update_xaxes(title_text='Номер среза')
        fig.update_yaxes(title_text='Величина отклонения, мм')

        fig.update_layout(
            title="Отчёт",
            legend_title="Легенда",
            font=dict(
                size=12
            )
        )

        fig.update_traces(marker_size=6)
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
