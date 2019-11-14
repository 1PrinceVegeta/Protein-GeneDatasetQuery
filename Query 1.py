import re
from os import listdir
from datetime import datetime


def query_file(path, organism, gene_id):
    interactors_list = []
    with open(path + "//" + organism, 'r') as currentFile:
        for line in currentFile:
            if gene_id in line:
                interactor = line.split("\t")
                if gene_id.isdigit():
                    if re.search(':(.*)', interactor[0]).group(1) == gene_id:
                        # interactors_list.append(interactor[1].partition(":")[2].partition(" ")[0])  # using partition
                        interactors_list.append(re.search(':(.*)', interactor[1]).group(1))  # using regex
                else:
                    if re.search(r'locuslink:([^|]*)', interactor[2]).group(1) == gene_id:
                        # interactors_list.append(interactor[3].partition("locuslink:")[2].partition("|")[0]) # using partition
                        interactors_list.append(re.search(r'locuslink:([^|]*)', interactor[3]).group(1))  # using regex
    return interactors_list


def print_result(interactors_list):
    if len(interactors_list) > 0:
        print("\nGene Name/ID : " + gene)
        interactors_list = list(dict.fromkeys(interactors_list))
        print("Number of interactors : " + str(len(interactors_list)))
        print("Interactors : ", end="")
        for interactor in interactors_list:
            print(interactor, end=" ")
    else:
        print("No interactor found for gene!")
    print("\nTime Taken: " + str(y - x))


if __name__ == '__main__':
    path = input("Enter Path to Biogrid Dataset: ")
    organism = input("Enter name of Organism: ")
    gene = input("Enter Gene Name/ID: ")
    x = datetime.now()
    interactors = query_file(path, organism, gene)
    y = datetime.now()
    print_result(interactors)
