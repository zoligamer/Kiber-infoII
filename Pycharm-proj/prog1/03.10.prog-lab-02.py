"""class Book:
    def __init__(self,title,author,edition):
        self.title=title
        self.author=author
        self.edition=edition

        def __str__(self):
        return f'{self.title}   {self.author}'
        def __repr__(self):
        return f'{self.title}   {self.author}'

    def __eq__(self, other):
        return self.title==other.title


book_01=Book('the book','Viktor','1999')
book_02=Book('the book','Eszter','2000')
print(book_01==book_02)

"""

class School:
    def __init__(self,name):
        self.name=name
        self.level=self.get_level()
    def get_level(self):
        if 'általános iskola' in self.name.lower():
            return 1
        elif 'gimnázium' in self.name.lower():
            return 2
        elif 'egyetem' in self.name.lower():
            return 3
        else:
            return 0

    def __lt__(self, other):
        return self.level<other.level
    def __gt__(self, other):
        return self.level>other.level
    def __ge__(self, other):
        return self.level>=other.level
    def __le__(self, other):
        return self.level<=other.level
    def __repr__(self):
        return self.name

school_names=['Berzsényi Gimnázium',"Kussuth Lajos Általános Iskola", 'Nigga Általános Iskola', ]
schools = []
for i in school_names:
    schools.append(School(i))
print(schools)
schools.sort()
print(schools)
print(school_names)