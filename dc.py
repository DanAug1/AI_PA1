""" starter file for pa1: dogcat """

import search       # AIMA module for search problems
import gzip         # read from a gzip'd file

# file name for the dictionary, with one word per line.  Each line
# will have a word followed by a tab followed by a number, e.g.
#   and     0.07358445
#   for     0.18200336

dict_file = "words34.txt.gz"

# dictionary is a dict to hold legal 3 and 4 letter words with their
# frequencies based on a sample of a large text corpus. The dict's
# keys are the words and its values are their frequencies

# load words into the dictionary dict
dictionary = {}
for line in gzip.open(dict_file, 'rt'):
    word, n = line.strip().split('\t')
    n = float(n)
    dictionary[word] = n



class DC(search.Problem):
    """DC is a subclass of the AIMA search files's Problem class. Its init
       method takes three arguments: the initial word, goal word, and cost method.
       A state is represented as a lowercase string of three or four
       ascii characters.  Both the initial and goal states must be
       words of the same length and they must be in the dict
       dictionary. The cost argument specifies how to measure the
       cost of an action and can be 'steps', 'scrabble' or 'frequency'
       """

    def __init__(self, initial='dog', goal='cat', cost='steps'):

        if not (3 <= len(initial) <= 4) or not (3 <= len(goal) <= 4):
            raise ValueError("Arg length for initial and goal must be 3 or 4 characters long")
        if (len(initial) != len(goal)):
            raise ValueError("Character lengths for initial and goal must be the same")

        self.initial = initial
        self.goal = goal

        if cost.casefold() not in ["steps", "scrabble", "frequency"]:
            raise ValueError("Cost method must be 'steps' or 'scrabble' or 'frequency'")
        else:
            self.cost = cost.casefold()



    def actions(self, state):
        #TODO: complete this
        """ Given a state (i.e., a word), return a list or iterator of
        all possible next actions.  An action is defined by position
        in the word and a character to put in that position.  But the
        result must be a legal word, i.e., in our dictionary, and it
        should not be the same as the state, i.e., don't replace a
        character with the same character """

        stateList = []


        #is this supposed to only do one index instead of all possible changes?
        for i in range(len(state)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                if letter == state[i]:
                    continue

                newWord = state[:i] + letter + state[i+1:]

                if newWord in dictionary:
                    stateList.append((i, letter))

        return stateList



    def result(self, state, action):
        #TODO: complete this
        """ takes a state and an action and returns a new state """

        #unpack the tuple from actions()
        index, letter = action

        return state[:inex] + letter + state[index+1:]



    def goal_test(self, state):
        #TODO: complete this
        """ returns True iff state is a goal state for this problem instance """

        return state == self.goal



    def path_cost(self, c, state1, action, state2):
        #TODO: complete this
        #how much has my current change cost me? 1 by 1????
        #after using chatgpt and asking about the abstractions between the heuristic function
        #and the path_cost function, whatever cost type given for __init__ will be used as
        #the controller to decide which math needs to be used to calculate cumulative cost
        #of each state transition
        """ Returns the cost to get to state2 by applying action in
        state1 given that c is the cost to get up to state1. For the 
        the dc problem, you will have to check what
        cost metric (self.cost) is being used for this problem instance,
        i.e., is it steps, scrabble or frequency """
        pass



    def __repr__(self):
        #TODO: complete this
        """" return a suitable string to represent this problem instance """
        pass



    def h(self, node):
        #TODO: complete this
        #How much do i predict the final cost will be???
        """Heuristic: returns an estimate of the cost to get from the
        state of the node to the goal state. The heuristic's value should
        depend on the Problem's cost parameter, self.cost (i.e., steps, scrabble
        or frequency), as this will effect the estimate cost to get to
        the nearest goal. """
        pass
