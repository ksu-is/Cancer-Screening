#cancer questionaire
print("Hello and welcome to my Cancer Screening tool.")
name = input("May I get your name please: ")
age = input("How old are you: ")
male_female = input("What gender were you assigned at birth (male or female): ")
smoker = input("Are you a smoker (y or n): ")
in_fam_lung = input("Does lung cancer run in your family (y or n): ")
radon = input("Have you had constant exposure to radon (y or n) choose no if unsure: ")
in_fam_breast = input("Does breast cancer run in your family (y or n): ")
braca = input("Do you have the BRACA 1 or 2 gene (please enter 1, 2 or n for no): ")
alcohol = input("Do you drink more than 2 alcoholic drinks a day (y or n): ")

print("Thank you,", name, "here are your results: \n")


#lung cancer screening code
def lung_cancer():
    lung_cancer_percent = 0
    #smoker = input("Are you a smoker (y or n): ")
    #in_fam_lung = input("Does lung cancer run in your family (y or n): ")
    #radon = input("Have you had constant exposure to radon (y or n) choose no if unsure: ")
    if smoker == "y":
        lung_cancer_percent += 20
    else:
       lung_cancer_percent += 10
    if in_fam_lung == "y":
        lung_cancer_percent += 8
    else:
        pass
    print("Your overall chance of getting lung cancer is", lung_cancer_percent, "percent.\n")
    print("Lung cancer is more prevalent in people 65 or older.\nSome tips to reduce your risk are:\n- quit smoking and reduce your exposure to second hand smoke\n- eat a diet of healthy fruits and veggies\n- avoid carcinogens.\n")
#lung_cancer()

#breast cancer screening code
def breast_cancer():
    breast_cancer_percent = 0.00
   # in_fam_breast = input("Does breast cancer run in your family (y or n): ")
 #Braca Genes
    #braca = input("Do you have the BRACA 1 or 2 gene (please enter 1, 2 or n for no): ")
    if male_female == "female":
        if braca == "1":
          breast_cancer_percent += 72.00  
        elif braca == "2":
            breast_cancer_percent += 69.00
        else:
            breast_cancer_percent += 18.00
    else:
        breast_cancer_percent += 1.00
 #   If breast cancer runs in family: 5 - 10%
    if in_fam_breast == "y":
        breast_cancer_percent += 10.00
    else:
        pass
 #breast cancer risk increases with age after 30
    if age in range(30,39):
        breast_cancer_percent += 0.44
    elif age in range(40,49):
        breast_cancer_percent += 1.45
    elif age in range(50,59):
        breast_cancer_percent += 2.31
    elif age in range(60,69):
        breast_cancer_percent += 3.49
    elif age in range(70,79):
        breast_cancer_percent += 3.84
    else:
        pass
 #   If have 2 or more alcoholic drinks a day: add .5%
    #alcohol = input("Do you drink more than 2 alcoholic drinks a day (y or n): ")
    if alcohol == "y":
        breast_cancer_percent += 0.50
    else:
        pass
    print("Your overall chance of getting breast cancer is", breast_cancer_percent, "percent.\n")
#breast_cancer()

def overall_cancer():
    lung_cancer()
    breast_cancer()

overall_cancer()
