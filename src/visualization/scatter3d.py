from PySide6.QtWidgets import QWidget, QTableWidget, QGridLayout, \
    QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, \
    QPushButton

from PySide6.QtWebEngineWidgets import *


import plotly.express as px


import pandas as pd

class Scatter3D(QWidget):
    def __init__(self, data_ct, data_mri, title="3D просмотр отклонений"):

        super().__init__()

        self.data_ct = data_ct
        self.data_mri = data_mri

        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        # Add table
        self.l = QGridLayout(self)
        self.l.addWidget(self.browser)

        self.resize(1200,800)

        self.init_scatter3d()

    def init_scatter3d(self):
        df_ct = pd.DataFrame(self.data_ct, columns = ['x', 'y', 'z']) 
        df_ct['modality'] = 'CT'

        df_mri = pd.DataFrame(self.data_mri, columns = ['x', 'y', 'z']) 
        df_mri['modality'] = 'MRI'

        df = pd.concat([df_ct, df_mri])
        df.to_csv('table.csv')

        fig = px.scatter_3d(df, x='x', y='y', z='z', color='modality')
        fig.update_traces(marker_size = 2)

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    T = Scatter3D()
    T.show()

    app.exec_()