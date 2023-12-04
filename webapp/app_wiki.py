import wikipedia
from yake import KeywordExtractor


#build a function to return the summary of a wikipedia page
def get_wiki_summary(page):
    """
    returns the summary of a wikipedia page
    """
    return wikipedia.summary(page)

#build a function to search wikipedia pages for a mach
def search_wiki_pages(page):
    '''
    Searches wikipedia pages for a match
    '''
    return wikipedia.search(page)

# build a function to return the wikipedia page

def get_wiki_page(page):
    """
    Return the wikipedia page
    """
    return wikipedia.page(page)


# return the top 10 keywords from the content of a page

def get_wiki_keyword(page):
    """
    gets the top 10 keywords from a content page
    """
    content = get_wiki_page(page).content
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)  # returns a list of tuples containing keyword and scores    (use ipython to checkout)  
    return {keyword: score for keyword, score in keywords[:10]}    # a dictionary comprehension
