data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

# 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for lokasi, data in data_panen.items():
    print(f"ID Lokasi: {lokasi}")
    print(f"Nama Lokasi: {data['nama_lokasi']}")
    print(f"Hasil panen : {data['hasil_panen']}")

#2. Tampilkan jumlah hasil panen jagung dari lokasi2.
panen_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi 2: {panen_jagung_lokasi2}") 

#3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama lokasi dari lokasi 3: {nama_lokasi3}")

#4. Masukkan jumlah hasil panen padi dan kedelai dan setiap lokasi ke dalam variabel yang berbeda:
#5. Buat variabel terpisah untuk menampung hasil panen padi dan kedelai dari setiap lokasi
jumlah_hasil_padi = {}
jumlah_hasil_kedelai = {}

for lokasi, data in data_panen.items():
    jumlah_hasil_padi[lokasi] = data['hasil_panen']['padi']
    jumlah_hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']

print("\nJumlah hasil panen padi setiap lokasi: ", jumlah_hasil_padi)
print("\nJumlah hasil panen kedelai setiap lokasi: ", jumlah_hasil_kedelai)

#6. Buat Percabangan 
#Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus.
#Jika tidak, maka lokasi tersebut dalam kondisi baik.
print("\nKondisi lokasi tiap kebun:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
        
#7. Push hasil pengerjaan kedalam GIT
