# User Interface Guide

The application interface consists of four main panels: Configuration, Vehicle Information, Data Collection, and Activity Log. This guide explains how to use each panel effectively.

## Shaker Configuration

The Shaker Configuration panel contains several important controls:

- **Battery Status**: Displays the current battery voltage with a refresh button to update readings.
- **Rotation Speed Controls**: 
  - A dropdown menu with preset Rotations Per Second (RPS) values (recommended: 10.33)
  - A direct entry field for custom values (up to 2 decimal places)
- **Operation Controls**:
  - Start: Initiates the shaker using either the direct entry value or the dropdown selection. Direct entry takes precedence over dropdown if entered.
  - Stop: Halts shaker operation
  - Home: Returns the shaker tip to the calibrated home position
- **Connection Settings**:
  - Controller IP field with manual entry and submission option
  - Auto Find button to automatically detect the shaker on the network
- **Position Controls**:
  - Calibration/Set Home: Initiates the calibration sequence. The system will verify the shaker has full range of motion, then prompt you to set the home position.
  - Auto Up: Automatically positions the shaker (available after calibration)
  - Down: Press and hold to lower the shaker

**Important**: Always start the shaker before beginning data collection. During calibration, the system will verify the shaker has full range of motion, then prompt you to set the home position. The Auto Up function will precisely position the shaker tip against the battery pack for optimal testing.

## Sensor Configuration

This panel allows you to configure the sensors for data collection:

- Set the number of sensors (1-2)
- Enter the sensor hostname ID for auto-detection. If not using auto-detection this can be left as is.
- Manually configure sensor IP addresses
- Monitor sensor battery levels (visible after data collection begins)

## Vehicle Information

Use this panel to record essential vehicle data:

- VIN
- Make
- Model
- Year
- Trim
- Mileage
- Current State of Charge (SOC%)
- Optional file suffix for unique identification

The system automatically generates a 10-digit Test ID for each test session. This ID can be used to access test results on the EVident Battery website and can be automatically emailed to your specified email.

## Data Collection

This panel controls the testing process:

1. Configure sample time and save location
2. Ensure the shaker is running
3. Click "Start Collection" to begin the process
   - The system will perform a 5-second calibration
   - Data collection will commence automatically
   - The system will detect sensor anomalies and restart collection if necessary
4. Progress bars indicate the status of data collection
5. After collection, you can:
   - Save data to AWS by clicking "Save to AWS" (compresses and uploads data). **Important** Ensure that only information you want uploaded to AWS is in the save location folder.
   - Request email notification with the Test ID

**Note**: After the first collection cycle, sensor battery levels will be visible in the Sensor Configuration panel.

## Activity Log

The Activity Log panel provides a comprehensive record of all system operations and events. This log is valuable for troubleshooting and maintaining a record of testing procedures.







