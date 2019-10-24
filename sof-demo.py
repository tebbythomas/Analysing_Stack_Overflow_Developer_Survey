import csv
import sys
from collections import defaultdict, Counter

with open('developer_Survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    
    dev_type_info = {}
    
    for line in csv_reader:
        dev_types = line['DevType'].split(';')
        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total' : 0,
                'language_counter' : Counter()
            })
            languages = line['LanguageWorkedWith'].split(';')
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1
print("Analysis done, results will be written into the output file now")
with open('output.txt', 'w') as the_file:
    for dev_type, info in dev_type_info.items():
        the_file.write(f'Developer Category: {dev_type}\n')
        the_file.write("Top 5 languages used:\n")
        for language, value in info['language_counter'].most_common(5):
            language_pct = (value / info['total']) * 100
            language_pct = round(language_pct, 2)

            the_file.write(f'\t{language}: {language_pct}%\n')
print("Results written into the output file")