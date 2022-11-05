# class var vs instance var....

# class example: will exsist in all instances

class Example:

    NAME = "same for everything"


print(Example.NAME)

e = Example()
print(e.NAME)


# instance variables  name is a local var...self.name is instance


# also on top of instance var is super class

class Form:
    IS_FORM = True

    def __init__(self, ssn):
        self.ssn = ssn

    def ask_for_ssn_again(self):
        ssn = input("What is your ssn? ")  # local var
        print(f"ty for giving your last four {ssn}")


# notice how we are passing Form into DicchargeForm and it inherits IS_FORM = True
class DischargeForm(Form):

    FORM_VERSION = "DD-214"

    def __init__(self, ssn, name, dob):
        super().__init__(ssn)
        self.name = name
        self.dob = dob
        print(self.IS_FORM)


print(DischargeForm.FORM_VERSION)
d = DischargeForm(1234, "vega", "1-1-2011")
# print(d.name, d.dob)
# print(d.IS_FORM)
print(d.ssn)
d.ask_for_ssn_again()
