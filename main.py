""""
hallo ini adalah project pertama dengan python
"""
#sequensial
print('ibu memberi perintah "beli 1 botol susu dan 6 butir telur"')
print('anak menjawab " Oke "')
print('anak pergi ke toko')

# PERCABANGAN: Eksekusi terpilih
apakah_susu_ada = True
if apakah_susu_ada:
    print('beli susu, "uang cukup"')
    apakah_telur_ada = False
    if apakah_telur_ada:
        print('Anak membeli susu 1 botol dan telur 5 butir')
    else:
        print('Anak membeli susu 1 botol')
else:
    print('tidak jadi beli susu,"karena susu habis"')



print('anak pulang ke rumah')
print('menyerahkan belanjaan ke ibu')