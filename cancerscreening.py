print("Hello and welcome to my Cancer Screening tool.")
name = input("May I get your name please: ")
print("Thank you,", name)

#lung cancer screening code
lung_cancer_percent = 0
def lung_cancer():
    smoker = input("Are you a smoker (y or n): ")
    in_fam_lung = input("Does lung cancer run in your family (y or n): ")
    radon = input("Have you had constant exposure to radon (y or n) choose no if unsure: ")
    if smoker == "y":
        lung_cancer_percent += 20
    else:
       lung_cancer_percent += 10
    if in_fam_lung == "y":
        lung_cancer_percent += 8
    else:
        pass

