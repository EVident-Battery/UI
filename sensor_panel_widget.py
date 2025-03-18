from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar

class SensorPanel:
    """UI panel for sensor configuration including hostname, IP, battery status and progress"""
    
    def __init__(self, sensor_id, hostname_default, ip_default):
        self.sensor_id = sensor_id
        self.hostname_default = hostname_default
        self.ip_default = ip_default
        
        # Create all UI components
        self.create_ui_elements()
        
    def create_ui_elements(self):
        """Create all UI elements for this sensor panel"""
        # Hostname row
        self.hostname_layout = QHBoxLayout()
        self.hostname_label = QLabel(f"Sensor {self.sensor_id} Hostname:")
        
        self.hostname_entry = QLineEdit()
        self.hostname_entry.setText(self.hostname_default)
        self.hostname_entry.setPlaceholderText(f"Sensor {self.sensor_id} Hostname")
        
        self.auto_find_button = QPushButton("Auto Find")
        
        # Add to hostname layout
        self.hostname_layout.addWidget(self.hostname_label)
        self.hostname_layout.addWidget(self.hostname_entry)
        self.hostname_layout.addWidget(self.auto_find_button)
        
        # IP row
        self.ip_layout = QHBoxLayout()
        self.ip_label = QLabel(f"Sensor {self.sensor_id} IP:")
        
        self.ip_entry = QLineEdit()
        self.ip_entry.setText(self.ip_default)
        self.ip_entry.setPlaceholderText(f"Sensor {self.sensor_id} IP Address")
        
        self.submit_ip_button = QPushButton("Submit IP")
        
        # Battery status indicator
        self.battery_icon = QLabel("🔋")
        self.battery_icon.setStyleSheet("font-size: 18px;")
        self.battery_value = QLabel("N/A")
        self.battery_value.setStyleSheet("font-weight: bold; color: #4caf50;")
        
        # Add to IP layout
        self.ip_layout.addWidget(self.ip_label)
        self.ip_layout.addWidget(self.ip_entry)
        self.ip_layout.addWidget(self.submit_ip_button)
        self.ip_layout.addWidget(self.battery_icon)
        self.ip_layout.addWidget(self.battery_value)
        
        # Progress bar for IP finder
        self.finder_progress = QProgressBar()
        self.finder_progress.setFixedHeight(20)
        self.finder_progress.setValue(0)
        self.finder_progress.setTextVisible(True)
        self.finder_progress.setFormat("Ready")
        
        # Collection progress elements
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #2962ff; font-weight: bold;")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("Ready")
        
    def add_to_layout(self, parent_layout):
        """Add all panel elements to the provided parent layout"""
        parent_layout.addLayout(self.hostname_layout)
        parent_layout.addLayout(self.ip_layout)
        parent_layout.addWidget(self.finder_progress)
        
    def connect_signals(self, parent_func1, parent_func2, sensor_id):
        """Connect signals for this sensor panel"""
        self.auto_find_button.clicked.connect(lambda: parent_func1(sensor_id))
        self.submit_ip_button.clicked.connect(lambda: parent_func2(sensor_id))
        
    def get_all_ui_elements(self):
        """Return a list of all UI elements for this sensor"""
        return [
            self.hostname_label, self.hostname_entry, self.auto_find_button,
            self.ip_label, self.ip_entry, self.submit_ip_button, 
            self.battery_icon, self.battery_value
        ]
        
    def update_battery_status(self, percentage):
        """Update battery status display"""
        self.battery_value.setText(f"{percentage:.0f}%")
        
        # Update color based on level
        if percentage <= 20:
            self.battery_icon.setStyleSheet("font-size: 18px; color: #f44336;")  # Red
            self.battery_value.setStyleSheet("font-weight: bold; color: #f44336;")
        elif percentage <= 40:
            self.battery_icon.setStyleSheet("font-size: 18px; color: #ff9800;")  # Orange
            self.battery_value.setStyleSheet("font-weight: bold; color: #ff9800;")
        else:
            self.battery_icon.setStyleSheet("font-size: 18px; color: #4caf50;")  # Green
            self.battery_value.setStyleSheet("font-weight: bold; color: #4caf50;")