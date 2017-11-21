from __future__ import division
from collections import defaultdict
from math import log

import os


def train(samples):
    classes, freq = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for feats, label in samples:
        classes[label] += 1  # count classes frequencies
        for feat in feats:
            freq[label, feat] += 1  # count features frequencies

    for label, feat in freq:  # normalize features frequencies
        freq[label, feat] /= classes[label]
    for c in classes:  # normalize classes frequencies
        classes[c] /= len(samples)

    return classes, freq  # return P(C) and P(O|C)


def classify(classifier, feats):
    classes, prob = classifier
    return min(classes.keys(),  # calculate argmin(-log(C|O))
               key=lambda cl: -log(classes[cl]) + \
                              sum(-log(prob.get((cl, feat), 10 ** (-7))) for feat in feats))

samples = []
for i in range(9):
    folder_name = 'part' + str(i+1)
    for filename in os.listdir(folder_name):
        features = []
        with open(folder_name + '\\' + filename, 'r') as f:
            for line in f:
                for word in line.split(" "):
                    line.replace('\n', '')
                    if word.lower() == 'subject:':
                        continue
                    try:
                        features.append(int(word))
                    except ValueError:
                        continue
        if filename.__contains__('sp'):
            label = 0
        else:
            label = 1
        samples.append([features, label])
classifier = train(samples)
folder_name = 'part' + str(10)
files_count = 0
right_answers = 0
for filename in os.listdir(folder_name):
    features = []
    with open(folder_name + '\\' + filename, 'r') as f:
        for line in f:
            for word in line.split(" "):
                line.replace('\n', '')
                if word.lower() == 'subject:':
                    continue
                try:
                    features.append(int(word))
                except ValueError:
                    continue
    if filename.__contains__('sp'):
        label = 0
    else:
        label = 1
    class_predicted = classify(classifier, features)
    files_count += 1
    right_answers += int(class_predicted == label)
print(right_answers/files_count)