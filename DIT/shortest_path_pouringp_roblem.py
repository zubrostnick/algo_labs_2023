"""
In the standard pouring problem, there are two glasses of different capacity.
Legal actions are filling a glass, emptying a glass or pouring as much as
possible of a glass into the other one. Glutting is not legal. Given an initial
filling, a goal filling must be achieved by applying these actions. The
shortest path of actions must be returned or no path in case the problem
is not solvable for a certain configuration of start, goal and capacities.
Sample configuration:
Capacities: 418 and 986
Start: 0 and 0
Goal: 6 and 0
The shortest solution requires 618 actions.
Professor Patrick GLAUNER Algorithms and Data Structures 2023 Summer Term 59 / 433
"""


def shortest_path_search(start, successors, is_goal):
    if is_goal(start):
        return [start]
 
    explored = set([start])
    frontier = [[start]]  # ordered list of path we have blazed
# а ну скажи мені чого ти хочеш,
# чого ти голову мужчині морочиш
# ти не людина є, а просто зараза
# якби я знав, то би застрілився зразу

Fail = []
start = (0, 0)


def is_goal(state):
    return state == (6, 0)


def successors(X, Y):
    def sc(state):
        x, y = state
        assert x <= X and y <= Y
        return {
            (X, y): 'fill x',
            (x, Y): 'fill y',
            (0, y): 'empty x',
            (x, 0): 'empty y',
            (0, y + x) if y + x <= Y else (x - (Y - y), Y): 'x->y',
            (x + y, 0) if x + y <= X else (X, y - (X - x)): 'x<-y'
        }

    return sc


if __name__ == "__main__":
    res = shortest_path_search((0, 0), successors(418, 986), lambda state: state == (6, 0))
