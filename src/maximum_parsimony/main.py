from Bio import SeqIO
from Bio.Align import MultipleSeqAlignment
from Bio.Alphabet import IUPAC, Gapped
from tools.parsimony_exact import ParsimonyExact
from tools.parsimony_heuristics import ParsimonyHeuristics
import time

def main():
    file_name = "data/coding.fa"
    # file_name = "data/cons_noncode.fa"
    alignment = MultipleSeqAlignment([], Gapped(IUPAC.unambiguous_dna, "-"))
    for seq_record in SeqIO.parse(file_name, "fasta"):
        alignment.extend([seq_record])

    """
    par = ParsimonyExact(alignment[:4], bnb=True)
    start = time.time()
    par.run()
    end = time.time()
    print("Maximum parsimony (exact) run in {} seconds.".format(end - start))
    par.draw_tree()
    """

    par = ParsimonyHeuristics(alignment[:4], seed=0)
    start = time.time()
    par.run(print_best=True)
    end = time.time()
    print("Maximum parsimony (with heuristics) run in {} seconds.".format(end - start))
    par.draw_tree()


if __name__ == '__main__':
    main()