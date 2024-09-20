from pygooglenews import GoogleNews

gn = GoogleNews(country='Korea')

def get_titles(query, when=None):
    stories = []
    # Check if a time frame is specified and adjust the search accordingly
    if when:
        search_result = gn.search(query, when=when)
    else:
        search_result = gn.search(query)
    newsitem = search_result['entries']
    for item in newsitem:
        story = {
            'title': item.title,
            'link': item.link
        }
        stories.append(story)
    return stories

# For searching articles mentioning MSFT but not AAPL over the past 6 months
stories = get_titles('윤석열', when='6m')

print(stories)
print(len(stories))  # This prints the number of stories found
