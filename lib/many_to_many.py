
class Author:
    def __init__(self,name):
        self.name = name

    def contracts(self):
        return [ contract for contract in Contract.all if contract.author == self ]

    def books(self):
        return [ contract.book for contract in Contract.all if contract.author == self ]
     
    
    def sign_contract(self,book, date, royalties):
        Book(book)
        Contract(self,book,date,royalties)   
class Book:
    all = []
    def __init__(self,title):
        self.title = title
        Book.add_book_to_all(self)
        
    @classmethod
    def add_book_to_all(cls,book):
        cls.all.append(book)

    def contracts(self):
        return [ contract for contract in Contract.all if contract.book == self ]
    
    def authors(self):
        return [ contract.author for contract in Contract.all if contract.book == self ]
class Contract:
    
    all = []
    def __init__(self,author,book,date,royalties):        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.add_contract_to_all(self)
        
    
    
    @property
    def author(self):
        return self._author 
            
    @author.setter
    def author(self,name):
        if isinstance(name , Author):
            self._author = name
        else:
            raise ValueError ("Author must be in the system")
        
    @property
    def book(self):
        return self._book 
            
    @book.setter
    def book(self,title):
        if isinstance(title , Book):
            self._book = title
        else:
            raise ValueError ("Book must be in the system")
    
    @property
    def date(self):
        return self._date
            
    @date.setter
    def date(self,date):
        if isinstance(date ,str):
            self._date = date
        else:
            raise TypeError ("Date must be a string")
    
    @property
    def royalties(self):
        return self._royalties
            
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties , int):
            self._royalties = royalties
        else:
            raise TypeError ("Royalties must be an integer")
    
    @classmethod
    def add_contract_to_all(cls,contract):
        cls.all.append(contract)
        

        