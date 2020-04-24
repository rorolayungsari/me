results = ["kosong" for i in range(Nbaris)]
    for n in set(x[-1] for x in pembelian): # just get all last elements as set
        sameLastElement = [x for x in pembelian if x[-1] == n] # get all sublists that match
        same = ["kosong" for i in range(Nbaris)] # accumulate sub lists into one list
        for a in sameLastElement:
            same +=  a
        tambah_isi_list(results,same) # put into result array
