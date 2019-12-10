import xml.etree.ElementTree as ET


# parse a xml file
def parse_xml(file):
    a = ET.parse(file)
    b = a.getroot()
    return b


# returns a list of iterations/tags in a chapter
def get_iterations(root):
    elements = [elem.tag for elem in root.iter()]
    return elements


# returns all iterations in a chapter, without duplicates
def get_iterations_nondup(root):
    elements = [elem.tag for elem in root.iter()]
    elements = list(dict.fromkeys(elements))
    return elements

# prints attributes of all sections in a chapter
def get_sections(root):
    for section in root.iter("{http://docbook.org/ns/docbook}section"):
        print(section.tag, section.attrib)

# get text of all titles
def get_titles(root):
    for title in root.iter("{http://docbook.org/ns/docbook}title"):
        print(title.text)


# print and return a list of all cross-references in a text
def get_xrefs(root):
    xrefs = []
    for elem in root.iter('{http://docbook.org/ns/docbook}xref'):
        item = elem.attrib
        xrefs.append(item)
    print(xrefs)
    print("This chapter has this amount of xrefs: " + str(len(xrefs)))
    return xrefs

# get all cross references in a chapter, including footnote en biblio references
def get_allrefs(root):
    refs = []
    for elem in root.iter('{http://docbook.org/ns/docbook}xref'):
        item = elem.attrib
        refs.append(item)
    for elem in root.iter('{http://docbook.org/ns/docbook}footnoteref'):
        item = elem.attrib
        refs.append(item)
    for elem in root.iter('{http://docbook.org/ns/docbook}biblioref'):
        item = elem.attrib
        refs.append(item)
    sorted(refs, key=lambda i: i['linkend'])
    print(refs)
    print("This chapter has this amount of crossreferences: " + str(len(refs)))

# return a list with all the attributes of a certain tag type in a chapter, also print this list and count the amount
def get_tag(root, tagtype):
    list = []
    for elem in root.iter('{http://docbook.org/ns/docbook}' + tagtype):
        item = elem.attrib
        list.append(item)
    print(list)
    print("This chapter has the following amount of the " + tagtype + " tagtype: " +str(len(list)))
    return list


# returns a dictionary with all tags and their occurrences in a chapter and prints it as well
def count_iterations(root):
    element_list = get_iterations_nondup(root)
    elements = get_iterations(root)
    iterationscounter = {}
    for x in element_list:
        counter = elements.count(x)
        iterationscounter.update({x: counter})
        print(x + ": " + str(counter))
    return iterationscounter


chapter1 = parse_xml("Chapter1.xml")
chapter2 = parse_xml("Chapter2n.xml")
chapter3 = parse_xml("Chapter2.xml")

get_tag(chapter1, "xref")
