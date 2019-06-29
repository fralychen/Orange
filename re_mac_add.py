import re

def cw_mac_add(mac_add):
    #mac_add='00-50-56-C0-00-08'

    result = re.findall('\S',mac_add)
    print(result)
    rmkey = [2,8,14]


    a_index = [i for i in range(len(result))]
    a_index = set(a_index)
    b_index = set(rmkey)
    index = list(a_index-b_index)
    result = [result[i] for i in index]
    print(result)
    str_result = "".join(result)
    print(str_result)
    


def read_csv():
    csvFile = open("netexcel.CSV","r")
    reader = csv.reader(csvFile)
    for item in reader:
        print(item)






cw_mac_add('00-50-56-C0-00-08')
