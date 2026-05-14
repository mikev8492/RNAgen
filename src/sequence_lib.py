# -*- coding: utf-8 -*-

import sys, random

# Constants (Global Definitions):
VALID_NUCLEOTIDES = ["A", "U", "C", "G"]
AMBIGUOUS_NUCLEOTIDES = ["N", "R", "Y", "S", "W", "K", "M", "B", "D", "H", "V"]
START_CODON = "AUG"
STOP_CODONS = ["UAA", "UAG", "UGA"]


def get_gc_content(sequence: str) -> float:
    """
    Calculate percent of G anc C nucleotides (Ignoring Ambiguous codes)
    Args: 
        sequence: RNA sequence string (uppercase, U for uracil)
    Returns:
        float: GC content as a percentage (0-100%)
    Raises:
        ValueError: If sequence is empty
    Example:
        > get_gc_content("AUGC")
        > 50.0
    """
    if not sequence:
        raise ValueError("Sequence argument empty")

    count = 0

    for i in sequence:
        if i == "G" or i == "C":
            count += 1
    gc_perc = (count / len(sequence)) * 100
    return round(gc_perc, 1)


def get_ambiguity_content(sequence: str) -> float:
    """
    Calculate percent of IUPAC ambiguous codes
    Args: 
        sequence: RNA sequence string
    Returns:
        float: calculated ambiguity percentage
    Raises:
        ValueError: if sequence empty or contains invalid nucleotides
    Example:
        > get_ambiguity_content("AUGCNRYS")
        > 50.0
    """
    if not sequence:
        raise ValueError("Sequence argument empty")
    
    count = 0
    for i in sequence:
        if i in AMBIGUOUS_NUCLEOTIDES:
            count += 1
    amb_percent = (count / len(sequence)) * 100
    return round(amb_percent, 1)


def generate_random_codon() -> str:
    """
    Generate a random 3-nucleotide codon
    Returns:
        str: 3 nucleotide codon
    """
    codon = ""
    nucleotides = VALID_NUCLEOTIDES + AMBIGUOUS_NUCLEOTIDES
    for _ in range(3):
        codon += random.choice(nucleotides)
    return codon

def is_start_codon(codon: str) -> bool:
    """
    Check if codon is AUG
    Args: 
        str: 3 nucleotide codon
    Returns:
        True: codon == AUG
    """
    return codon == START_CODON

def is_stop_codon(codon: str) -> bool:
    """
    Check if codon is UAA, UAG, or UGA
    Args: 
        str: 3 nucleotide codon
    Returns:
        True: codon == stop codon
    """
    return codon in STOP_CODONS


def generate_random_sequence(length: int) -> str:
    """
    Generate a random RNA sequence
    Args: 
        int: length value
    Returns:
        str: RNA sequence
    Raises:
        ValueError: length is zero or negative 
    Example:
        > generate_random_sequence(5)
        > seq = "AUGCG"
    """
    rna = ""
    if length <= 0:
        raise ValueError("Length argument invalid")
    
    for _ in range(length):
        rna += random.choice(VALID_NUCLEOTIDES)
    return rna
    

def write_fasta(sequences: list[tuple[str, str, str]], output_file: str) -> None:
    """
    Write sequences to FASTA file
    Args: 
        list: ordered sequence strings
        str: output file name
    Raises:
        FileNotFoundError
        PermissionError
        OSError
    """
    output_file = "output/" + output_file
    try:
        with open(output_file, "w") as file:
            for seqid, desc, seq in sequences:
                file.write(f">{seqid} [{', '.join(item for item in desc)}]\n")
                file.write(f"{seq}\n")
    except (FileNotFoundError, PermissionError, OSError) as err:
        sys.stderr.write(f"File operation error: {err}")
    