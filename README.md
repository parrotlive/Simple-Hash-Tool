# Hash Calculator Tool Usage Guide

This tool allows you to hash files or text using a calculator that includes the most common hash algorithms. The usage is straightforward, and the following steps will guide you through the process.

## Requirements

Before you begin, ensure the following:

1. **Python 2.6+ Installed**: Make sure you have Python 2.6 or a later version installed on your system.
2. **Install `customtkinter` Library**: To install the required `customtkinter` library, open your command prompt (cmd) and enter the following command:
   ```bash
   pip install customtkinter
   ```
   
## Getting Started

### Launch the Tool

1. **Start the Application**: 
- Simply double-click the `start.bat` file. This will open the application window on your screen.

### Select the Algorithm

2. **Choose Hash Algorithm**:
- At the top of the window, you'll see a dropdown menu labeled "Select Algorithm." Choose your desired hashing algorithm from the list.

### Input Text

3. **Enter Your Text**:
- In the text field provided, type the text that you want to hash.

### Generate Hash

4. **Hash the Text**:
- Once you've entered your text, click on the "Hash Text Field Input" button to generate the hash using the selected algorithm.

## Hashing Files

### Select a File

5. **Choose a File to Hash**:
- To hash a file, click on the "Select File" button. A file dialog will appear, allowing you to choose the file you want to hash.

### Generate File Hash

6. **Hash the Selected File**:
- After selecting the file, click on the "Hash Selected File" button to generate the hash of the file using the selected algorithm.

## Retrieving Hashes

7. **View Generated Hashes**:
- To view the hashes you have generated, navigate to the `logs` folder in the tool's directory. Inside, you'll find a file named with the current date. Open this file to retrieve the hashes.
## Color Chooser Feature

The Hash Calculator Tool also includes a **Color Chooser** that allows you to customize the application's color scheme. This feature lets you adjust the primary, secondary, background, button, and highlight colors according to your preferences.

### How to Use the Color Chooser

1. **Access the Color Chooser**:
   - Open the application and navigate to the "Color Selector" tab.

2. **Adjust the Colors**:
   - You will see three sliders corresponding to the Red, Green, and Blue (RGB) values.
   - Adjust these sliders to mix the desired color for the selected element.

3. **Preview the Color**:
   - A color preview box will display the current color based on the RGB values you’ve set.

4. **Apply the Color**:
   - Once you're satisfied with the color, click on the corresponding button to apply it:
     - **Primary Color**: Affects the main elements of the UI.
     - **Secondary Color**: Affects secondary elements and accents.
     - **Background Color**: Sets the background color of the application.
     - **Button Background Color**: Changes the background color of the buttons.
     - **Highlight Color**: Adjusts the color of highlighted elements.

5. **Restore Default Colors**:
   - If you want to revert to the original color scheme, simply click the "Restore default Colors" button.

6. **Save Your Settings**:
   - The changes you make are saved in the `config.ini` file. To apply your new color settings, restart the application.

### Notes:
- **Settings Application**: Color changes will only take effect after restarting the application.
- **Logging**: Any changes you make to the color scheme are logged and can be reviewed in the `logs` directory.

This feature provides a simple and intuitive way to personalize the look and feel of your Hash Calculator Tool.
