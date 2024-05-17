from math import log2
import pandas as pd


def main():
    data = pd.read_csv("Information Gain.csv")
    decision_tree(data)


def decision_tree(data):
    priority = {}
    max_priority = (0, '')  # IG, name of attribute

    columns_except_last = data.iloc[:, :-1]
    successes = data.iloc[:, -1].value_counts()[1]  # calculate the number of successes.
    # value_counts() returns a count of unique values found in the column

    for column in columns_except_last.columns:
        attributes = {} # dict iwht a counter of

        row_counter = 0
        for value in data[column]:
            if value not in attributes.keys():  # calculate individual attribute instances
                attributes[value] = [1, 0]
            else:
                attributes[value][0] += 1

            if data.iloc[row_counter, -1]:  # if success for given case
                attributes[value][1] += 1

            row_counter += 1

        result = calculate_entropy(successes / data.shape[0])  # at first we calculate B(positive, all values)
        # data.shape returns a tuple representing its dimensions

        print(f"IG(D, {column})=H({successes}/{data.shape[0]})", end=" ")

        for attribute, attribute_stats in attributes.items():
            if attribute_stats[1] != 0 and attribute_stats[1] != attribute_stats[0]:
                result -= attribute_stats[0] / data.shape[0] * calculate_entropy(attribute_stats[1] / attribute_stats[0])
                print(f"- {attribute_stats[0]}/{data.shape[0]}*H({attribute_stats[1]}/{attribute_stats[0]})", end=" ")

        print(f"= {result}")
        if max_priority[0] < result:
            max_priority = (result, column)

        priority[column] = (result, attributes)

    print('\n', max_priority[1], priority[max_priority[1]])


    print("Node", priority[max_priority[1]][1])
    for attribute, attribute_stats in priority[max_priority[1]][1].items():
        if attribute_stats[1] != 0 and attribute_stats[1] != attribute_stats[0]:
            print("Branch with attribute", attribute , "from", max_priority[1], '\n')
            filtered_data = data[data[max_priority[1]] == attribute]
            print(filtered_data)
            filtered_data = filtered_data.drop(max_priority[1], axis=1)
            decision_tree(filtered_data)


def calculate_entropy(q):
    """
    Function that calculates binary entropy
    :param q: q in [0,1]
    :return: binary entropy
    """
    return -(q * log2(q) + (1 - q) * log2(1 - q))


def information_gain(successes, total_amount, attr1_total, attr1_success, attr2_success,
                     attr3_total=0, attr3_success=0):

    attr2_total = total_amount - attr1_total - attr3_total
    q3 = 0.5 if attr3_total == 0 else attr3_success/attr3_total

    result = calculate_entropy(successes / total_amount) - (
                attr1_total / total_amount * calculate_entropy(attr1_success / attr1_total)
                + attr2_total / total_amount * calculate_entropy(attr2_success/attr2_total)
                + attr3_total / total_amount * calculate_entropy(q3)
                )

    return result


#print(information_gain(5, 12, 6, 4, 1))
if __name__ == "__main__":
    main()
