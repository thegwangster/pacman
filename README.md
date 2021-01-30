# Homework 2: Pacman
In this problem, you'll implement several different search algorithms to help Pac-Man find his way through a maze.

You'll do so by filling in the code marked as YOUR CODE HERE in search.py and searchAgents.py. Make sure to follow the directions in the homework document.

We recommend that you either install locally on your computer. However, you should be able to use CAEN if necessary. If you do use CAEN, then you will not be able to use the graphics, and so you will not install the

## Downloading the repo and installing dependencies
You'll need to install pip and tkinter. On Ubuntu and similar, run
```
sudo apt-get install python3-tk
sudo apt install python3-pip
```
Otherwise, install them in whatever way you install Python packages.

Then, 
```
pip3 install future
```
Note: you may need this [fix](https://askubuntu.com/questions/1061486/unable-to-locate-package-python-pip-when-trying-to-install-from-fresh-18-04-in).

To test that all the dependencies worked, run this command and play pacman. If this works, you can get started coding and testing.
```
python3 pacman.py
```

If this doesn't work, then you may want to try running a command from test.py using the `-q` flag to not have graphical output. Note that this will likely mean that it will be more challenging to debug your code, because you won't be able to see what's going on.

## Testing Your Code
The staff has provided some test cases for you to test your code in `test.py`. Run `python3 test.py` to test them. Note that these are *not comprehensive*. Your grade will be based partially on these test cases, but will also be based on a larger suite of hidden test cases. For this reason, we strongly recommend that you write your own test cases. In particular, you may want to test your A* code yourself, for both manhattan and euclidean heuristics.

## Credit
All credit for this portion of the homework goes to [UC Berkeley’s CS188](http://ai.berkeley.edu).
