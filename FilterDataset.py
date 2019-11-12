'''
Filter idmapping_selected.tab into test_idmapping_selected.txt
Remove all except for UniprotAC, UniprotID and GeneID
'''


def filter_idmapping_selected():
    with open("E:\\CSE 3113Y Assignment\\idmapping_selected.tab", 'r') as file1:
        with open("E:\\CSE 3113Y Assignment\\test_idmapping_selected.txt", 'a') as file2:
            for line in file1:
                gene = line.split("\t")
                newLine = gene[0] + "\t" + gene[1] + "\t" + gene[2] + "\n"
                file2.write(newLine)


'''
Filter uniprot_sprot.dat into test_uniprot_sprot.txt
Remove all except for lines starting with ID, AC, CC, SQ and whitespaces, and also '//' to separate results
'''


def filter_uniprot_sprot():
    with open("E:\\CSE 3113Y Assignment\\test_uniprot_sprot.txt", 'a') as file1, open(
            "E:\\CSE 3113Y Assignment\\uniprot_sprot.dat", 'r') as file2:
        for line in file2:
            if line.startswith("ID"):
                gene += line
            if line.startswith("AC"):
                gene += line
            if line.startswith("CC"):
                gene += line
            if line.startswith("SQ") or line.startswith(" "):
                gene += line
            if "//" in line:
                file1.write(gene)
                file1.write("//\n")
                gene = ""


if __name__ == '__main__':
    filter_idmapping_selected()
    filter_uniprot_sprot()
