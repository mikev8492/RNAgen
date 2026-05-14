# -*- coding: utf-8 -*-

import argparse, random

from src.sequence_lib import(
    START_CODON,
    STOP_CODONS,
    get_gc_content,
    get_ambiguity_content,
    generate_random_codon,
    generate_random_sequence,
    write_fasta
)

class Simulator:
    def __init__(self, args: argparse.Namespace) -> None:
        self.num_sequences = args.num_sequences
        self.min_orf_length = args.min_length
        self.max_orf_length = args.max_length
        self.flanking_probability = args.flanking_prob
        self.flanking_length = args.flanking_length
        self.completeness_ratio = args.completeness
        self.results = []

    def generate_orf(self, complete: bool = True) -> str:
        """
        Generate single ORF
        Args: 
            Bool: complete - determine whether to generate an ORF with start/stop codons
        Returns:
            Constructed ORF string
        Example:
            > generate_orf()
            > orf = "AUGAAAUUUCCCGGGUAA"

            > generate_orf(complete = False)
            > orf = "AAAAAAUUUUUCCCCCGGGGGG"
        """
        # Random length based on user args
        length = random.randint(self.min_orf_length, self.max_orf_length)
        orf = ""
        # Complete ORF: 
        if complete == True:
            orf = START_CODON

            for _ in range(0, length - 3, 3):
                orf += generate_random_codon()
            orf += random.choice(STOP_CODONS)
        # Partial ORF:
        else:
            orf = generate_random_sequence(length)
        
        return orf

    def generate_sequence(self)-> "tuple[str,str,str]":
        """
        Generates complete sequence with randomized features
        Returns:
            tuple[sequence, ORF type, Flanking status
        """
        is_complete = random.random() <= self.completeness_ratio
        orf = self.generate_orf(is_complete)
        if is_complete:
            orf_type = "Complete ORF"
        else:
            orf_type = "Partial ORF"

        if random.random() <= self.flanking_probability:
            left = generate_random_sequence(self.flanking_length)
            right = generate_random_sequence(self.flanking_length)
            seq = left + orf + right
            flank_status = "Flanked"
        else:
            seq = orf
            flank_status = "Not Flanked"        

        return seq, orf_type, flank_status 

    def generate_sequences(self) -> "list[tuple[str, str, str]]":
        """
        Generate all sequences with metadata using sequence_lib modules
        Returns:
            list of tuples containing (sequence ID, description, sequence)
        Example:
            > generate_sequences()
            > [(seq_0001, description, "AAAGCU"),(seq_0002, description, "AACGCG")]
        """
        # results = []

        for i in range(self.num_sequences):
            seq, orf_type, flank_status = self.generate_sequence()
            # Type specifier used to format: {i:03d} = integer formatted as 4 digits with leading zeros
            seq_id = f"seq{i:04d}"
            gc = get_gc_content(seq)
            amb = get_ambiguity_content(seq)

            description = (
                f"Length = {len(seq)}",
                f"GC = {gc}%", 
                f"Ambiguity = {amb}%",
                f"ORF Type = {orf_type}",
                f"Status = {flank_status}"
            )

            self.results.append((seq_id, description, seq))
        return self.results

    def save_fasta(self, output_file: str) -> None:
        """
        Generate sequences and save to a FASTA file
        Args: 
            str: output filename from user
        """
        sequences = self.generate_sequences()
        write_fasta(sequences, output_file)

    def generate_report(self) -> str:
        """
        Generate a concise summary report from self.results.
        Returns:
            Formatted report string
        """
        total = len(self.results)
        if total == 0:
            return "No sequences generated."

        lengths, gc_vals, amb_vals = [], [], []
        complete, flanked = 0, 0

        for _, description, seq in self.results:
            lengths.append(len(seq))
            for field in description:
                k, v = field.split(" = ")
                if k == "GC":
                    gc_vals.append(float(v.strip("%")))
                elif k == "Ambiguity":
                    amb_vals.append(float(v.strip("%")))
                elif k == "ORF Type" and v == "Complete ORF":
                    complete += 1
                elif k == "Status" and v == "Flanked":
                    flanked += 1

        return (
            f"\n{'─' * 38}\n"
            f"  Sequences  : {total}\n"
            f"  Length     : avg {sum(lengths)/total:.0f} nt  "
                        f"(min {min(lengths)} / max {max(lengths)})\n"
            f"  GC content : avg {sum(gc_vals)/total:.1f}%\n"
            f"  Ambiguity  : avg {sum(amb_vals)/total:.1f}%\n"
            f"  Complete   : {complete}/{total} "
                        f"({complete/total*100:.0f}%)\n"
            f"  Flanked    : {flanked}/{total} "
                        f"({flanked/total*100:.0f}%)\n"
            f"{'─' * 38}\n"
        )