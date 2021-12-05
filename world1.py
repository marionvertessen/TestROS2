from ressources import Interaction
from turtlesim_enacter import TurtlePyEnacter


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.memoire = []  # De la forme [action, anticipation]
        self.cycle_iteration = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        estdeja = False
        for i in range(len(self.memoire)):
            if self.memoire[i][0] == self._action and self.memoire[i][1] == outcome:
                estdeja = True
        if estdeja == False and self._action is not None:
            self.memoire.append([self._action, outcome])
        # print(self.memoire)
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        if self.cycle_iteration < 3:
            self._action = outcome
            self.cycle_iteration = self.cycle_iteration + 1
            # print(self.cycle_iteration)
        else:
            if outcome == 0:
                self._action = 1
            else:
                self._action = 0
            self.cycle_iteration = 0

        present = None  # On considere que l'action n'est pas presente dans la memoire
        for i in range(len(self.memoire)):  # On parcours la memoire
            # Si l'action est presente dans la memoire, on enregistre la valeur de l'anticipation
            if self.memoire[i][0] == self._action:
                present = self.memoire[i][1]
        if present != None:  # Si l'action est présente
            self.anticipated_outcome = present
        else:
            self.anticipated_outcome = 0
        return self._action


class Agent2:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.memoire = []  # De la forme [action, anticipation]
        self.cycle_iteration = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        estdeja = False
        for i in range(len(self.memoire)):
            if self.memoire[i][0] == self._action and self.memoire[i][1] == outcome:
                estdeja = True
        if estdeja == False and self._action is not None:
            self.memoire.append([self._action, outcome])
        # print(self.memoire)
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        if self._action is not None:
            if self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == 1:
                self.cycle_iteration = self.cycle_iteration + 1
                # print(self.cycle_iteration)
            elif self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == -1:
                if outcome == 0:
                    self._action = 1
                else:
                    self._action = 0
                self.cycle_iteration = 0
            else:
                if self._action == 0:
                    self._action = 1
                else:
                    self._action = 0
                self.cycle_iteration = 0
        else:
            self._action = 0

        present = None  # On considere que l'action n'est pas presente dans la memoire
        for i in range(len(self.memoire)):  # On parcours la memoire
            # Si l'action est presente dans la memoire, on enregistre la valeur de l'anticipation
            if self.memoire[i][0] == self._action:
                present = self.memoire[i][1]
        if present != None:  # Si l'action est présente
            self.anticipated_outcome = present
        else:
            self.anticipated_outcome = 0
        return self._action


class Agent3:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.memoire = []  # De la forme [action, anticipation]
        self.cycle_iteration = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        estdeja = False
        for i in range(len(self.memoire)):
            if self.memoire[i][0] == self._action and self.memoire[i][1] == outcome:
                estdeja = True
        if estdeja == False and self._action is not None:
            self.memoire.append([self._action, outcome])

        # print(self.memoire)
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        if self._action is not None:
            if self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == 1:
                self.cycle_iteration = self.cycle_iteration + 1
                # print(self.cycle_iteration)
            elif self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == -1:
                if self._action == 0:
                    self._action = 1
                elif self._action == 1:
                    self._action = 2
                else:
                    self._action = 0
                self.cycle_iteration = 0
            else:
                if self._action == 0:
                    self._action = 1
                elif self._action == 1:
                    self._action = 2
                else:
                    self._action = 0
                self.cycle_iteration = 0
        else:
            self._action = 0

        present = None  # On considere que l'action n'est pas presente dans la memoire
        for i in range(len(self.memoire)):  # On parcours la memoire
            # Si l'action est presente dans la memoire, on enregistre la valeur de l'anticipation
            if self.memoire[i][0] == self._action:
                present = self.memoire[i][1]
        if present is not None:  # Si l'action est présente
            self.anticipated_outcome = present
        else:
            self.anticipated_outcome = 0
        return self._action


class Agent4:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.memoire = []  # Interaction(t-1) : previous ; Interaction(t) : last
        self.cycle_iteration = 0
        self.previous_interaction = None
        self.last_interaction = None

    def action(self, outcome):
        """ tracing the previous cycle """
        # On enregistre dans la mémoire la valeur du cicle précédent

        if self._action is not None:
            self.previous_interaction = self.last_interaction
            self.last_interaction = Interaction.create_or_retrieve(self._action, outcome,
                                                                   self.hedonist_table[self._action][outcome])
        estdeja = False
        # print("taille mémoire : ", len(self.memoire))
        for i in range(len(self.memoire)):
            #print(self.memoire[i][1])
            #print(self.last_interaction)
            if self.memoire[i][0] == self.previous_interaction and self.memoire[i][1] == self.last_interaction :
                estdeja = True
                #print(estdeja)

        if (estdeja == False) and (self._action is not None) and (self.previous_interaction is not None):
            self.memoire.append([self.previous_interaction, self.last_interaction])

        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")")

        """ Computing the next action to enact """
        if self._action is not None:
            last = self.last_interaction
            list_actions = []
            list_bad_actions = []
            for interactions in self.memoire:
                if (interactions[0] == last):
                    if (interactions[1].valence == 1):
                        list_actions.append(interactions)
                    else :
                        list_bad_actions.append(interactions[1].action)

            if len(list_actions) != 0:
                print("bonne action")
                self._action = list_actions[0][1].action
                self.anticipated_outcome = list_actions[0][1].outcome

            elif len(list_bad_actions) != 0:
                print("mauvaise action à éviter")
                for action in list_bad_actions:
                    if action == 0:
                        self._action = 1
                    else:
                        self._action = 0

            else:
                print("action aléatoire")
                if self._action == 0:
                    self._action = 1
                else:
                    self._action = 0
                self.anticipated_outcome = None

            # if self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == 1:
            #     self.cycle_iteration = self.cycle_iteration + 1
            #     # print(self.cycle_iteration)
            # elif self.cycle_iteration < 3 and self.hedonist_table[self._action][outcome] == -1:
            #     if outcome == 0:
            #         self._action = 1
            #     else:
            #         self._action = 0
            #     self.cycle_iteration = 0
            # else:
            #     if self._action == 0:
            #         self._action = 1
            #     else:
            #         self._action = 0
            #     self.cycle_iteration = 0
        else:
            self._action = 0

        """present = None  # On considere que l'action n'est pas presente dans la memoire
        for i in range(len(self.memoire)):  # On parcours la memoire
            # Si l'action est presente dans la memoire, on enregistre la valeur de l'anticipation
            if self._action == self.last_interaction.action and self.previous_interaction == self.memoire[i][0]:
                #print(self.memoire[i][1])
                #print(self.memoire[i][0])
                present = self.memoire[i][1]

        if present != None:  # Si l'action est présente
            self.anticipated_outcome = present.outcome
            #print(present.outcome)
        else:
            self.anticipated_outcome = None"""
        return self._action


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


class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """

    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome


# TODO Define the hedonist values of interactions (action, outcome)
#hedonist_table = [[-1, 1], [1, -1]]
#hedonist_table = [[1, 1], [1, 1]]
hedonist_table = [[-1,1], [-1,1]]
#hedonist_table = [[1, -1, -1], [-1, 1, -1], [-1, -1, 1]]
# TODO Choose an agent
# a = Agent(hedonist_table)
# a = Agent2(hedonist_table)
# a = Agent3(hedonist_table)
a = Agent4(hedonist_table)
# TODO Choose an environment
#e = Environment1()
#e = Environment2()
e = Environment3()
# e = TurtleSimEnacter()
#e = TurtlePyEnacter()

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(20):
        action = a.action(outcome)
        outcome = e.outcome(action)
