import json
import csv

import numpy as np

"""
Code Reference: https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
"""
if __name__=='__main__':
    # Opening JSON file and loading the data
    # into the variable data
    with open('data/training_set_task1.txt') as json_file:
        input_data = json.load(json_file)

    # now we will open a file for writing
    data_file = open('data/propagandaMemeClassification_training.csv', 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    labels = ["Loaded Language",
              "Name calling/Labeling",
              "Smears",
              "Appeal to fear/prejudice",
              "Black-and-white Fallacy/Dictatorship",
              "Exaggeration/Minimisation",
              "Slogans",
              "Misrepresentation of Someone's Position (Straw Man)",
              "Obfuscation, Intentional vagueness, Confusion",
              "Presenting Irrelevant Data (Red Herring)",
              "Whataboutism",
              "Causal Oversimplification",
              "Appeal to authority",
              "Flag-waving",
              "Doubt",
              "Thought-terminating cliché",
              "Bandwagon",
              "Reductio ad hitlerum",
              "Repetition",
              "Glittering generalities (Virtue)"
              ]


    for row in input_data:
        if count == 0:
            # Writing headers of CSV file
            header = ["text"] + labels
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        populateRow = [row["text"]]
        list_labels = np.zeros(20)
        for l in row['labels']:
            list_labels[labels.index(l)] = 1
        csv_writer.writerow(populateRow + list(list_labels))

    data_file.close()
