"""
Module: table
Module for table widget
"""
from PySide6.QtWidgets import QWidget, QTableWidget, QGridLayout, \
    QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, \
    QPushButton

import pandas as pd


class Table(QWidget):
    """
    Table widget
    """
    def __init__(self, input_data, headers=('parameter', 'mean', 'std'), title="Статистика"):
        super().__init__()

        self.d = input_data
        self.headers = headers
        self.setWindowTitle(title)

        # Add table
        self.layout = QGridLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(headers)

        # Adjust table to window size
        h = self.table.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Add export option
        p = QPushButton("Сохранить таблицу в .csv")
        p.clicked.connect(self.export_to_csv)
        self.layout.addWidget(p)
        self.resize(1200, 400)

        self.custom_key_names = {
            'Mean difference, mm': 'Среднее отклонение, мм',
            'Min difference, mm': 'Минимальное отклонение, мм',
            'Max difference, mm': 'Максимальное отклонение, мм',
            'Std, mm': 'Стандартное отклонение, мм',
            'Percentage of differences > 0.5 mm': 'Процент отклонений, превышающих 0.5 мм',
            'Percentage of differences > 1 mm': 'Процент отклонений, превышающих 1 мм',
        }

        self.init_table()

    def init_table(self):
        """
        Initialize table widget
        """
        for k, v in self.d.items():
            # Add a new row at the end of the table
            i = self.table.rowCount()
            self.table.setRowCount(i+1)

            # Get custom key name, default to the original key if not found
            custom_key = self.custom_key_names.get(k, k)

            # Write the dictionary key in first column
            self.table.setItem(i, 0, QTableWidgetItem(custom_key))

            # if only one number is provided
            if isinstance(v, float) or isinstance(v, int):
                self.table.setItem(i, 1, QTableWidgetItem(str(v)))
            # if multiple values are provided
            elif type(v) is tuple:
                for j, v_ in enumerate(v):
                    self.table.setItem(i, 1+j, QTableWidgetItem(str(v_)))
            else:
                self.table.setItem(i, 1, QTableWidgetItem(str(v)))


    def export_to_csv(self):
        # Specify default CSV export option
        fd = QFileDialog()
        fd.setDefaultSuffix("csv")
        save_to = fd.getSaveFileName(filter="*.csv")[0]

        # No file is selected, abort export routine
        if not save_to:
            return

        # Retrieve information from table
        items = []

        for i in range(self.table.rowCount()):
            row = {}

            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                if item is not None:
                    row[self.headers[j]] = item.text()

            items.append(row)

        # Create pandas DataFrame and export to CSV
        df = pd.DataFrame(items)
        df.to_csv(save_to, index=False)

        QMessageBox.information(
            self,
            "Данные сохранены",
            f"Таблица успешно сохранена в \n{save_to}."
        )