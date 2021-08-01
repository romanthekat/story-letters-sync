import bs4
import requests as req


def iterate_over_letters(letters: bs4.element.ResultSet, level=0):
    for child in letters:
        spans = child.select('span')
        number = spans[0]  # attrs{'class'} == ['tocnumber']
        text = spans[1]  # attrs{'class'} == ['toctext']

        prefix = '\t' * level
        print(f"{prefix}{number.text}: {text.text}")

        if len(spans) > 2:
            iterate_over_letters(child.select('li'), level + 1)


# Requesting for the website
response = req.get('https://animalrestaurant.fandom.com/wiki/Letters#Story_Letters')
if response.status_code != 200:
    print("failed to fetch letters, response not ok: " + str(response))
    raise Exception

page = bs4.BeautifulSoup(response.text, 'lxml')
page.prettify()

story_letters_elements = page.select('.toclevel-2')  # page.select('.toclevel-1.tocsection-2')
iterate_over_letters(story_letters_elements)
