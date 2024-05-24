# Bruce Provencher
# 05 MAY 2021
# Python List & Stats
scores = []
def build_list():

    num_items = int(input('How many items do you want to add to your list today? (Example: 4)\n'))
    for j in range(num_items):
        list_item = int(input('Enter an integer to add to your list:\n'))
        #scores.append(list_item, scores[j])
        scores.append(list_item)
    # Print contents of the list
    return scores

def print_list(list_name):
    for k in range(len(list_name)):
        print(f'List item #{k + 1} : {list_name[k]}')


def show_list_stats(list_name):
    print(f'Minimum value in list: {min(list_name)}')
    print(f'Maximum value in list: {max(list_name)}')
    print(f'Average of list values: {sum(list_name) / len(list_name)}')

    # Calculate the list's median value
    scores.sort()
    mid = len(scores) // 2
    res = (scores[mid] + scores[~mid]) / 2

    print(f'Median value of list: {res}')
        
my_list = build_list()
print_list(my_list)
show_list_stats(my_list)
