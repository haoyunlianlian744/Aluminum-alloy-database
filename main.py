import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QPushButton,
)

from auth.login import LoginDialog
from data_storage.storage import DataStorageWidget
from data_query.query import DataQueryWidget
from data_overview.overview import DataOverviewWidget
from machine_learning.ml import MachineLearningWidget


class MainWindow(QMainWindow):
    """Main application window providing access to all modules."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aluminum Alloy Database")

        self.stack = QStackedWidget()
        self.storage_page = DataStorageWidget()
        self.query_page = DataQueryWidget()
        self.overview_page = DataOverviewWidget()
        self.ml_page = MachineLearningWidget()

        self.stack.addWidget(self.storage_page)
        self.stack.addWidget(self.query_page)
        self.stack.addWidget(self.overview_page)
        self.stack.addWidget(self.ml_page)

        # Navigation buttons
        nav_layout = QVBoxLayout()
        storage_btn = QPushButton("Data Storage")
        query_btn = QPushButton("Data Query")
        overview_btn = QPushButton("Data Overview")
        ml_btn = QPushButton("Machine Learning")

        storage_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.storage_page))
        query_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.query_page))
        overview_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.overview_page))
        ml_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.ml_page))

        nav_layout.addWidget(storage_btn)
        nav_layout.addWidget(query_btn)
        nav_layout.addWidget(overview_btn)
        nav_layout.addWidget(ml_btn)

        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.addLayout(nav_layout)
        container_layout.addWidget(self.stack)
        container.setLayout(container_layout)

        self.setCentralWidget(container)


def main() -> int:
    """Entry point for the application."""
    app = QApplication(sys.argv)
    login = LoginDialog()
    login.exec()

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
