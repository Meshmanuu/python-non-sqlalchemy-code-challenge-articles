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

# Definition of the class Author
class Author:
    def __init__(self, name):
        self._name = None  # Initialize name attribute
        self.name = name  # Use the setter to validate the name

    @property
    def name(self):
        return self._name  # Getter method for the name attribute

    @name.setter
    def name(self, new_name):
        if self._name is not None:  # Check if name has already been set
            AttributeError("Name cannot be changed")  # Raise error if trying to change name
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name  # Set name if it's a non-empty string
        else:
            ValueError("Name must be a non-empty string")  # Raise error for invalid name

    def articles(self):
        return [article for article in Article.all if self == article.author]  # Get the articles written by this author

    def magazines(self):
        return list({article.magazine for article in self.articles()})  # Get the list of magazines the author has written for

    def add_article(self, magazine, title):
        return Article(self, magazine, title)  # Add a new article written by this author to the list of articles

    def topic_areas(self):
        areas = list({magazine.category for magazine in self.magazines()})  # Get the topic areas based on the magazines the author has written for
        return areas if areas else None  # Return None if no topic areas
# Definition of the class Magazine
class Magazine:
    def __init__(self, name, category):
        self._name = None  # Initialize name attribute
        self._category = None  # Initialize category attribute
        self.name = name  # Use the setter to validate the name
        self.category = category  # Use the setter to validate the category

    @property
    def name(self):
        return self._name  # Getter method for the name attribute

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name  # Set name if it's a string between 2 and 16 characters
        else:
            ValueError("Name must be a string between 2 and 16 characters")  # Raise an error for invalid input

    @property
    def category(self):
        return self._category  # Getter method for the category attribute

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category  # Set category if it's a non-empty string
        else:
            ValueError("Category must be a non-empty string")  # Raise an error for invalid input

    def articles(self):
        return [article for article in Article.all if self == article.magazine]  # Get the articles associated with this magazine

    def contributors(self):
        return list({article.author for article in self.articles()})  # Get the list of contributors for this magazine

    def article_titles(self):
        titles = [article.title for article in self.articles()]  # Get the titles of the articles associated with this magazine
        return titles if titles else None  # Return None if no articles

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count >= 2] or None  # Get the authors who have contributed multiple articles to this magazine
