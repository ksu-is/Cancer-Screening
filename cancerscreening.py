#cancer questionaire
print("Hello and welcome to my Cancer Screening tool. In this tool, we will calculate your risk for getting the 4 most prevalent cancers in America:\nLung\nBreast\nProstate\nColorectal\n")
name = input("May I get your name please: ")
age = int(input("How old are you (integers only please): "))
male_female = input("What gender were you assigned at birth (male or female): ").lower()
in_fam = input("Do any the 4 above cancers run in your family?\nIf yes, please specify which ones: " ).lower()
smoker = input("Are you a smoker (y or n): ").lower()
radon = input("Have you had constant exposure to radon (y or n) choose no if unsure: ").lower()
braca = input("Do you have the BRACA 1 or 2 gene (please enter 1, 2 or n for no): ")
alcohol = input("Do you drink more than 2 alcoholic drinks a day (y or n): ").lower()
print("Thank you,", name, "here are your results: \n")

#lung cancer screening code
def lung_cancer():
    lung_cancer_percent = 0
    if smoker == "y":
        lung_cancer_percent += 20
    else:
       lung_cancer_percent += 10
    if "lung" in in_fam:
        lung_cancer_percent += 8
    else:
        pass
    print("Your overall chance of getting lung cancer at some point in your life is", lung_cancer_percent, "percent.\n")

#breast cancer screening code
def breast_cancer():
    breast_cancer_percent = 0.00
    if male_female == "female":
        if braca == "1":
          breast_cancer_percent += 72.00  
        elif braca == "2":
            breast_cancer_percent += 69.00
        else:
            breast_cancer_percent += 18.00
    else:
        breast_cancer_percent += 1.00
 #   If breast cancer runs in your family your risk increasesby: 5 - 10%
    if "breast" in in_fam:
        breast_cancer_percent += 10.00
    else:
        pass
 #breast cancer risk increases with age after 30, below is the code for this increase based on age range
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
    if alcohol == "y":
        breast_cancer_percent += 0.50
    else:
        pass
    print("Your overall chance of getting breast cancer at some point in your life is", breast_cancer_percent, "percent.\n")

def prostate_cancer():
    prostate_cancer_percent = 0.0
    if male_female == "male":
        prostate_cancer_percent += 12.5
        if "prostate" in in_fam:
            prostate_cancer_percent += 12.5
        else:
            pass
        print("Your overall chance of getting prostate cancer is", prostate_cancer_percent, "percent.\n")
    else:
        print("You are at no risk getting prostate cancer due to being female\n")

def overall_cancer():
    lung_cancer()
    breast_cancer()
    prostate_cancer()
    print("Some general tips to reduce your chances of getting the cancers mentioned above are: \n")
    print("Quit smoking\nReduce alcohol intake\nEat more fruits and veggies\nAvoid carcinogens\nGet regular screenings from your doctor.\n")
overall_cancer()

