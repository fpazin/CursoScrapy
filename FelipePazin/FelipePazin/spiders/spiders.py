import scrapy
from FelipePazin.items import FelipePazinItem

class QuotesSpider(scrapy.Spider):
    name = "ufmg"
    #UFPA
    #start_urls = ['http://repositorio.ufpa.br/jspui/simple-search?query=saude+mental']

    #UFMG
    start_urls = ['http://www.bibliotecadigital.ufmg.br/dspace/search?query=saude+mental&submit=Go']

    custom_settings ={'ITEM_PIPELINES':
         {
             'FelipePazin.pipelines.FelipePazinPipeline': 400
         },
        'LOG_FILE':'FelipePazin.log',
        'FEED_FORMAT':'csv',
        #'JOBDIR':'crawls\\FelipePazin',
        'FEED_URI':'FelipePazin_Resultado.csv'
    }
    def parse(self, response):
        item = FelipePazinItem()
        #UFPA
        # link = response.css('div table tr')
        # link1 = response.css('div table tr td:nth-child(2) a')
        # for link in link1: #Link completo dos artigos (linkfull).
        #     url_artigo = link.css('a').attrib['href']
        #     linkfull = ('http://repositorio.ufpa.br') + url_artigo
        #     print("Links de acesso da pag:",linkfull)
        #     yield scrapy.Request(linkfull,callback=self.extrair)

        #UFMG

        link = response.css('ul.ds-artifact-list li div.item_metadata_slider.hidden').get()
        links1 = response.css('ul.ds-artifact-list li div.item_metadata_slider.hidden td:nth-child(2)::text').get()
        print("Estrutura0:", link)
        print("Resumo0:", links1)
        # for link in links1:
        #     print("Estrutura:",link)
        #     print("Resumo:",links1)

    def extrair(self,response):
        item = FelipePazinItem()
        # PegaData = response.css('div table tbody tr:nth-child(1)')  #Pegando a Data - UFPA
        # print("Data:",PegaData)

        # #Pegando Autor - UFPA
        # RefAutor = response.css('div table tr td')
        # print("Ref do Autor na pag:", RefAutor)
        # item['autor'] = RefAutor.css('a').attrib['href']
        # #item['autor'] = response.css('div table tr td:nth-child(3) a').get(attrib['href'])
        # print("Extrair Autor",item['autor'])
        # yield item

















        # for div in divs:
        #     item['data'] = div.css('div td,text::text').extract_first()
        #     item['div'] = div.css('div td a,text::text').extract_first()
        #     item['autor'] = div.css('div td em').extract_first()
        #     yield item
        #  proxima = response.css('ul.pager li.next a::attr(href)')
        #  if proxima is not None:
        #      proxima = response.urljoin(proxima)
        #      yield scrapy.Request(proxima, callback=self.parse)
