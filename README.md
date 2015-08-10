# MySQL Workbench Model Document Generation

A Python script to generate documentation from MySQL Workbench ERR diagram.

## Installation

* Download the latest release from [Github](https://github.com/letrunghieu/mysql-workbench-plugin-doc-generating/releases)
* Extract the downloaded file and find a file named `mysql-workbench-plugin-doc-generating.py`
* Open the MySQL Workbench
* Navigate to menu **Scripting** > **Install Plugin/Module...**
* Browse and select the extracted `.py` file
* Restart the Workbench

## Usage

### Generate documentation from ERR digram

* Open the ERR digram
* Navigate to menu **Tools** > **Utilities** > **Generate Documentation (Markdown)**
* When you see the status bar text changed to *Documentation generated into the clipboard. Paste it to your editor.*, Paste (<kbd>Ctrl</kbd> + <kbd>V</kbd> in most Linux/Window applications) to your editor and save as a new file.

### Generate ERR digram from physical database

In case that you do not have the ERR diagram, you have to create a diagram from your physical database first. Don't worry, MySQL Workbench has a greate tool to do this for you called **Reverse Engineer**.

* Open Workbench
* Navigate to menu **Database** > **Reverse Engineer...**
* Choose the connection, **Next**
* Wait and **Next**
* Select the datbase you want to create ERR diagram from, **Next**
* Wait and **Next**
* Select tables that you want to include in the ERR diagram, **Execute>**
* Wait and **Next**
* **Finish**

You have a new ERR diagram, you can generate the documentation from this diagram as the previous step.


After that, you can convert the output Markdown document into any format that you want.


## License

This script is released under the MIT license.