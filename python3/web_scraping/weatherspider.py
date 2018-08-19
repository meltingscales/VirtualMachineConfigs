import scrapy


class WeatherSpider(scrapy.Spider):
    name = "weatherspider"
    start_urls = ['https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US']

    def parse(self, response):
        for row in response.css('tbody tr'):
            yield {
                'description': row.css('td.description span::text').extract_first()
            }
