import csv
import yaml
import string
import pdb
import urllib
from bs4 import BeautifulSoup

in_file  = open('cases.csv', "r")
items = []
items_dict = {}
item_descriptions = []


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;"
    }

slug_strip_table = {
    "&": "",
    '"': "",
    "'": "",
    ">": "",
    "<": "",
    "?": ""  
}

category_mapping = [
    {
        "id":"5",
        "category":"Spanish-language Cases",
        "order":"2"
    },
    {
        "id":"15",
        "category":"Public Policy Cases",
        "order":"3"
    },
    {
        "id":"16",
        "category":"Public Health and Medical Cases",
        "order":"4"
    },
    {
        "id":"17",
        "category":"Journalism Cases",
        "order":"1"
    },
    {
        "id":"19",
        "category":"AKU Cases",
        "order":"6"
    },
    {
        "id":"20",
        "category":"Sustainable Development Cases",
        "order":"5"
    },

]

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def remove_images(description):
    soup = BeautifulSoup(description)
    imgs = soup.find_all('img')
    for img in imgs: 
        img.extract()
    return soup

def set_category(cat_id):
    for cat in category_mapping:
        if cat["id"] == cat_id:
            return cat['category']

    return "None"


def convert_to_yaml(line, counter):
    title = html_escape(line[2])
    case_topics = [st.strip(string.whitespace) for st in line[4].split(';') ]
    if len(case_topics) == 1:
        case_topics = [st.strip(string.whitespace) for st in line[4].split(',') ]
    for topic in range(len(case_topics)):
        if case_topics[topic] == "":
            case_topics[topic] = " None"
    related_cases = [st.strip(string.whitespace) for st in line[8].split(',') ]
    description = line[11]
    description = description.replace('_x000d_', '')
    description = description.replace('\n', '')
    description = description.replace('\t', '')
    description_soup = remove_images(description)
    description = str(description_soup)

    description_clean = description_soup.get_text()
    slug_soup = line[1].split(' ')
    temp_slug = "".join(s for s in slug_soup)
    clean_slug = "".join(slug_strip_table.get(st,st) for st in temp_slug)
    category = set_category(line[26])
    item = {
        'id': line[0],
        'slug': clean_slug,
        'title': title,
        'case_number': line[3],
        'case_topics': case_topics,
        'case_author': line[5],
        'news_org': line[6],
        'faculty_notes': line[7],
        'related_cases': related_cases,
        'redtext': line[9],
        'teaser': line[10],
        'description': description,
        'price': line[12],
        'pdf': line[13],
        'abstract': line[14],
        'teaching_note': line[15],
        'epilogue': line[16],
        'banner': line[17],
        'thumb': line[19],
        'link_color': line[20],
        'title_color': line[21],
        'authentication': line[22],
        'faculty_only': line[23],
        'layout': line[24],
        'linked_classes': line[25],
        'category_id': line[26],
        'category': category,
        'status_id': line[27],
        'created_on': line[28],
        'school': line[29],
        'description_clean': description_clean
    }

    items.append(item)
    items_dict[item['id']] = item
    item_descriptions.append(description)

def replace_related_caseids(items_dict, items):
    for i in range(len(items)):
        related_case_list = []
        for rel_item in range(len(items[i]['related_cases'])):
            ri = items[i]['related_cases'][rel_item]
            if not ri == "":
                cn = items_dict[items[i]['related_cases'][rel_item]]['case_number']
                related_case_list.append(cn)
        items[i]['related_cases'] = related_case_list

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers

    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)

    replace_related_caseids(items_dict, items)

    

    for i in range(len(items)):
        out_filename = "case_" + items[i]['id'] + ".md"
        out_file = open(out_filename, "w")
        out_file.write(
            yaml.dump(items[i],
                      default_flow_style=False,
                      allow_unicode=True,
                      default_style='"',
                      line_break=False,
                      explicit_start=True,
                      explicit_end=False) )
        ''' the Yaml lib explicit_end is ... not --- '''
        out_file.write("---")
        out_file.write("\n")

        out_file.write(item_descriptions[i])
        out_file.write("\n")

finally:
    in_file.close()
    out_file.close()