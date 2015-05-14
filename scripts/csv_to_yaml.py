import csv
import yaml
import pdb
in_file  = open('cases.csv', "r")
items = []
item_descriptions = []

'''
class HugoYaml(yaml.YAMLObject):
    def __init__(id, slug, title, case_number, case_topics, case_author, news_org, faculty_notes, related_cases, redtext):
        self.id = id
        self.slug = slug
        self.title = title
        self.case_number = case_number
        self.case_topics = case_topics
        self.case_author = case_author
        self.news_org = news_org
        self.faculty_notes = faculty_notes
        self.related_cases = related_cases
        self.redtext = redtext

    def __repr__(self):
        return "%s(id=%r, slug=%r, title=%r) % "(
            self.__class__.__id__, self.id, self.slug, self.title)
'''

def convert_to_yaml(line, counter):
    title = line[2]
    case_topics = line[4].split(';')
    related_cases = line[8].split(',')
    description = line[11]
    description = description.replace('_x000d_', '')
    description = description.replace('\n', '')
    description = description.replace('\t', '')
    #pdb.set_trace()
    item = {
        'id': line[0],
        'slug': line[1],
        'title': title,
        'case_number': line[3],
        'case_topics': [case_topics],
        'case_author': line[5],
        'news_org': line[6],
        'faculty_notes': line[7],
        'related_cases': [related_cases],
        'redtext': line[9],
        'teaser': line[10],
        'description': description,
        'price': line[12],
        'abstract': line[13],
        'teaching_note': line[14],
        'epologue': line[15],
        'banner': line[16],
        'abstract_img': line[16],
        'thumb': line[17],
        'link_color': line[18],
        'authentication': line[19],
        'faculty_only': line[20],
        'layout': line[21],
        'linked_classes': line[22],
        'category_id': line[23],
        'status_id': line[24],
        'created_on': line[25],
        'school': line[26],
    }
    items.append(item)
    item_descriptions.append(description)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
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