class Page:
    '''This class represents a page of a book'''
    def __init__(self, words=set()):
        self.words = words

    def add_word(self, word):
        self.words.add(word)
    
    def remove_word(self, word):
        self.words.remove(word)

    def contains_word(self, word):
        return word in self.words

    def print(self):
        for word in self.words:
            print(word)

class Book:
    '''This class represents a book'''
    def __init__(self, name, pages=list()):
        self.nextpage = 1
        self.name = name
        self.pages = dict()
        for page in pages:
            self.add_page(page)

    def add_page(self, page):
        self.pages[self.nextpage] = page
        self.nextpage += 1

    def remove_page(self, number):
        del self.pages[number]

    def remove_all_pages(self):
        self.pages.clear()

    def print(self):
        print("Book: ", self.name)
        for iter in self.pages.iteritems():
            print(iter.values)

if __name__ == '__main__':
    page1 = Page(("manik", "mary", "sheeri", "tennant"))
    page2 = Page(("manik2", "mary2", "sheeri2", "tennant2"))
    page3 = Page(("manik3", "mary3", "sheeri3", "tennant3"))
    book = Book("Sheeris", [page1, page2, page3])    
    book.print()
    book.remove_all_pages()
    book.print()
