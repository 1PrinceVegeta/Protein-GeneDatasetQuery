import re
from os import listdir
from datetime import datetime


def query_file(path, filename, gene_id):
    interactors_list = {}
    interactors_id_array_duplicates = []
    interactors_alias_array_duplicates = []
    interactors_id_array = []
    interactors_alias_array = []
    with open(path + "\\" + filename, 'r') as currentFile:
        for line in currentFile:
            interactor = line.split("\t")
            if gene_id in line:
                clean_id = interactor[1].replace("entrez gene/locuslink:", "");
                clean_alias = interactor[5].replace("entrez gene/locuslink:", "").replace("(gene name synonym)", "")
                interactors_id_array_duplicates.append(clean_id)
                interactors_alias_array_duplicates.append(clean_alias)
                for i in interactors_id_array_duplicates: 
                    if i not in interactors_id_array: 
                        interactors_id_array.append(i) 

                for i in interactors_alias_array_duplicates: 
                    if i not in interactors_alias_array: 
                        interactors_alias_array.append(i)       
                interactors_list.update({ 'id' : interactors_id_array, 'alias' : interactors_alias_array})
    return interactors_list


def print_result(interactors_list):
    if len(interactors_list) > 0:
        print("\nGene Name/ID : " + gene)
        print("Number of interactors : " + str(len(interactors_list['id'])))
        print("Interactors (ID): ", end="")
        print(interactors_list['id'])
        print("Interactors (Aliases): ", end="")
        print(interactors_list['alias'])
    else:
        print("No interactor found for gene!")
    print("\nTime Taken: " + str(y - x))


if __name__ == '__main__':
    path = input("Enter Dataset Path:  ")
    filename = input("Enter Organism file to search: ")
    gene = input("Enter Gene Name/ID: ");
    x = datetime.now()
    interactors = query_file(path, filename, gene)
    y = datetime.now()
    print_result(interactors)
