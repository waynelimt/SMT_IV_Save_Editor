# SMT_IV_Save_Editor
Save editor for Shin Megami Tensei IV

This is a save editor for Shin Megami Tensei IV, made in Python 3. Tested 100% working in Windows.
<br/><br/>
Installation:
No installation needed for this. 
<br/><br/>
For Windows:
Just install Python 3 for Windows (https://www.python.org/downloads/, v3.5.2 at time of writing) with the default settings on. After that, you can just double click on the .py script and it should automatically launch the script with the installed python interpreter.
<br/><br/>
For Linux (Ubuntu):
Newer versions of Ubuntu (14.04 LTS & above) should come with Python 3 installed. Firstly, make the script executable, by typing the following in a terminal: <b>chmod a+x <path to script>/smt_iv_apocalypse_save_editor.py</b>
<br/>
*Replace <path to script> with the path to the script itself.
After that, type in a terminal: <b>./smt_iv_apocalypse_save_editor.py</b>
<br/>
If there are no errors and the script successfully launches a GUI, then it is all good, you can ignore the following instructions.
<br/><br/>
However, Ubuntu 16.04 LTS does not have Tkinter package installed, which is responsible for the GUI for the script. So, if you are using Ubuntu 16.04 LTS, you will need to first install the Tkinter package by typing the following in a terminal: <b>sudo apt-get install python3-tk</b>
<br/>
After installing the package, the script should launch properly.
