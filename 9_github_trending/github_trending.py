from datetime import date, timedelta
import requests


def get_trending_repositories(page_limit, days_ago):
    url = "https://api.github.com/search/repositories"
    from_date = date.today() - timedelta(days=days_ago)
    params = {'q': 'created:>{}'.format(from_date),
              'sort': 'starts',
              'per_page': page_limit}
    response = requests.get(url, params)
    return response.json()["items"]


def print_repositories(repositories):
    print( "|", 'name'.center(30),
           "|", 'url'.center(55),
           "|", 'stars'.center(10),
           "|", 'open issues'.center(15),
           "|")
    for repo in repositories:
        print( "|", repo['name'].center(30),
               "|", repo['html_url'].center(55),
               "|", str(repo['stargazers_count']).center(10),
               "|", str(repo['open_issues']).center(15),
               "|")


if __name__ == '__main__':
    repositories_quantity = 20
    days = 7
    print('Самые интересные проекты:')
    repositories = get_trending_repositories(repositories_quantity, days)
    print_repositories(repositories)
