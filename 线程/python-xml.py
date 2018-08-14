# -*- coding:utf-8 -*-
# author: "XiangLei Kong"

import xml.etree.ElementTree as ET
tree = ET.parse("argument.xml")
tree2 = ET.parse("argument2.xml")
root = tree.getroot()
root2 = tree2.getroot()
root_dict = {}
root2_dict = {}
for child in root:
    root_dict[child.tag]={}
    root_dict[child.tag][child.tag] = child.text
    for i in child:
        root_dict[child.tag][i.tag] = i.text
for child in root2:
    root2_dict[child.tag]={}
    root2_dict[child.tag][child.tag] = child.text
    for i in child:
        root2_dict[child.tag][i.tag] = i.text
# for child in root:
#     if root_dict[child.tag][child.tag] != root2_dict[child.tag][child.tag]:
#         print (child.tag)
#         print (root_dict[child.tag][child.tag])
#         print (root2_dict[child.tag][child.tag])
#     for i in child:
#         if root_dict[child.tag][i.tag] != root2_dict[child.tag][i.tag]:
#             print (child.tag,i.tag)
#             print (root_dict[child.tag][i.tag])
#             print (root2_dict[child.tag][i.tag])
#             root2_dict[child.tag][i.tag] = root_dict[child.tag][i.tag]

for child in root2:
    if root_dict[child.tag][child.tag] != root2_dict[child.tag][child.tag]:
        print (child.tag)
        print (root_dict[child.tag][child.tag])
        print (root2_dict[child.tag][child.tag])
        child.text = root_dict[child.tag][child.tag]
    for i in child:
        if root_dict[child.tag][i.tag] != root2_dict[child.tag][i.tag]:
            i.text = root_dict[child.tag][i.tag]
            print (child.tag,i.tag)
            print (root_dict[child.tag][i.tag])
            print (root2_dict[child.tag][i.tag])
            root2_dict[child.tag][i.tag] = root_dict[child.tag][i.tag]
tree2.write("argument2.xml")