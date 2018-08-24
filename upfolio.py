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
        posts = db.Lynx2
        posts2 = db.Lynx3

        typevalue=""
        sour_value=""
        release_value=""
        website=""
        reddit=""
        twitter=""
        facebook=""
        amountRaisedvalue=""
        icoBonusvalue=""
        minInvestmenvalue=""
        fundingTargetvalue=""
        fundingCapvalue=""
        country=""
        whitePaperresponse=""
        proofTypevalue=""
        hardwareWalletvalue=""
        webWalletvalue=""
        mobileWalletvalue=""
        platformvalue=""
        touxiang=""
        username =""
        zhiwei=""
        linked=""


        titel=response.css('.coinnamenew::text').extract()


        typeList = response.css('.coinbodytext::text').extract()
        if  "Type:" in typeList:
            typevalue = typeList[typeList.index("Type:") + 1]


        if (len(response.css('.coinbodytext::text').extract()) > 3):
            sour_value = response.css('.coinbodytext::text').extract()[4]

        releaselist=response.css('.coinbodytext::text').extract()
        if "Release:" in releaselist:
             release_value = releaselist[releaselist.index("Release:")+1]

        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>0):
            website=response.css('.coinlinkboxnew::attr(href)').extract()[0]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>1):
            reddit = response.css('.coinlinkboxnew::attr(href)').extract()[1]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>2):
            twitter=response.css('.coinlinkboxnew::attr(href)').extract()[2]


        if (len(response.css('.coinlinkboxnew::attr(href)').extract())>3):
             facebook=response.css('.coinlinkboxnew::attr(href)').extract()[3]

        amountRaised = response.css('.coinbodytext::text').extract()
        if "Amount Raised" in amountRaised:
            amountRaisedvalue=amountRaised[amountRaised.index("Amount Raised")+1]


        icoBonus = response.css('.coinbodytext::text').extract()
        if "ICO Bonus" in icoBonus:
            icoBonusvalue=icoBonus[icoBonus.index("ICO Bonus")+1]

        minInvestmen=response.css('.coinbodytext::text').extract()
        if "Min. Investment" in minInvestmen:
            minInvestmenvalue= minInvestmen[minInvestmen.index("Min. Investment")+1]

        fundingTarget=response.css('.coinbodytext::text').extract()
        if "Funding Target" in fundingTarget:
            fundingTargetvalue=fundingTarget[fundingTarget.index("Funding Target")+1]

        fundingCap=response.css('.coinbodytext::text').extract()
        if "Funding Cap" in fundingCap:
            fundingCapvalue=fundingCap[fundingCap.index("Funding Cap")+1]

        countryList = response.css('.coinbodytext::text').extract()
        if "Country" in countryList:
            country = countryList[countryList.index("Country") + 1]

        if(len(response.css('.coinlinkboxnew::attr(href)').extract())>4):
            whitePaperresponse=response.css('.coinlinkboxnew::attr(href)').extract()[4]

        if (len(response.css('.prooftypetext::text').extract()) > 1):
            proofTypevalue=response.css('.prooftypetext::text').extract()[1]
        else:
            proofTypevalue="NO"

        hardwareWallet = response.css('.coinbodytext::text').extract()
        if "Hardware Wall." in hardwareWallet:
            hardwareWalletvalue=hardwareWallet[hardwareWallet.index("Hardware Wall.")+1]


        webWallet=response.css('.coinbodytext::text').extract()
        if "Web Wallet" in webWallet:
            webWalletvalue=webWallet[webWallet.index("Web Wallet")+1]


        mobileWallet=response.css('.coinbodytext::text').extract()
        if "Mobile Wallet" in mobileWallet:
            mobileWalletvalue=mobileWallet[mobileWallet.index("Mobile Wallet")+1]

        platform=response.css('.coinbodytext::text').extract()
        if "Platform" in platform:
            platformvalue=platform[platform.index("Platform")+1]


        teamList = response.css(".collectionitenmteam.w-clearfix.w-dyn-item")

        for item in teamList:
               touxiang=item.css(".teampicture::attr(src)").extract_first()
               username=item.css(".text-block-14::text").extract_first()
               zhiwei= item.css(".text-block-14.tb14::text").extract_first()
               linked = item.css('.linkedinlink::attr(href)').extract()
               post2={
                   "titles": titel,
                   "touxiang": touxiang,
                   "username": username,
                   "zhiwei": zhiwei,
                   "linked": linked
               }
               posts2.insert(post2)
        post = {
                    "titles": titel,
                    "type": typevalue,
                    "sour": sour_value,
                    "release": release_value,
                    "website": website,
                    "reddit": reddit,
                    "twitter": twitter,
                    "facebook": facebook,
                    "amountRaised": amountRaisedvalue,
                    "icoBonus": icoBonusvalue,
                    "minInvestmen": minInvestmenvalue,
                    "fundingTarget": fundingTargetvalue,
                    "fundingCap": fundingCapvalue,
                    "country": country,
                    "whitePaperresponse": whitePaperresponse,
                    "proofType": proofTypevalue,
                    "hardwareWallet": hardwareWalletvalue,
                    "webWallet": webWalletvalue,
                    "mobileWallet": mobileWalletvalue,
                    "platform": platformvalue,
                    }
        print("11111111111")
        print(titel)
        print("11111111111")
        posts.insert(post)




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

                yield scrapy.Request(url=url, callback=self.region_parse)

        # print(titleList) 输出链接集合
