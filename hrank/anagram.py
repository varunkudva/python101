
def main():
    # A G T C genes
    n = int(raw_input().strip())
    gene_str = raw_input().strip()
    gmap = {}
    num_chars = 0

    for c in gene_str:
        if c in gmap:
            gmap[c] += 1
        else:
            gmap[c] = 1

    for gene, count in gmap.iteritems():
        if count >= n/4:
            num_chars += count - n/4
    print gmap
    print num_chars

if __name__ == '__main__':
    main()




