Title: How to create a virtual environment on Mac
Date: 2020-04-30 15:52
Category: Python
Tags: Python, Virtual Environment
Slug: create_virtual_environment
Authors: Iain
Summary: A short guide on how to create a virtual environment in python.
Draft: True

Open a terminal window and go to the folder where the project is going to be located, usually using the cd command.

~~~
cd folder/path
~~~

And then once in the folder I run the command:

~~~
python3 -m venv venv
~~~

This creates the virtual environment, to check that it's been successful you can simply type `ls` into the terminal to return a list of contents for the folder where you should now see a /venv/ folder.

Next you need to activate the virtual environment, to do that run the following:

~~~
source venv/bin/activate
~~~

In the terminal you should now see `(venv)` on the command line, this means that the virtual environment is active.

The next step is to install your packages, I will cover this another time!

To leave the virtual environment, you simply need to type the folowing into the command line followed by enter:

~~~
deactivate
~~~