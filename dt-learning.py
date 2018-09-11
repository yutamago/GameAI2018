def classification(example):
    return 0

def allHaveSameClassification(examples):
    return False

# information gain -> entropy
def importance(arg, examples):
    return 0

def plurality_val(examples):
    return examples[0]

def dt_learning(examples, attributes, parent_examples):
    if empty(examples):
        return plurality_val(parent_examples)
    elif allHaveSameClassification(examples):
        return classification(examples[0])
    elif empty(attributes):
        plurality_val(examples)
    else:
        attributes_importance =
        A = argmax(lambda importance(a, examples))



res = dt_learning([], [], [])
print(res)
