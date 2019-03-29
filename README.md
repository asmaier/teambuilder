# Teambuilder

Teambuilder is a small tool that helps to solve the problem of assigning N people to M teams, when each team has a
limited capacity of K members. To do this each person must give a list of preferences from 1 (most preferred team)
to K (least preferred team). The skript then uses the [Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm)
(also called Kuhn-Munkres algorithm) to find a solution to this assignment problem.

In a broader context this assignment problem belongs to the class of _Bipartite matching problems with one sided
preferences_ (see [Manlove(2013): Algorithmics of Matching Under Preferences](https://books.google.de/books?id=jPO6CgAAQBAJ&lpg=PP1&hl=de&pg=PA4#v=onepage&q&f=true)). This is also called House Allocation problem. The name stems from the application where students are
assigned to campus housing, based on their preferences. When each house can only accomodate applicants to a fixed
capacity (as in our problem here) the problem is called Capacitated House Allocation problem (CHA). Since the preferences
are only given by one side the notion of stability is not relevant. Other optimality criteria have to be used. The
Hungarian algorithm as it is used here maximizes the number of applicants with their first choice.

## Installation

The python skript makes use of the [munkres package](https://pypi.python.org/pypi/munkres/) for python
(see also (http://software.clapper.org/munkres/)). So you have to install this package first:

    $ pip3 install munkres

## Usage

The preferences of each person must be stored as CSV file like in this example:

    name, team1, team2, team3
    Andreas, 3,2,1
    Markus, 3,2,1
    Jan, 2,3,1
    Andre, 3,1,2
    Thomas, 2,1,3

 To compute a possible assignment of the people to the three teams "team1", "team2" and "team3" with a capacity of 2 do

     $ python3 teambuilder.py <name_of_csv> 2
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
