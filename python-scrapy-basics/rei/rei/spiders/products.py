import scrapy
# import CrawlSpider to crawl product listings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ReiItem
from scrapy.loader import ItemLoader

class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["rei.com"]
    start_urls = ["https://rei.com/c/camping-and-hiking/f/scd-deals"]

    rules = (
        Rule(LinkExtractor(allow=(r"page=",))),
        Rule(LinkExtractor(allow=(r"product",)), callback="parse_item"),
    )
    # Paste HTML selectors that you want to query off of -> find them using shell searching
    def parse_item(self, response):
        '''
        response.css("h1#product-page-title::text").get()
        response.css("span#buy-box-product-price::text").get()
        response.css("span#product-item-number::text").get()
        response.css("span.cdr-rating__number_13-5-3::text").get()
        '''
        l = ItemLoader(item=ReiItem(), response=response)
        l.add_css("title", "h1#product-page-title")
        l.add_css("price", "span#buy-box-product-price")
        l.add_css("item_no", "span#product-item-number")
        l.add_css("rating", "span.cdr-rating__number_13-5-3")

        return l.load_item()


        # item = ReiItem()
        # yield {
        #     "title": response.css("h1#product-page-title::text").get(),
        #     "price": response.css("span#buy-box-product-price::text").get(),
        #     "item_no": response.css("span#product-item-number::text").get(),
        #     "rating": response.css("span.cdr-rating__number_13-5-3::text").get(),
        # }

    