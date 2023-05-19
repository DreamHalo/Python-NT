def lst(first_lst:list,second_list:list,lst:list):
    dct={}
    for i in range(len(first_lst)):
        dct[first_lst[i]]={f'{second_list[i]}':lst[i]}
    print(dct)