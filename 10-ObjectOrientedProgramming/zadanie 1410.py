class Book:
    def __init__(self):
        self.is_on=False
        self.pagenumber=0
        self.currentpage=0

    def open(self):
        self.is_on=True
    def close(self):
        self.is_on=False

    def create_book(self,autor,tytul,pages):
        self.autor=autor
        self.pagenumber=pages
        self.tytul=tytul

    def status(self):
        if self.is_on==True:
            print(f'książka otwarta: {self.autor}, {self.tytul}, {self.pagenumber}, current page {self.currentpage}')
        else:
            print(f'książka zamknieta')

    def forward(self,ile):
        if self.is_on==True:
            self.currentpage+=ile
            if self.currentpage>self.pagenumber:
                self.currentpage=self.pagenumber
        else:
            pass

    def backward(self,ile):
        if self.is_on==True:
            self.currentpage-=ile
            if self.currentpage<0:
                self.currentpage=0
        else:
            pass


b=Book()
b.create_book('autor','tytul',90)
b.open()
b.status()
b.forward(31)
b.status()
b.forward(80)
b.status()
b.backward(80)
b.status()