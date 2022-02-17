"""
Lab 2 Task 2
"""
import json

def if_dict(file_name):
    """
    if the json file begins with dict
    """
    with open(file_name, 'r') as file: #twitter2.json
        data = json.load(file) #вичитування данних з відкритого файлу
    print(list(data.keys()))
    while True:
        inp_k = input("Enter a key:")
        if not inp_k:
            break
        if type(data) == list:
            inp_k = int(inp_k)
        data = data[inp_k] #заходим 'глибше'
        if type(data) == list:
            print(f'Number of elements: {len(data)}')
        elif type(data) == dict:
            print(f'Dict keys are: {list(data.keys())}')
        else:
            print(f'Value is: {data}')
            break
    return
def if_list(file_name):
    """
    if the json file begins with list
    """
    with open(file_name, 'r') as file:
        data = json.load(file)
        i = int(input('Enter an index of dict:'))
        print(list(data[i].keys()))
        while True:
            inp_k = input("Enter a key:")
            if not inp_k:
                break
            if type(data[i]) == list:
                inp_k = int(inp_k)
            data[i] = data[i][inp_k]
            if type(data[i]) == list:
                print(f'Number of elements: {len(data[i])}')
            elif type(data[i]) == dict:
                print(f'Dict keys are: {list(data[i].keys())}')
            else:
                print(f'Value is: {data[i]}')
                break
    return

if __name__ == "__main__":
    path = input("Enter the name of file:")
    if path == 'twitter1.json':
        if_list(path)
    elif path == 'twitter2.json':
        if_dict(path)
    else:
        print('You entered the wrong name of file')