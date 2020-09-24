import re

def detail(bs_obj):
    left_pane = bs_obj.find(attrs={"class": 'left-pane'})
    right_pane = bs_obj.find(attrs={"class": 'right-pane'})

    attribute = re.compile(r'<p>(.*?)</p>')

    keys = []
    values = []

    for i in left_pane:
        if len(attribute.findall(str(i))) > 0:
            keys.append(attribute.findall(str(i))[0])

    for i in right_pane:
        if len(attribute.findall(str(i))) > 0:
            values.append(attribute.findall(str(i))[0])

    for i, j in zip(keys, values):
        print("{:<20} : {:>20}".format(i, j))
