import tiffani010


def input_vektor(nama):
    print(f"\nMasukkan vektor {nama}:")
    n = int(input("  Jumlah dimensi vektor: "))
    v = []
    for i in range(n):
        x = float(input(f"  Elemen ke-{i+1}: "))
        v.append(x)
    return v

def tampilkan_menu():
    print("       KALKULATOR VEKTOR - tiffani010")
    print("  1. Penjumlahan Vektor")
    print("  2. Pengurangan Vektor")
    print("  3. Dot Product")
    print("  4. Sudut Antara Dua Vektor")
    print("  0. Keluar")
   

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-4): ")

    if pilihan == "0":
        print("\nProgram selesai. Terima kasih!")
        break

    elif pilihan == "1":
        v1 = input_vektor("v1")
        v2 = input_vektor("v2")
        try:
            hasil = tiffani010.penjumlahan(v1, v2)
            print(f"\nHasil penjumlahan: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    elif pilihan == "2":
        v1 = input_vektor("v1")
        v2 = input_vektor("v2")
        try:
            hasil = tiffani010.pengurangan(v1, v2)
            print(f"\nHasil pengurangan: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    elif pilihan == "3":
        v1 = input_vektor("v1")
        v2 = input_vektor("v2")
        try:
            hasil = tiffani010.dot_product(v1, v2)
            print(f"\nHasil dot product: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")

    
    elif pilihan == "4":
        v1 = input_vektor("v1")
        v2 = input_vektor("v2")
        try:
            hasil = tiffani010.sudut(v1, v2)
            print(f"\nSudut antara dua vektor: {hasil:.4f}°")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("\nPilihan tidak valid. Masukkan angka 0-4.")

    input("\nTekan Enter untuk kembali ke menu...")
