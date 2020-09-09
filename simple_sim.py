from blackjack import game
import matplotlib.pyplot as plt
import utils
import numpy as np

targets = [15, 16, 17, 18, 19]
win, draw, loss = [0] * len(targets), [0] * len(targets), [0] * len(targets)

# Setting up two plots
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

for index in range(len(targets)):
    # Set up initial parameters
    initial_amount = 10000
    wager = 100
    curr_amount = initial_amount
    target = targets[index]
    
    # Array to store values, to plot
    xGame, yAmount = [], []
    for i in range(1000):
        utils.block_print() # Blocks printing through games
        value = game(target)
        utils.enable_print()
        if value == 1:
            win[index] += 1
        elif value == 0:
            draw[index] += 1
        else:
            loss[index] += 1
        curr_amount += value * wager
        xGame.append(i+1)
        yAmount.append(curr_amount)
    
    # Plotting amount vs games curve
    ax1.plot(xGame, yAmount, label=str(target))
    ax1.set_title('Amount vs Games')
    ax1.set_xlabel('Games')
    ax1.set_ylabel('Amount')
    ax1.legend()

# Plot bars for win, loss, draw with different strategies
width = 0.6
x = np.arange(len(targets))
win_bar = ax2.bar(x - width/3, win, width/3, label='Wins')
loss_bar = ax2.bar(x, loss, width/3, label='Loss')
draw_bar = ax2.bar(x + width/3, draw, width/3, label='Draws')

ax2.set_title('Wins Loss Draws by Strategy')
ax2.set_xticks(x)
ax2.set_xticklabels(targets)
ax2.set_xlabel('Count')
ax2.set_ylabel('Stop Target')
ax2.legend()
plt.show()