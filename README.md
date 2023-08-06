# Monty Hall Simulation

## Introduction
Simple python program to run simulations of the famous [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) and calculate the probability of success by taking the average of success over the total of simulations ran.
Using the stay strategy the probability is ~0.33 while using the switch strategy it is ~0.66.

## Usage

```
usage: monty_hall.py [-h] [-n NUMBER_OF_SIMULATIONS] [-s]

Monty Hall

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_SIMULATIONS, --number-of-simulations NUMBER_OF_SIMULATIONS
                        Number of simulations to be run (default: 100000)
  -s, --switch          Switch door option. If unset will stay with first
                        choice. (default: False)
```
