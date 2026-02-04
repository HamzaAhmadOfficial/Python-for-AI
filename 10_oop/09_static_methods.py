class ChaiUtils:
    @staticmethod   # Static method are those method which does'nt require any object creation, They are not dependent on object.
    
    def clean_ingredients(text):
        return[item.strip() for item in text.split(",")]
    

raw = "water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)