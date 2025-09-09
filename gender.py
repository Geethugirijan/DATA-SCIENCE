import matplotlib.pyplot as plt
import numpy as np

groups = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
men_scores = [22, 30, 35, 35, 26]
women_scores = [25, 32, 30, 35, 29]

n_groups = len(groups)
index = np.arange(n_groups)
bar_width = 0.35

# Bars for men
plt.bar(index, men_scores, bar_width, label='Men', color='DeepSkyBlue')

# Bars for women (shifted by bar_width)
plt.bar(index + bar_width, women_scores, bar_width, label='Women', color='DeepPink')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(index + bar_width / 2, groups)
plt.legend()

plt.tight_layout()
plt.savefig('graph9')
#plt.show()
