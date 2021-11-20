print("Hello and welcome to my Cancer Screening tool.")
name = input("May I get your name please: ")
print("Thank you,", name)


#lung cancer screening code
def lung_cancer():
    lung_cancer_percent = 0
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
    print("Your overall chance of getting lung cancer is", lung_cancer_percent, "percent.")
    print("Lung cancer is more prevalent in people 65 or older.\nSome tips to reduce your risk are:\n- quit smoking and reduce your exposure to second hand smoke\n- eat a diet of healthy fruits and veggies\n- avoid carcinogens.")
lung_cancer()

