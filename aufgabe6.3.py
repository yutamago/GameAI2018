from dt_learning import dt_learning, prettyprint_tree

if __name__ == '__main__':
    data = {
        'sky': ['sunny', 'sunny', 'rainy', 'sunny', 'sunny'],
        'air': ['warm', 'warm', 'cold', 'warm', 'warm'],
        'humid': ['normal', 'high', 'high', 'high', 'normal'],
        'wind': ['strong', 'strong', 'strong', 'strong', 'weak'],
        'water': ['warm', 'warm', 'warm', 'cool', 'warm'],
        'forecast': ['same', 'same', 'change', 'change', 'same'],
        'attack': ['+', '+', '-', '+', '-']
    }

    attributes = columns = ["sky", "humid", "wind", "water", "forecast"]
    attributes.append("attack")

    decisionTree = dt_learning(data, attributes)
    prettyprint_tree(decisionTree)
