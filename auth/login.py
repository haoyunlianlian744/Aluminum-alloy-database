from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton


class LoginDialog(QDialog):
    """Simple login dialog with login and register options."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        layout = QVBoxLayout()
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        # In a real application these would handle authentication and registration.
        self.login_button.clicked.connect(self.accept)
        self.register_button.clicked.connect(self.accept)

        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
