# Scrapy

## 1. 개요

Scrapy는 python 기반 크롤러 프레임워크이다.

```bash
$pip install Scrapy
$scrapy startproject [프로젝트 이름]
```

## 2. 튜토리얼

`scrapy startproject example`로 프로젝트를 생성하면 아래와 같이 프로젝트 디렉터리가 생성된다.

- `scrapy.cfg`
- example
  - spiders
    - `__init.py__`
  - `items.py`
  - `middlewares.py`
  - `pipelines.py`
  - `settings.py`
  - `__init.py__`

Scrapy에서는 각 프로젝트를 하나의 spider라고 부른다. web을 크롤링한다는 뜻으로 이름을 붙였다.

크롤러를 만들기 위해 `example` 폴더에 실행하고자 하는 python 파일을 생성한다.

*example/spiders/quotes_spider.py*

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

이후 다음 명령어로 실행한다.

```bash
$scrapy crawl quotes
```

또는 직접 파일을 실행 시키는 방법으로는 해당 디렉터리에서 다음 명령어를 입력하면 실행된다.

```bash
$scrapy runspider quotes_spider.py
```

## 3. Spiders 

[공식문서 참고](https://docs.scrapy.org/en/latest/topics/spiders.html)

위의 예제의 `scrapy.Spider`와 같은 클래스는 `Spiders` 클래스 중 하나이며 목적에 맞는 클래스를 선택하여 상속 후 작성하면 된다. 종류는 다음과 같다.

- scrapy.Spider
  
  가장 간단한 spider이지만 다른 모든 spiders도 상속받아 사용되는 핵심적인 클래스이다.

- Generic Spiders

  - CrawlSpider

    가장 일반적으로 사용되는 Spider

  - XMLFeedSpider

    특정 노드 이름으로 반복하여 XML 피드를 구문 분석하도록 설계된 Spider

  - CSVFeedSpider

    XMLFeedSpider와 유사하지만 노드 대신 행을 반복하는 Spider

  - SitemapSpider

    [Sitemap](https://https://www.sitemaps.org/index.html)을 사용하여 URL을 검색을 통해 사이트를 크롤링하게 해주는 spider

각 Spider마다 사용되는 인수는 다르기 때문에 공식문서를 보며 사용하자. 이 문서에서는 CrawlerSpider만 다룰 것이다.

### CrawlerSpider

다음 예제를 통해 알아보자

*example/spiders/article.py*
```python
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import Article

class ArticleSpider(CrawlSpider):
  name = 'articles'
  allowed_domains = ['wikipedia.org']
  start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
  rules = [
    Rule(LinkExtractor(allow='en.wikipedia.org/wiki/((?!:).)*$'),
        callback='parse_items', follow=True)
  ]

  def parse_items(self, response):
    article = Article()
    article['url'] = response.url
    article['title'] = response.css('h1::text').extract_first()
    article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
    
    lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
    article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')

    return article

```

`scrapy.spiders`의 `Rule`은 규칙을 담은 객체이고 `LinkExtractor`는 정규표현식을 받는 인수 `allow`에 맞는 HTML의 링크를 인식하고 반환하도록 한다. 또한 인수 `deny`를 이용하여 정규표현식에 일치하는 링크를 모두 거부할 수 있도록 해준다. 

`Rule`의 인수 `callback`은 페이지 내용을 구문 분석하는 함수이다. 예제에는 없으나 `Rule`의 인수 `follow`는 현재 페이지의 링크를 향후 크롤링에 포함할지 여부를 나타낸다. `callback`이 제공이 되면 기본값이 `True`이고 그렇지 않으면 기본값이 `False`이다.

`Rule`의 인수 `cb_kwargs`는 `callback`에 넘기는 매개변수를 딕셔너리 형태로 입력받는다. 예를 들면 다음과 같이 사용할 수 있다.

```python
class MySpider(CrawlSpider):
  ...
  rules = [
    Rule(LinkExtractor(allow=('category\.php', ), cb_kwargs={'is_article':True})
  ]

  def parse_items(self, response, is_article):
    ...
```

`response.xpath`는 XPath 선택기를 사용하여 추출할 수 있어 텍스트 블록 안의 `<a>` 태그 같은 하위 태그의 텍스트를 포함해 텍스트 컨텐츠를 검색할 때 자주 사용한다.

`response.css`는 CSS 선택기를 사용하여 추출한다.

데이터 저장을 위해 크롤링한 결과를 객체로 정리할 필요가 있다. 예제의 `from example.items import Article`가 그것인데 프로젝트 생성시 기본적으로 생성하는 `items.py`에서 클래스를 정의해야한다.

*example/items.py*

```python
import scrapy

class Article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    lastUpdated = scrapy.Field()
```

Item 객체를 정의하고 나서 다음과 같은 명령어로 실행하면 해당하는 파일 형식으로 결과가 저장된다.

```bash
$scrapy crawl articles -o articles.csv -t csv
$scrapy crawl articles -o articles.json -t json
$scrapy crawl articles -o articles.xml -t xml

or

$scrapy runspider articles.py -o articles.csv -t csv
$scrapy runspider articles.py -o articles.json -t json
$scrapy runspider articles.py -o articles.xml -t xml
```

