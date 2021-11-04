#!/usr/bin/env python
# TODO Import the Turtlesim environment when ROS is installed
# from turtlesim_enacter import TurtleSimEnacter

# Olivier Georgeon, 2020.
# This code is used to teach Develpmental AI.


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.anticipated_outcome = 0
        self.memoire = [] #De la forme [action, anticipation]
        self.cycle_iteration = 0

    def action(self, outcome):
        """Interprete le resultat"""
        if len(self.memoire) == 0:
            memoire
         if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")
        if self.cycle_iteration < 4:
            self._action = outcome
            self.cycle_iteration = self.cycle_iteration + 1
        else:
            if outcome == 0:
                self._action = 1
            else:
                self._action = 0
            self.cycle_iteration = 0

        """On veut que l'anticipation soit relier à l'action
        Si le robot fait l'action 1 alors il anticipe 1
        Si le robot fait l'action 0 alors il anticipe 0
        On part du principe qu'il commence par 0 
        S'il ne connait pas l'action, il teste la caleur de l'outcome précédent"""


        #Si la memoire est vide on propose 0
        if len(self.memoire) == 0:
            self.anticipated_outcome = 0
        else :
            present = None #On considere que l'action n'est pas presente dans la memoire
            for i in range(len(self.memoire)): #On parcours la memoire
                # Si l'action est presente dans la memoire, on enregistre la valeur de l'anticipation
                if self.memoire[i][0] == self._action:
                    present = self.memoire[i][1]
            if present != None : #Si l'action est présente
                self.anticipated_outcome = present
            else :
                self.anticipated_outcome = 0


        return self._action


    def anticipation(self):
        """ Returning the anticipated outcome that was computed when choosing the action """
        return self.anticipated_outcome

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]
        return anticipation_satisfaction, hedonist_satisfaction



class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """
    def outcome(self, action):
        # return int(input("entre 0 1 ou 2"))
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """
    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(10):
        action = agent.action(outcome)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))


# TODO Define the hedonist values of interactions (action, outcome)
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent(hedonist_table)
# TODO Choose an environment
e = Environment1()
# e = Environment2()
# e = TurtleSimEnacter()

world(a, e)