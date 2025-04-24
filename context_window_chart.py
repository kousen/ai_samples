import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
models = ['GPT-4o', 'Claude', 'Gemini', 'Mistral']
context_windows = [128, 200, 1024, 131]  # in K tokens

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(models, context_windows, color=['#4285F4', '#34A853', '#FBBC05', '#EA4335'])

# Add labels and title
plt.xlabel('AI Model')
plt.ylabel('Context Window Size (K tokens)')
plt.title('Context Window Size Comparison Across AI Models')

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 20,
             f'{height}K', ha='center', va='bottom')

# Adjust y-axis to make Gemini's large value more visible
plt.ylim(0, 1200)  # Set y-axis limit to accommodate labels

# Add grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure
plt.tight_layout()
plt.savefig('context_window_comparison.png', dpi=300)

# Display the chart
plt.show()
