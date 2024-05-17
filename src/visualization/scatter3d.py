from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import plotly.express as px
import pandas as pd


class Scatter3D(QWidget):
    """
    Class for 3D scatter viewer
    """
    def __init__(self, data_ct, data_mri, title="3D просмотр отклонений"):
        super().__init__()

        self.data_ct = data_ct
        self.data_mri = data_mri

        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        # Add table
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.browser)

        self.resize(1200, 800)

        self.init_scatter3d()

    def init_scatter3d(self):
        """
        Initialize 3D scatter viewer
        """
        df_ct = pd.DataFrame(self.data_ct, columns=['x', 'y', 'z'])
        df_ct['modality'] = 'CT'
        df_mri = pd.DataFrame(self.data_mri, columns=['x', 'y', 'z'])
        df_mri['modality'] = 'MRI'
        df = pd.concat([df_ct, df_mri])
        df.to_csv('table.csv')
        fig = px.scatter_3d(df, x='x', y='y', z='z', color='modality')
        fig.update_traces(marker_size=2)

        # Customize axes spacing and stretch the plot by z-axis
        fig.update_layout(
            scene=dict(
                aspectratio=dict(x=1, y=1, z=1.05),  # Stretch z-axis
                xaxis=dict(
                    nticks=10,  # Number of ticks on x-axis
                    range=[df['x'].min(), df['x'].max()]  # Range for x-axis
                ),
                yaxis=dict(
                    nticks=10,  # Number of ticks on y-axis
                    range=[df['y'].min(), df['y'].max()]  # Range for y-axis
                ),
                zaxis=dict(
                    nticks=10,  # Number of ticks on z-axis
                    range=[df['z'].min(), df['z'].max()]  # Range for z-axis
                )
            )
        )

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
