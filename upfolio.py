# -*- coding: utf-8 -*-

import scrapy
import pymongo
import random
import time

class UpfolioSpider(scrapy.Spider):
    name = 'upfolio'
    allowed_domains = ['www.upfolio.com']
    start_urls = ['http://www.upfolio.com']

    def region_parse(self, response):
        time.sleep(random.random() * 3)
        connection = pymongo.MongoClient("127.0.0.1", 27017)
        db = connection.Lynx2
        post_lynx_one = db.Lynx2
        post_lynx_two = db.Lynx3

        type_value = ""
        sour_value = ""
        release_value = ""
        website_value = ""
        reddit_value = ""
        twitter_value = ""
        facebook_value = ""
        amountRaised_value = ""
        icobonus_value = ""
        mininvestmen_value = ""
        fundingtarget_value = ""
        fundingcap_value = ""
        country_value = ""
        whitepaperresponse_value= ""
        prooftype_value = ""
        hardwarewallet_value = ""
        webwallet_value = ""
        mobilewallet_value = ""
        platform_value = ""
        avatar_value = ""
        username_value = ""
        position_value = ""
        linked_value = ""
		title_value = ""

        title_value = response.css('.coinnamenew::text').extract()

        typelist = response.css('.coinbodytext::text').extract()
        if  "Type:" in typelist:
            type_value = typelist[typelist.index("Type:") + 1]


        if (len(response.css('.coinbodytext::text').extract()) > 3):
            sour_value = response.css('.coinbodytext::text').extract()[4]

        releaselist=response.css('.coinbodytext::text').extract()
        if "Release:" in releaselist:
             release_value = releaselist[releaselist.index("Release:")+1]

        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>0):
            website_value = response.css('.coinlinkboxnew::attr(href)').extract()[0]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>1):
            reddit_value = response.css('.coinlinkboxnew::attr(href)').extract()[1]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>2):
            twitter_value = response.css('.coinlinkboxnew::attr(href)').extract()[2]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>3):
             facebook_value = response.css('.coinlinkboxnew::attr(href)').extract()[3]

        amountraised = response.css('.coinbodytext::text').extract()
        if "Amount Raised" in amountraised:
            amountRaised_value = amountraised[amountraised.index("Amount Raised")+1]


        icobonus = response.css('.coinbodytext::text').extract()
        if "ICO Bonus" in icobonus:
            icobonus_value = icobonus[icobonus.index("ICO Bonus")+1]

        mininvestmen = response.css('.coinbodytext::text').extract()
        if "Min. Investment" in mininvestmen:
            mininvestmen_value = mininvestmen[mininvestmen.index("Min. Investment")+1]

        fundingtarget = response.css('.coinbodytext::text').extract()
        if "Funding Target" in fundingtarget:
            fundingtarget_value = fundingtarget[fundingtarget.index("Funding Target")+1]

        fundingcap = response.css('.coinbodytext::text').extract()
        if "Funding Cap" in fundingcap:
            fundingcap_value = fundingcap[fundingcap.index("Funding Cap")+1]

        countrylist = response.css('.coinbodytext::text').extract()
        if "Country" in countrylist:
            country_value = countrylist[countrylist.index("Country") + 1]

        if(len(response.css('.coinlinkboxnew::attr(href)').extract())>4):
            whitepaperresponse_value = response.css('.coinlinkboxnew::attr(href)').extract()[4]

        if (len(response.css('.prooftypetext::text').extract()) > 1):
            prooftype_value = response.css('.prooftypetext::text').extract()[1]
        else:
            prooftype_value = "NO"

        hardwarewallet = response.css('.coinbodytext::text').extract()
        if "Hardware Wall." in hardwarewallet:
            hardwarewallet_value = hardwarewallet[hardwarewallet.index("Hardware Wall.")+1]


        webwallet = response.css('.coinbodytext::text').extract()
        if "Web Wallet" in webwallet:
            webwallet_value = webwallet[webwallet.index("Web Wallet")+1]


        mobilewallet = response.css('.coinbodytext::text').extract()
        if "Mobile Wallet" in mobilewallet:
            mobilewallet_value = mobilewallet[mobilewallet.index("Mobile Wallet")+1]

        platform = response.css('.coinbodytext::text').extract()
        if "Platform" in platform:
            platform_value = platform[platform.index("Platform")+1]


        teamlist = response.css(".collectionitenmteam.w-clearfix.w-dyn-item")

        for item in teamlist:
               avatar_value = item.css(".teampicture::attr(src)").extract_first()
               username_value = item.css(".text-block-14::text").extract_first()
               position_value = item.css(".gu-block-14.tb14::text").extract_first()
               linked_value = item.css(".linkedinlink::attr(href)").extract()

               post_two = {
                   "title":title_value,
                   "avatar":avatar_value,
                   "username":username_value,
                   "position":position_value,
                   "linked":linked_value
               }
               post_lynx_two.insert(post_two)
        post_one = {
                    "title":title_value,
                    "type":type_value,
                    "sour":sour_value,
                    "release":release_value,
                    "website":website_alue,
                    "reddit":reddit_value,
                    "twitter":twitter_value,
                    "facebook":facebook_value,
                    "amountraised":amountRaised_value,
                    "icobonus":icobonus_value,
                    "mininvestmen":mininvestmen_value,
                    "fundingtarget":fundingtarget_value,
                    "fundingcap":fundingcap_value,
                    "country":country_value,
                    "whitepaperresponse":whitepaperresponse_value,
                    "prooftype":prooftype_value,
                    "hardwarewallet":hardwarewallet_value,
                    "webwallet":webwallet_value,
                    "mobileallet":mobilewallet_value,
                    "platform":platform_value
                    }
        post_lynx_one.insert(post_one)




    def parse(self, response):
        mixList = response.css('.mix')
        #counts = 0
        for mix in mixList:
            #counts += 1
            #if( counts>15 ):
                #break
            checkString = mix.css(".learnmorecta.w-button::text").extract_first()
            if ( checkString == "Learn More" ):
                title = mix.css('.newcoinname::text').extract_first()
                desc = mix.css('.coinsummarynew::text').extract_first()
                #url = mix.css('.coinlinktop.w-inline-block[href*="/asset/"]::attr(href)').extract_first()
                url = mix.css('a::attr(href)').extract_first()
                #url="https://www.upfolio.com/asset/cloud-cld"

                yield scrapy.Request(url = url, callback = self.region_parse)

        # print(titleList) 输出链接集合
