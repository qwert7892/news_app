import json
import datetime
from . import settings


def load_news(path=settings.BASE_DIR / 'app' / 'data' / 'news.json', page=1):
    with open(path, 'r', encoding='utf-8') as f:
        news = json.load(f)
        f.close()
    news = sorted(news, key=lambda x: x['date'], reverse=True)
    return news[(page - 1) * 5:page * 5]


def load_all_news(path=settings.BASE_DIR / 'app' / 'data' / 'news.json', page=1):
    with open(path, 'r', encoding='utf-8') as f:
        news = json.load(f)
        f.close()
    news = sorted(news, key=lambda x: x['date'], reverse=True)
    return news


def add_news(title, summary, content, path=settings.BASE_DIR / 'app' / 'data' / 'news.json'):
    news = load_news(path)
    new_post = {
        'id': len(news) + 1,
        'title': title,
        'summary': summary,
        'content': content,
        'date': str(datetime.datetime.now().date())
    }
    news.append(new_post)
    with open(path, 'w+', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=2)
        f.close()
    return


def get_news_by_id(news_id: int, path=settings.BASE_DIR / 'app' / 'data' / 'news.json'):
    news_list = load_all_news()
    target_news = [news for news in news_list if news['id'] == news_id]
    return target_news[0]


def format_date(date: str):
    date_list = date.split('-')[::-1]
    return '.'.join(date_list)