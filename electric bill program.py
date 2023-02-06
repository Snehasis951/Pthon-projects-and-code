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
    elif unitused > 400:
        energy_bill = ((unitused-400)*10) + (100*8) + (100*7) +(100*6) + (50*5) + (50*4)
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
    elif unitused > 300:
        energy_bill = ((unitused-300)*8) + (100*7) +(100*6) + (50*5) + (50*4)
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

    elif unitused > 200:
        energy_bill = ((unitused-200)*7) +(100*6) + (50*5) + (50*4)
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
    elif unitused > 100:
        energy_bill = ((unitused-100)*6) + (50*5) + (50*4)
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
    elif unitused > 50:
        energy_bill = ((unitused-50)*5) + (50*4)
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
    elif unitused > 00:
        energy_bill = ((unitused-50)*5) + (50*4)
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
elif  m1.lower() == "c":
    if unitused > 1000:
        energy_bill = ((unitused-1000)*16) + (300*14) + (200*10) + (200*9) +(300*8)
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
    elif unitused > 700:
        energy_bill = ((unitused-700)*14) + (200*10) + (200*9) +(300*8)
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
    elif unitused > 500:
        energy_bill = ((unitused-500)*10) + (200*9) +(300*8)
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
    elif unitused > 300:
        energy_bill = ((unitused-300)*9) + (300*8)
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
    elif unitused > 000:
        energy_bill = ((unitused-000)*8) 
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
        
    











    
