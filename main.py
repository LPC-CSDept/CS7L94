def changeKey(org_dict, org_key, new_key):
    ##################################################
    # Code your program here
    ##################################################


def printDict(p_dict):
    ##################################################
    # Code your program here
    #########################################
    print('***************')
    for k, v in p_dict.items():
        print(f'{k} : \t {v}')


def main():
    emp_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    printDict(emp_dict)
    org_keyval = 'city'
    new_keyval = 'location'
    changeKey(emp_dict, org_keyval, new_keyval)
    printDict(emp_dict)


if __name__ == '__main__':
    main()
