import matplotlib.pyplot as plt
from urllib.request import urlopen
import seaborn as sns
import numpy as np

# Theme settings -------------------------------------------------------------------------------------------------------

sns.set_theme()
sns.set_style("ticks")
sns.set_context("paper")
sns.axes_style()
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

# HTML settings --------------------------------------------------------------------------------------------------------

link = "https://www.gutenberg.org/cache/epub/100/pg100.txt"  # Read file from gutenberg project
file = urlopen(link)  # open the file in the url
text = file.read().lower().decode('utf-8')  # reads the file, converts all the words and converts the format to UTF-8
word_text = text.split(' ')  # splits the text with a spacer, otherwise you would be counting characters, not words.
filtered_text = filter(lambda x: x.isalpha(), word_text)  # filters the text so all punctuation points.

# Find the word frequency ----------------------------------------------------------------------------------------------

d = dict()  # create an empty dictionary

# Loop through each line of the file
for line in filtered_text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

top_results = sorted(d.items(), key=lambda x: -x[1])[:30]  # second filter to showcase the top results (set a 30)

labels, values = zip(*top_results)

indSort = np.argsort(values)[::-1]  # sort the values in descending order

labels = np.array(labels)[indSort]  # rearrange the data
values = np.array(values)[indSort]  # rearrange the data

indexes = np.arange(len(labels))

plt.bar(indexes, values)
plt.xticks(indexes, labels)
plt.xticks(rotation=90)
plt.show()
