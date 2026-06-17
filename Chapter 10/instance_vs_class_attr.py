# Instance attribute takes preference over the class attributes during assignment and retreival

class details:
    language = "python"     # this is a class attribute

naveed = details()
naveed.language = "react"   # this is a instance attribute
print(naveed.language)