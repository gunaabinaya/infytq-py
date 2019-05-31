def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    x=patient_medical_speciality_list.count('O')
    y=patient_medical_speciality_list.count('P')
    z=patient_medical_speciality_list.count('E')
    if x>y and x>z:
        s=medical_speciality["O"]
    elif y>z and y>x:
        s=medical_speciality["P"]
    else:
        s=medical_speciality["E"]
    return s
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
