import scrapy

class BooksScrapperItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    star_rating = scrapy.Field()
