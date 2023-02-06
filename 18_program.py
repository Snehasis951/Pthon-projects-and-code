name = input("enter customer name: ")
m1 =input("enter consumer type d for domestic and c for commercial: ")
prevmreading = int(input("enter your previous meter reading: "))
curmreading = int(input("enter your current meter reading: "))
unitused = curmreading - prevmreading
total_bill = 0
energy_bill =0
gst = 0
service_tax = 30
if m1.lower() == "d":
    if unitused > 500:
        energy_bill = ((unitused-500)*12) + (100*10) + (100*8) + (100*7) +(100*6) + (50*5) + (50*4)
        gst = energy_bill*.05
        total_bill = energy_bill +gst + service_tax
        print("Name : ", name)
        print("Ctype : ", m1)
        print("previous meter reading: ", prevmreading)
        print("current meter reading: ", curmreading)
        print("energy bill : ", energy_bill)
        print("GST : ", gst)
        print("Service tax: ", service_tax)
        print("Total bill : ", total_bill)
    