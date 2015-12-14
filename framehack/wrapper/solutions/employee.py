class Employee:
    "Pretend that this is actually a C++ class that's been wrapped by SWIG"
    def GetGivenName(self): return self.given_name
    def SetGivenName(self, value):  self.given_name = value

    def GetFamilyName(self): return self.family_name
    def SetFamilyName(self, value):  self.family_name = value

    def GetDateOfBirth(self): return self.date_of_birth
    def SetDateOfBirth(self, value):  self.date_of_birth = value

    given_name = ''
    family_name = ''
    date_of_birth = ''
