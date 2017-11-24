# -*- coding: utf-8 -*-

from scrapy.spiders import Spider, Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy_cnblogs.items import BotcnblogsItem
import re


class CnblogsSpiderSpider(CrawlSpider):
    name = 'cnblogs_spider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/fengzheng/default.html?page=3']

    rule = (Rule(LinkExtractor(allow=('fengzheng/default.html\?=page\=([\d]+)',), ), callback='parse', follow=True))

    def parse(self, response):
        items = []

        sel = response.selector
        posts = sel.xpath('//div[@id="mainContent"]/div/div[@class="day"]')
        for p in posts:
            item = BotcnblogsItem()
            publishDate = p.xpath('div[@class="dayTitle"]/a/text()').extract_first()
            item["publishDate"] = publishDate
            title = p.xpath('div[@class="postTitle"]/a/text()').extract_first()
            item["title"] = title

            readCount = p.xpath('div[@class="postDesc"]/text()').re_first(u"阅读\(\d+\)")
            regReadCount = re.search(r'\d+', readCount)
            if regReadCount is not None:
                readCount = regReadCount.group()
            item["readCount"] = readCount

            commentcount = p.xpath('div[@class="postDesc"]/text()').re_first(u"评论\(\d+\)")
            regCommentCount = re.search(r'\d+', commentcount)
            if regCommentCount is not None:
                commentcount = regCommentCount.group()
            item["commentCount"] = commentcount
            items.append(item)
        return items
