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
