2017Fall 590PR Final Project 
==========

A brief introduction on our project about **M**onte **C**arlo **S**imulation. 

> ***We are still learning, but for sure will try our best.***
> @ [*Yingjun Guan*](https://ischool.illinois.edu/people/phd-students/yingjun-guan)
> @ [*Lan Li*](https://www.linkedin.com/in/lan-li-42682214a/)


## Title: 
  Monte Carlo Simulation for Tic-tac-toe Game
  
  ![Tic-tac-toe](https://lh3.googleusercontent.com/EgfiSB2bdf7kuRfNQbe8Jaj_bhfrlfeRt2nzphA6jcbCQdy5iEku2uZyK-5_VWtWUCxi=w300)

## Team Member(s):
  Yingjun Guan, Lan Li. And special thanks to our instructor, John Weible
  
## Project
### Project Structure
**check the file [Framework_project](https://github.com/yingjun2/Final-project/blob/master/Framework_Project)**

### Project usage
**Clone the whole repository to the local space, run Model/Board_GUI.py. **

### Background:
[Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) is a world famous game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

[Monte Carlo Simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method) is a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. 

*Our project* focuses on applying the Monte Carlo Simulation into training the machine to how to play tic-tac-toe _wisely_.

### Hypothesis:
+ [ ] **Absolute randomness** - For any specific situation, the machine will try any blank spot, with an absolute randomness. In our case, the decision is on the basis of the simulation, which is on and only on the basis of randomness.
+ [ ] **random variable series** - Each step will be a different situation which will call a MCS for the decision, and the whole game is based on the collabraton of all MCS.
+ [ ] **No human experiences involved** - The program contains the idea of Exhaustive Attack method and the spirit of traversal, on the other hand, no human experience of the game is needed.
+ [ ] **Decision making** - Each possible solution is given appropriate weight for evaluation, and make the final decision; the process of decision making which based on the traversal on the next level(s) is called back propagation.

### Purpose/Functions:
 - We are ambitious enough to generate a human-computer interactive GUI medium for playing the game. 
 - The player can choose to play on the offensive position or the defensive position. [Not fulfiled yet.]
 - The player can choose to play with the AI in different levels (easy: totally random, medium: look only one step ahead, hard: traverse all possibilities)
 - The program can use the MCS to make the (best) decision. 
 - The program can also help dig in some interesting research on tic-tac-toe, including but not limited to:
 ~~~~
 1. What's the winning rate of the offensive position / defensive position?
 2. What's the potential skill level of the game?
 3. Is there a way to never lose at Tic-Tac-Toe?
 4. How's the winning rate for different levels of AIs?
 5. How much will the times of Monte Carlo Simulation affect the results.
 etc.
 ~~~~
 
### Algorithm:
 - The whole program applies the idea of recursion. The following figure can also helps to clarify the algorithm.
 ![Algorithm](http://i.imgur.com/L6uAKBD.png)
 
### Future work:
 - Efficiency. (When the hard level is selected, the program is very slow)
 - Elimate the Redundancy. (Code repititions and referencing in chaos)
 - In battle mode, both first and second player position should be selected.
 - Tighter connection between 1st and 2nd modes.
 - Training the machine. / try other algorithms.
 - OOP improvement (eg: static programs.)
 
## Sources:
 - Software: Python 3.6 (PythonCharm), 
 - PyQT for UI design,
 - Algorithm: [Monte Carlo Tree Search](http://www.cameronius.com/research/mcts/about/index.html)
 
## References:
 - _Tic tac toe_: https://en.wikipedia.org/wiki/Tic-tac-toe
 - _Monte Carlo Method_: https://en.wikipedia.org/wiki/Monte_Carlo_method
 - _Minimax algorithm_: https://neverstopbuilding-dropblog.herokuapp.com/minimax
 - _Monte Carlo Tree Search_: http://www.cameronius.com/research/mcts/about/index.html
 - _PYQT_: https://en.wikipedia.org/wiki/PyQt
 - _interesting questions in Tic Tac Toe_: https://www.quora.com/topic/Tic-Tac-Toe
