def deleteDict(org_dict, keys):
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
    keys = ['name', 'salary']
    deleteDict(emp_dict, keys)
    printDict(emp_dict)


if __name__ == '__main__':
    main()
