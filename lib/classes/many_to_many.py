# Definition of the class Article
class Article:
    all = []  # Class-level list to store all instances of Article

    def __init__(self, author, magazine, title):
        self.author = author  # Set author using the setter method
        self.magazine = magazine  # Set magazine using the setter method
        self._title = None  # Initialize title attribute (private)
        self.title = title  # Use the setter to validate and set the title
        Article.all.append(self)  # Add current instance to class-level list 'all'

    @property
    def title(self):
        return self._title  # Getter for title attribute

    @title.setter
    def title(self, new_title):
        if self._title is not None:
            AttributeError('Title cannot be changed')  # Raise error if title is already set
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title  # Set title if conditions are met
        else:
            ValueError('Title must be a string between 5 and 50 characters')  # Raise error for invalid title

    @property
    def author(self):
        return self._author  # Getter for author attribute

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author  # Set author if it's an instance of Author
        else:
            raise TypeError("Author must be an instance of Author")  # Raise error if author is not of type Author

    @property
    def magazine(self):
        return self._magazine  # Getter for magazine attribute

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine  # Set magazine if it's an instance of Magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")  # Raise error if magazine is not of type Magazine

