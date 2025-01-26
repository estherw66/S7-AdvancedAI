# RL - Exercise

## Description
Main: Select a discrete environment from Gymnasium, Frama Foundation.

Try out Q-learning and study the impact of the hyper-parameters on the learning, in particular, study the exploration-exploitation trade-off.

Make sure you are making plots that show the agent is learning, for example via average reward per episode as a function of the training epoch (see slides) for different choices of hyper-parameters.
Some ideas (optional, but recommended):
On Frozen Lake (Frozen Lake - Gymnasium Documentation (farama.org) Links to an external site.) , shows that adding a negative reward for each move and a negative reward for each time the agent falls in the hole makes learning faster.

On Frozen Lake,  compare the effect of having the is_slippery on or off (this makes the environment stochastic when on or deterministic when off)

Compare the epsilon-greedy exploration against the Boltzmann Policy (soft-max applied to the Q table). Investigate the temperature of the Boltzmann.

Show how craving works in your environment (large Q values when favorable outcomes are about to happen). Make a heatmap plot of the Q-table, and use arrows to show optimal behavior.

Reason how should you shape the reward, what is the impact of the size of the negative penalty when the agents fall in the hole?

[Optional] Implement prioritized experience replay.

 

Assign numbers to all figures and include the experimental settings in their captions (e.g., slippery on/off, exploration strategy such as epsilon-greedy or Boltzmann).

Provide a clear summary at the end that discusses the specific results in detail.

Design plots to facilitate performance comparison by overlaying different methods in a single plot. For highly fluctuating curves, consider using a moving average for better clarity.




After doing the steps above, if you would like to try out deep-Q learning (where you use a Neural Network instead of a Q-table) you can do the tasks below [optional]

Try out an environment with simple actions for example Cart Pole - Gymnasium Documentation (farama.org) Links to an external site. This can be any game, but remember that you have to be able to access or being able to calculate the three main parameters of reinforcement learning: state, action, and reward.

## Feedback
Good job. You put quite some effort into it. 

a few tips for plotting: 
Give figures a number, put the experimental settings in the figure description. make plots in a way that help you compare performance by overlaying different methods in one plot. Make the summary explain the overall agent performance also. If there is a highly fluctuating curve, it helps to plot a moving average. 