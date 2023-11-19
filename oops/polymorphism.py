#Polymorphism
class India:
    def capital(self):
        return "New Delhi"

    def language(self):
        return "Hindi"

class USA:
    def capital(self):
        return "Washington, D.C."

    def language(self):
        return "English"

def country_info(country):
    print(f"Capital: {country.capital()}")
    print(f"Language: {country.language()}")

# Create instances
ind = India()
usa = USA()

# Polymorphism in action
country_info(ind)
country_info(usa)
