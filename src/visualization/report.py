from PySide6.QtWidgets import (QWidget, QGridLayout, QApplication, QVBoxLayout,
                               QHBoxLayout, QPushButton, QStackedWidget, QSlider)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
import sys
from table import Table
from plots import Plots
from scatter2d import Scatter2D
from scatter3d import Scatter3D
import pandas as pd
import json
import plotly.express as px


class Report(QWidget):
    """
    Report widget
    """
    def init(self, table_data, plot_data, ct_data, mri_data):
        super().init()
        self.setWindowTitle('Report')

        # Main layout for the Report widget
        main_layout = QVBoxLayout(self)

        # Create buttons for switching views
        button_layout = QHBoxLayout()
        self.table_button = QPushButton("Table View")
        self.plots_button = QPushButton("Plots View")
        self.browser_button = QPushButton("Browser View")
        self.scatter3d_button = QPushButton("3D Scatter View")
        self.scatter2d_button = QPushButton("2D Scatter View")
        button_layout.addWidget(self.table_button)
        button_layout.addWidget(self.plots_button)
        button_layout.addWidget(self.browser_button)
        button_layout.addWidget(self.scatter3d_button)
        button_layout.addWidget(self.scatter2d_button)
        main_layout.addLayout(button_layout)

        # Create a stacked widget to hold different views
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Initialize and add the Table widget
        self.table = Table(table_data)
        self.stacked_widget.addWidget(self.table)

        # Initialize and add the Plots widget
        self.plots = Plots(plot_data)
        self.stacked_widget.addWidget(self.plots)

        # WebEngineView for additional HTML content if needed
        self.browser = QWebEngineView()
        self.browser.setHtml('hello world')  # Example HTML content
        self.stacked_widget.addWidget(self.browser)

        # Initialize and add the Scatter3D widget
        self.scatter3d = Scatter3D(ct_data, mri_data)
        self.stacked_widget.addWidget(self.scatter3d)

        # Initialize and add the Scatter2D widget
        self.scatter2d = Scatter2D(ct_data, mri_data)
        self.stacked_widget.addWidget(self.scatter2d)

        # Connect buttons to switch views
        self.table_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.plots_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.browser_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.scatter3d_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.scatter2d_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))

        # Resize the Report window
        self.resize(1200, 1000)


if __name__ == 'main':
    app = QApplication(sys.argv)

    # Example data for Table and Plots
    with open('C:\\dev\\git\\MRIphantom_desktop\\studies\\1221124\\difference_stats.json') as f:
        table_data = json.load(f)
    plot_data = pd.read_json('C:\\dev\\git\\MRIphantom_desktop\\studies\\1221124\\slice_difference_stats.json').T
    print(plot_data)

    # Example data for Scatter3D and Scatter2D (you'll need to provide actual CT and MRI data)
    ct_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Replace with actual CT data
    mri_data = [[1.1, 2.1, 3.1], [4.1, 5.1, 6.1], [7.1, 8.1, 9.1]]  # Replace with actual MRI data

    report = Report(table_data, plot_data, ct_data, mri_data)
    report.show()

    sys.exit(app.exec())