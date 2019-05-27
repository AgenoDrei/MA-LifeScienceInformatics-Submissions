
#!/usr/bin/python

def fasta_reader(inputfile): 
    with open(inputfile,"r") as fasta:
        lines=fasta.readlines()
        fasta_dic={}
        for i in lines:
            j=i.rstrip()[1:]
            if i.startswith(">"):
                header=j
                fasta_dic[header]=""
            else:
                fasta_dic[header]=fasta_dic[header] + str(j)
        return list(fasta_dic.items())
    
def read_fasta_generator(filename):
    name = None
    with open(filename) as file:
        for line in file.readlines():
            if line[0] == ">":
                if name:
                    yield (name, seq)
                name = line[1:].strip()
                seq = ""
            else:
                seq += line[:-1]
        yield (name, seq)
        
def write_fasta(header,sequence,outfile):
    import textwrap
    outfile.write(">" + header+"\n")
    for i in textwrap.wrap(sequence,70):
        outfile.write(i+"\n")
    outfile.write("\n")
    
if __name__ == '__main__':
    print ("Import modules \"fasta_reader\", \"read_fasta\" and \"write_fasta\" from this file")
