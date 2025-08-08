import scrapy
from ..items import BooksScrapperItem

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            item = BooksScrapperItem()

            item['title'] = book.css('h3 a::attr(title)').get()
            item['image_url'] = response.urljoin(book.css('div.image_container img::attr(src)').get())
            item['price'] = book.css('p.price_color::text').get()

            availability_list = book.css('p.instock.availability::text').getall()
            item['availability'] = ''.join(availability_list).strip()

            star_classes = book.css('p.star-rating').attrib.get('class')
            item['star_rating'] = star_classes.replace('star-rating', '').strip()

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
