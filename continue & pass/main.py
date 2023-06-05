# # # continue, pass, break

# # # pass

#  angka = 0

#  while angka < 5:
#      angka += 1
#      pass

#      print(angka)

# print("=" * 20)
# # continue

 angka = 0

 while angka < 5:
     angka += 1
     print(f"angka sekarang --> {angka}")

     if angka == 3:
         print("Nice")
         continue

     print("Whattsapp")

 print("Finish")
 print("=" * 20)

# # break

 data_int = int(input("Hitung Sampai = "))
 angka = 0

 while True:
     angka += 1
     print(f"angka sekarang --> {angka}")

     if angka == data_int:
         print("Nice")
         break

     print("Whasupp")

 print("cukup finish")
