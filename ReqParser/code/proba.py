import xml.etree.ElementTree as ET

context = ET.iterparse("Eng8_SW_Tests.xml", events=("start", "end"))

path = []
reqs = []
meqs = []
ident_value = ''
desc_value = ''
for event, elem in context:
    tag = elem.tag
    value = elem.text
    ident = tag == 'ident'
    description = tag == 'description'
    if event == 'start':
        path.append(tag)

    elif event == 'end':
        # process the tag
        if ident:
            if 'testcase' in path:
                ident_value = value
                reqs.append(tag)
                meqs.append(ident_value)
        if description:
            if 'ident' in reqs:
                desc_value = value
                meqs.append(desc_value)
                #print(meqs)
        #reqs[ident_value].append(desc_value)

            #else:
                #print()
        #path.pop()
#print(path)

#my_list_in_list = [ ['001', ['AAA', 'BBB']], ['002', ['AAA']]]
#my_list_in_list.append(['0002', ['CCC']])
#my_list_in_list.append(['002', ['CCC']])
'''#context = iter(context)
on_testcase_tag = False
on_ident_tag = False
for event, elem in context:
    tag = elem.tag
    value = elem.text

    #if value:
        #value = value.encode('utf-8').strip()
    if event == 'start':
        if tag == 'testcase':
            on_testcase_tag = True
        elif tag == 'description':
            if on_testcase_tag:
                print("Requirement number is %s" % value)
        else:
            print("WHERE IS THAT??? ---> %s " % value)
    if event == 'end' and tag == 'testcase':
        on_testcase_tag = False
    elem.clear()
'''
