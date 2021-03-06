import json
import math


def possibilityOfValueInData(value, data):
    countAll = len(data)
    data_for_this_value = list(filter(lambda _label: _label == value, data))
    countValue = len(data_for_this_value)
    return countValue / countAll


def entropy(data):
    _entropy = 0
    data_set = set(data)
    for label in data_set:
        p = possibilityOfValueInData(label, data)
        _entropy += p * math.log2(p)
    return -_entropy


# B(...)
def binary_entropy(q):
    if q == 0.0 or q == 1.0:
        return 0
    else:
        return -(q * math.log2(q) + (1 - q) * math.log2(1 - q))


def filterImportance(columnData, label, goalData):
    ret = []
    for x in range(len(columnData)):
        if columnData[x] == label:
            ret.append(goalData[x])
    return ret


def importance(data, dataColumn, goalColumn, goalValue):
    goalData = data[goalColumn]
    pGoal = possibilityOfValueInData(goalValue, goalData)

    columnData = data[dataColumn]
    columnData_set = set(columnData)

    pLabel = {label: possibilityOfValueInData(label, columnData) for label in columnData_set}

    entropy_sum = binary_entropy(pGoal)

    for label in columnData_set:
        filteredGoalData = filterImportance(columnData, label, goalData)

        p = possibilityOfValueInData(goalValue, filteredGoalData)
        entropy_sum -= pLabel[label] * binary_entropy(p)

    return entropy_sum


def plurality_val(data, goalColumn=None, goalValue=None):
    if data == None:
        return None

    highest_importance = -1
    ig_column = None

    for column in data:
        if column != goalColumn:
            ig = importance(data, column, goalColumn, goalValue)
            if ig > highest_importance:
                highest_importance = ig
                ig_column = column

    return ig_column


def allHaveSameClassification(examples, attributes):
    goalColumn = examples[attributes[-1]]

    if len(goalColumn) == 0:
        return True

    classification = goalColumn[0]

    for result in goalColumn:
        if result != classification:
            return False
    return classification


def filterExamples(examples, column, attribute):
    newExamples = {}
    rowsToRemove = [i for i in range(len(examples[column])) if examples[column][i] != attribute]

    for i in range(len(examples[column])):
        for _column in examples.keys():
            if i not in set(rowsToRemove) and _column != column:
                if _column not in newExamples.keys():
                    newExamples[_column] = []
                newExamples[_column].append(examples[_column][i])
    return newExamples


def dt_learning(examples, attributes, parent_examples=None):
    classification = allHaveSameClassification(examples, attributes)

    if len(examples) == 0:
        return plurality_val(parent_examples)
    elif classification != False:
        return classification
    elif len(attributes) == 1:
        return plurality_val(examples, attributes[0])
    else:
        goalColumn = attributes[-1]
        goalValue = examples[goalColumn][0]
        A = plurality_val(examples, goalColumn, goalValue)
        A_str = A + "?"

        tree = {
            A_str: {}
        }
        for attribute in set(examples[A]):
            subtree = dt_learning(filterExamples(examples, A, attribute), [x for x in attributes if x != A], examples)
            tree[A_str][attribute] = subtree
        return tree

def prettyprint_tree(tree):
    print(json.dumps(tree, sort_keys=True, indent=4))
