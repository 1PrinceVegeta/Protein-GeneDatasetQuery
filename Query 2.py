#  query 2
from datetime import datetime


def query_file(gene_id1):
    interactors_list = []
    with open("E:\\CSE 3113Y Assignment\\test_idmapping_selected.txt", 'r') as file:
        for line in file:
            if gene_id1 in line:
                gene = line.split("\t")
                if gene[2] == (gene_id1 + "\n"):
                    interactors_list.append(gene[0] + "\t" + gene[1])
    return interactors_list


def print_result(interactors_list):
    if len(interactors_list) > 0:
        print("\nGene ID : " + gene_id)
        print("Interactors :  UniProtKB-AC UniProtKB-ID")
        interactors_list = list(dict.fromkeys(interactors_list))
        for interactor in interactors_list:
            print("               " + interactor)
    else:
        print("No interactor found for gene!")


if __name__ == '__main__':
    gene_id = input("Enter Gene ID: ")
    x = datetime.now()
    interactors = query_file(gene_id)
    y = datetime.now()
    print_result(interactors)
    print("\nTime Taken: " + str(y - x))
