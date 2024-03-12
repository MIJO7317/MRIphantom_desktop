from PySide6.QtWidgets import QWidget, QTableWidget, QGridLayout, \
    QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox, \
    QPushButton

import pandas as pd

class Table(QWidget):
    def __init__(self, d, headers=['parameter', 'mean', 'std'], title="Статистика отклонений"):
        """Shows a window with a table

        :param d: Dictionary containing keys (parameters) with corresponding values
        :type d: dict
        :param headers: table headers, defaults to ['parameter', 'mean', 'std']
        :type headers: list, optional
        :param title: window title, defaults to "Table"
        :type title: str, optional
        """
        super().__init__()

        self.d = d
        self.headers = headers
        self.setWindowTitle(title)

        # Add table
        self.l = QGridLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(headers)

        # Adjust table to window size
        h = self.table.horizontalHeader()
        h.setSectionResizeMode(QHeaderView.Stretch)
        self.l.addWidget(self.table)

        # Add export option
        p = QPushButton("Сохранить таблицу в .csv")
        p.clicked.connect(self.exportToCSV)
        self.l.addWidget(p)
        self.resize(500, 400)

        self.initTable()

    def initTable(self):
        for k, v in self.d.items():
            # Add a new row at the end of the table
            i = self.table.rowCount()
            self.table.setRowCount(i+1)

            # Write the dictionary key in first column
            self.table.setItem(i, 0, QTableWidgetItem(k))

            # if only one number is provided
            if type(v) is float or type(v) is int:
                self.table.setItem(i, 1, QTableWidgetItem(str(v)))

            # if multiple values are provided
            elif type(v) is tuple:
                for j, v_ in enumerate(v):
                    self.table.setItem(i, 1+j, QTableWidgetItem(str(v_)))

            else:
                self.table.setItem(i, 1, QTableWidgetItem(str(v)))

    def exportToCSV(self):
        # Specify default CSV export option
        fd = QFileDialog()
        fd.setDefaultSuffix("csv")
        
        saveTo = fd.getSaveFileName(filter="*.csv")[0]

        # No file is selected, abort export routine
        if not saveTo:
            return

        # Retrieve information from table
        items = []

        for i in range(self.table.rowCount()):
            row = {}

            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                
                if item != None:
                    row[self.headers[j]] = item.text()

            items.append(row)

        # Create pandas DataFrame and export to CSV
        df = pd.DataFrame(items)
        df.to_csv(saveTo, index=False)

        QMessageBox.information(
            self,
            "Данные сохранены",
            f"Таблица успешно сохранена в \n{saveTo}."
        )


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    
    params = {
        'Distance': (100, 10),
    }

    T = Table(params)
    T.show()

    app.exec_()