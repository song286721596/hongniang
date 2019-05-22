# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from hongniang.items import HongniangItem
#class HnSpider(CrawlSpider):
class HnSpider(RedisCrawlSpider):
    name = 'hn'
    allowed_domains = ['www.hongniang.com']
    #start_urls = ['https://www.hongniang.com/index/search?&sex=2&starage=2&page=1']
    redis_key = "hn:start_urls"
     # 动态域范围获取
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(HnSpider, self).__init__(*args, **kwargs)
    #第一级别匹配：每一页女性链接匹配规则
    page_links = LinkExtractor(allow=(r"https://www.hongniang.com/index/search\?&sex=2&starage=2&page=\d+"))
    #第二级别匹配:每位女性个人主页的匹配规则
    profile_links = LinkExtractor(allow=(r"https://www.hongniang.com/user/member/id/\d+"))

    rules = (
        Rule(page_links,follow=True),
        Rule(profile_links, callback = "parse_item", follow = False)
    )
    def parse_item(self, response):
        item = HongniangItem()
        #用户名
        item['username'] = self.get_name(response)
        #年龄
        item['age'] = self.get_age(response)
        #头像图片的链接
        item['header_url'] = self.get_header_url(response)
        #相册图片的链接
        item['images_url'] = self.get_images_url(response)
        #内心独白
        item['content'] = self.get_content(response)
        #工作地
        item['workplace'] = self.get_workplace(response)
        #学历
        item['education'] = self.get_education(response)
        #年收入
        item['income'] = self.get_income(response)
        #个人主页
        item['source_url'] = response.url
        #数据来源网站
        item['source'] = "hongniang"

        yield item

    def get_name(self, response):
        username = response.xpath("//div[@class='info1']/div[@class='name nickname']/text()").extract()
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()
    def get_age(self, response):
        age = response.xpath("//div[@class='info2']/div/ul[1]/li[1]/text()").extract()
        if len(age):
            age = age[0]
        else:
            age = "NULL"
        return age.strip()
    def get_header_url(self, response):
        header_url = response.xpath("//ul[@id='tFocus-pic']/li[1]/img[@id='pic_']/@src").extract()
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = "NULL"
        return header_url.strip()
    def get_images_url(self, response):
        images_url = response.xpath("//div[@id='tFocus-btn']/ul/li/img/@src").extract()
        if len(images_url):
            images_url = images_url[0]
        else:
            images_url = "NULL"
        return images_url.strip()
    def get_content(self, response):
        content = response.xpath("//div[@class='info5']/div[@class='text']/text()").extract()
        if len(content):
            content = content[0]
        else:
            content = "NULL"
        return content.strip()
    def get_workplace(self, response):
        workplace = response.xpath("//div[@class='info2']/div/ul[3]/li[2]/text()").extract()
        if len(workplace):
            workplace = workplace[0]
        else:
            workplace = "NULL"
        return workplace.strip()
    def get_education(self, response):
        education = response.xpath("//div[@class='info2']/div/ul[2]/li[2]/text()").extract()
        if len(education):
            education = education[0]
        else:
            education = "NULL"
        return education.strip()
    def get_income(self, response):
        income = response.xpath("//div[@class='info2']/div/ul[3]/li[1]/text()").extract()
        if len(income):
            income = income[0]
        else:
            income = "NULL"
        return income.strip()
