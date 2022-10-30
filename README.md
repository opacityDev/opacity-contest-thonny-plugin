# Opacity Share
A Plugin for students and teachers who are in love with thonny to share in real time their work and code together with a very little data usage

## How to prepare your workspace ?

Opacity plugins development is done under a virtual python environment called **devenv** kept in the repo folder.</br>
This isolated workspace helps avoiding all kinds of conflicts with existing python distribution and site-packages
</br>
In order to prepare your environment and install all dependcies, kindly run the following code in the repo s' root directory :
~~~~
$ make first_use
~~~~

## How to run and test your code ?

The provided makefile does all the hardwork for you
* Creates a distrubtion from the current existing code
* Installs it in the virtual environment
* Cleans the directory
* Runs thonny from the virtual environment for the test
all you have to do is to run in your terminal `$ make` 