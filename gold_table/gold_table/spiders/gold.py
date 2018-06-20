# -*- coding: utf-8 -*-
import scrapy


class GoldSpider(scrapy.Spider):
	name = 'gold'
	allowed_domains = ["www.investing.com"]
	start_urls = ["https://www.investing.com/commodities/gold-historical-data"]


	def parse(self, response):


		table1 = response.xpath('//table')[3]
		trs = table1.xpath('.//tr')[1:]


		for tr in trs:
			
			date = tr.xpath('.//td[1]//text()').extract()
			price= tr.xpath('.//td[2]//text()').extract()
			opened =tr.xpath('.//td[3]//text()').extract()
			high = tr.xpath('.//td[4]//text()').extract()
			low = tr.xpath('.//td[5]//text()').extract()
			vol = tr.xpath('.//td[6]//text()').extract()
			change_per = tr.xpath('.//td[7]//text()').extract()

			yield{'date': date,
				  'price': price,
				  'opened': opened,
				  'high': high,
				  'low': low,
				  'vol': vol,
				  'change_per': change_per}


		    
