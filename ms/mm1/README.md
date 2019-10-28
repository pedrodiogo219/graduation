## First install virtualenv (recommend):

This step creates a virtual environment. This basically creates a different python installation to allow you to install the python version you need and install the packages you need in the version you need, without the risk of having conflicting versions or packages messing up your local python installation and interfering in your other projects.

### Install **pip** first
pip is the python package installer, you are going to use this to install the numpy package and many other insteresting stuff.

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv

### Now create a virtual environment

    virtualenv venv

>you can use any name insted of **venv**

### You can also use a Python interpreter of your choice
>For this code to work you're going to need the 3.6.5 version
    virtualenv -p /usr/bin/python3.6 venv

### Active your virtual environment:    

    source venv/bin/activate

### To deactivate:

    deactivate

### Once the virtualenv is installed and activated, install the requirements
Inside this folder there is a *requirements.txt* file. This file have all the packages you must install to the run the project. You can install them all at once using pip3

    pip3 install -r requirements.txt


-------------------
## Run the code
You can now run the app easily, just run the file *Fila.py*

    python3 run.py


## Changing parameters for the simultation
Inside this folder there is, also, a *configs.env* file. Change it as you will and then run the code again.
