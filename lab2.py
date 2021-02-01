import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)


class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program = program


loc_A,loc_B,loc_C,loc_D='A','B','C','D'

class vaccumEnvironment():

    def __init__(self):
        self.status={
                      loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean','Dirty'])
                      }

    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):
        if action=='Top Right': agent.location=loc_B
        elif action=='Top Left': agent.location=loc_A
        elif action=='Bottom Right': agent.location=loc_D
        elif action=='Bottom Left': agent.location=loc_C
        elif action=='Suck':
            if self.status[agent.location]=='Dirty':
                self.status[agent.location]='Clean'


class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            print(percepts)
            action=table.get(tuple(percepts))
            print('Agent perceives ', percept, ' and does ', action)
            return action
        self.program=program



def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),):'Right',
              ((loc_A,'Dirty'),):'Suck',
              ((loc_B,'Clean'),):'Left',
              ((loc_B,'Dirty'),):'Suck',

              ((loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
              ((loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',

              ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_A, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_A, 'Dirty'), (loc_A, 'Dirty')): 'Suck',

              ((loc_B, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_B, 'Clean'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Clean'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',

              ((loc_B, 'Dirty'), (loc_A, 'Clean')): 'Right',
              ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
              ((loc_B, 'Dirty'), (loc_B, 'Dirty')): 'Right',
              ((loc_B, 'Dirty'), (loc_A, 'Dirty')): 'Suck',



              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Clean')): 'Right',
              ((loc_A, 'Clean'), (loc_A, 'Clean'), (loc_A, 'Dirty')): 'Suck',
            }
    return tableDrivenAgent(table)



Tagent=tableDrivenVaccumAgent()
env=vaccumEnvironment()
env.add_object(Tagent)


for _ in range(10):
    action=Tagent.program(env.percept(Tagent))
    env.execute_action(Tagent,action)
