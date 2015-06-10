from YBio import *

def Main():
    dna = YDNA([])
    dna.Load('C:\\data\\input.txt')
    rna = YRNA(dna)
    rna.Save('C:\\data\\output.txt')
Main()