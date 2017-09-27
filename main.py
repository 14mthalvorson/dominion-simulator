from Dominion import *
import matplotlib.pyplot as plt

sim = Simulator()
#sim.reset()
sim.run(50000)
sim.graph()
