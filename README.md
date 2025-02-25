# Number Guesser

A simple command-line number guessing game written in Python where players try to guess a random number between 0 and 100.

## Features

- Three difficulty levels:
  - Easy (10 chances)
  - Medium (5 chances)
  - Hard (3 chances)
- Random number generation between 0-100
- Feedback on each guess
- Game over message revealing the number if not guessed

## How to Play

1. Run the program:
python number_guessr.py


2. Choose your difficulty level:
   - Enter `1` for Easy
   - Enter `2` for Medium
   - Enter `3` for Hard

3. Enter your guesses when prompted
   - You'll be told if you won after a correct guess
   - If you run out of chances, the correct number will be revealed

## Requirements

- Python 3.x
- No external libraries required (uses built-in `random` module)

## Example Game
a task tracker this is, the loop is to take input from user, if user says "updt" then it prompts which task no. (0 through 9) to update, and then takes user input to update the task and save it to the said json file without changing any other tasks saved


Here's a README.md for your Task Tracker application:
python
python task_tracker.py
TASK TRACKER APP
enter the number of tasks you want to add: 2
Task 1: Complete homework
Task 2: Buy groceries
update a task...(updt)
add a task...(add)
remove a task...(rmv)
mark a task as done...(done)
mark a task as in progress...(ip)
list all tasks...(lst)
list done tasks...(lst_done)
list in progress tasks...(lst_ip)
=> lst
tasks to do: {'task_1': 'Complete homework', 'task_2': 'Buy groceries'}
This README provides:
A brief description of the application
List of features
Usage instructions
Available commands
Information about data storage
Requirements
Example usage
Important notes
Feel free to modify or expand this README based on any additional features or specific instructions you want to include!
generate a readme.md file for this

Here's a README.md file for your Number Guesser game:
python number_guessr.py
welcome to the game!
i will guess a number from 0-100
chose your difficulty
1. easy - 10 chances
2. medium - 5 chances
3. hard - 3 chances
-> 2
enter your guess -> 50
wrong one!
enter your guess -> 75
wrong one!
enter your guess -> 25
wrong one!
enter your guess -> 12
wrong one!
enter your guess -> 6
wrong one!
the number was 87
