import re
from datetime import datetime

uniprot_id = []
gene_id = []
gene1 = ""
gene2 = ""
result1 = ""


def query_file(uniprot_ac1):
    with open("E:\\CSE 3113Y Assignment\\test_idmapping_selected.txt", 'r') as file1, open(
            "E:\\CSE 3113Y Assignment\\test_uniprot_sprot.txt", 'r') as file2:
        for line1 in file1:
            if uniprot_ac1 in line1:
                gene = line1.split("\t")
                if gene[0] == uniprot_ac1:
                    uniprot_id.append(gene[1])
                    gene_id.append(gene[2])
        for line1 in file2:
            global gene1
            gene1 += line1
            if "//" in line1:
                if "AC   " + uniprot_ac1 + ";" in gene1:
                    global gene2
                    gene2 += gene1 + "\n"
                gene1 = ""


def print_result(uniprot_id1, gene_id1):
    if len(uniprot_id1) > 0:
        print("\nUniProtKB-AC : " + uniprot_ac)
        print("UniProtKB-ID : ", end="")
        uniprot_id1 = list(dict.fromkeys(uniprot_id1))
        for item in uniprot_id1:
            if item.strip():
                print(item, end=" ")
        print("\nGeneID : ", end="")
        gene_id1 = list(dict.fromkeys(gene_id1))
        for item in gene_id1:
            if item.strip():
                print(item, end=" ")
        gene_details1 = gene2.split("-!-")
        for line in gene_details1:
            if "FUNCTION" in line:
                function = line.split("CC")
                for line1 in function:
                    global result1
                    result1 += line1.strip("\n\t").replace("       ", " ")
        print("\nFunction : " + result1[11:])
        print("\nSequence : ", end="")
        gene_details1 = gene2.split("\n")
        sequence = ""
        for line in gene_details1:
            if re.match(r'\s', line):
                sequence += str(line)
        result2 = sequence.split("    ")
        for line in result2:
            if line.strip():
                print(line, end="")
    else:
        print("No interactor found for gene!")


if __name__ == '__main__':
    uniprot_ac = input("Enter UniProtAC: ")
    x = datetime.now()
    query_file(uniprot_ac)
    y = datetime.now()
    print_result(uniprot_id, gene_id)
    print("\nTime Taken: " + str(y - x))
