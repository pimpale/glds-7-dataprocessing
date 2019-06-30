import sys
import numpy as np
import pandas as pd

hypocotyl = fix_dataframe(pd.read_csv('GLDS-7_hypocotyl.comp.marker_table.txt', sep='\t'))
root = fix_dataframe(pd.read_csv('GLDS-7_root.comp.marker_table.txt', sep='\t'))
shoot = fix_dataframe(pd.read_csv('GLDS-7_shoot.comp.marker_table.txt', sep='\t'))
whole_plant = fix_dataframe(pd.read_csv('GLDS-7_whole_plant.comp.marker_table.txt', sep='\t'))

def fix_dataframe(dataframe):
    has_desc=pd.notna(dataframe['Description'])
    fixed = dataframe[has_desc].copy()
    fixed['Description'] = fixed['Description'].str.lower().str.replace(';',' ').str.split().str[0]
    return fixed

# prints feature p and fold change from row
def get_vals(row):
    print(row[1]['Description'].split()[0], '  FP: ', row[1]['Feature P'], '  FC: ', row[1]['Fold Change'])


def gene_input():
    return get_list(sys.stdin)

def get_list(file):
    list = []
    for word in file.read().split():
        list.append(word.lower())
    return list

def strict(row):
    return row[1]['Feature P'] < 0.05 and row[1]['Fold Change'] > 1.5

def semistrict(row):
    return row[1]['Feature P'] < 0.15 and row[1]['Fold Change'] > 1.1

def all(row):
    return True

def get_genes(genelist, dataframe, filterfunc):
    for row in filter(filterfunc, dataframe.iterrows()):
        if row[1]['Description'] in genelist:
            get_vals(row)

def search(genelist, filterfunc):
    for dataframe in [
        (shoot, '---SHOOT---'),
        (root, '---ROOT---'),
        (hypocotyl, '---HYPOCOTYL---'),
        (whole_plant, '---WHOLE PLANT---')
    ]:
        print(dataframe[1])
        get_genes(genelist, dataframe[0], filterfunc)
