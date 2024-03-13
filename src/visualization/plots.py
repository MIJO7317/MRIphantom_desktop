from PySide6.QtWidgets import QWidget, QGridLayout, QSlider, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np

import json

class Plots(QWidget):
    def __init__(self, d, title="Графики"):
        super().__init__()

        self.data_per_slice = d

        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)

        self.resize(1500, 850)
        self.init_plots()

    def init_plots(self):
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

        fig.add_trace(go.Scatter(x=df.index, y=df['Mean difference, mm'], name='Среднее отклонение, мм', mode='markers'),
            row=1, col=1)

        fig.add_trace(go.Scatter(x=df.index, y=df['Max difference, mm'], name='Максимальное отклонение, мм', mode='markers'),
            row=1, col=2)

        fig.add_trace(go.Scatter(x=df.index, y=df['Min difference, mm'], name='Минимальное отклонение, мм', mode='markers'),
            row=1, col=3)

        fig.add_trace(go.Scatter(x=df.index, y=df['Std, mm'], name='Среднеквадратичное отклонение', mode='markers'),
            row=2, col=1)
        
        fig.add_trace(go.Scatter(x=df.index, y=df['Number of differences > 0.5 mm'], name='Число отклонений > 0.5 мм', mode='markers'),
            row=2, col=2)
        
        fig.add_trace(go.Scatter(x=df.index, y=df['Number of differences > 1 mm'], name='Число отклонений > 1 мм', mode='markers'),
            row=2, col=3)
        
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

if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication([])

    with open('/Users/bzavolovich/Developer/MRIphantom_interface/Users/bzavolovich/Developer/MRIphantom_interface/studies/29January/slice_difference_stats.json', 'r') as f:
        data = json.load(f)
    p = Plots(data)
    p.show()

    app.exec_()
