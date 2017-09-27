from Dominion import *
import matplotlib.pyplot as plt

sim = Simulator()
sim.reset()
sim.run(1, output=True)
sim.graph()
