# Teambuilder

Teambuilder is a small tool that helps to solve the problem of assigning N people to M teams, when each team has a
limited capacity of K members. To do this each person must give a list of preferences from 1 (most preferred team)
to K (least preferred team).

## Installation

    $ pip install munkres

## Usage

The preferences of each person must be stored as CSV file like in this example:

    name, team1, team2, team3
    Andreas, 3,2,1
    Markus, 3,2,1
    Jan, 2,3,1
    Andre, 3,1,2
    Thomas, 2,1,3

 To compute a possible assignment of the people to the three teams "team1", "team2" and "team3" with a capacity of 2 do

     $ python teambuilder.py <name_of_csv> 2
     WISHES:
     ['Markus', ' 3', '2', '1']
     ['Jan', ' 2', '3', '1']
     ['Andreas', ' 3', '2', '1']
     ['Thomas', ' 2', '1', '3']
     ['Andre', ' 3', '1', '2']
     TEAM ASSIGNMENT:
     (Markus,  team3) -> 1
     (Jan,  team1) -> 2
     (Andreas,  team3) -> 1
     (Thomas,  team2) -> 1
     (Andre,  team2) -> 1
     FAIRNESS:
     0.833333333333

The tool will randomly shuffle the rows of the input file. So to see another possible assignment just rerun the tool
again.



