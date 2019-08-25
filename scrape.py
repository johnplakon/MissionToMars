def scrape():

    from splinter import Browser
    from bs4 import BeautifulSoup
    from datetime import datetime
    import pandas as pd
    import pprint

    pp = pprint.PrettyPrinter(indent=4)

    # Initialize browser
    def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"executable_path": "/Users/jplakon/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

    # Function to scrape NASA title
    def scrape_nasa_title():

        # Initialize browser
        nasa_browser = init_browser()

        # Visit the nasa site
        nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        nasa_browser.visit(nasa_url)

        # Scrape page into soup
        nasa_html = nasa_browser.html
        nasa_soup = BeautifulSoup(nasa_html, "html.parser")

        # Find title
        content_title = nasa_soup.find(
            "div", class_="content_title"
        ).get_text()
        return content_title

    # Function to scrape NASA text
    def scrape_nasa_text():

        # Initialize browser
        nasa_browser = init_browser()

        # Visit the nasa site
        nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        nasa_browser.visit(nasa_url)

        # Scrape page into soup
        nasa_html = nasa_browser.html
        nasa_soup = BeautifulSoup(nasa_html, "html.parser")


        # Find paragraph text
        content_text = nasa_soup.find(
            "div", class_="article_teaser_body"
        ).get_text()
        return content_text


    news_title = scrape_nasa_title()
    news_p = scrape_nasa_text()

    # Function to scrape JPL data
    def scrape_jpl():

        # Initialize browser
        jpl_browser = init_browser()

        # Visit the nasa jpl site
        jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        jpl_browser.visit(jpl_url)

        # Scrape page into soup
        jpl_html = jpl_browser.html
        jpl_soup = BeautifulSoup(jpl_html, "html.parser")

        # Find featured image
        mars_image = "https://www.jpl.nasa.gov/" + jpl_soup.find(
            "section", class_="centered_text clearfix main_feature primary_media_feature single"
        ).find(
        "article", class_="carousel_item"
        )["style"].split()[1][5:57]
        return mars_image


    mars_imageurl = scrape_jpl()

    # Function to scrape weather data
    def scrape_weather():

        # Initialize browser
        weather_browser = init_browser()

        # Visit the mars twitter site
        weather_url = "https://twitter.com/marswxreport?lang=en"
        weather_browser.visit(weather_url)

        # Scrape page into soup
        weather_html = weather_browser.html
        weather_soup = BeautifulSoup(weather_html, "html.parser")

        # Find info
        mars_tweet = weather_soup.find(
            "p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"
        ).text
        mars_tweet

        # Return results
        return mars_tweet

    mars_recent_tweet = scrape_weather()

    # Function to scrape Mars facts
    def scrape_facts():

        # Visit the specefacts site
        facts_url = "https://space-facts.com/mars/"

        mars_facttable = pd.read_html(facts_url)

        # Return results
        mars_factsdf = mars_facttable[0]
        mars_factsdf.rename( columns = {0 : "fact", 1 : "value"})

        mars_factshtml = mars_factsdf.to_html()

        print(mars_factshtml)
        return(mars_factshtml)


    mars_facts = scrape_facts()

    # Function to scrape hemisphere data
    def scrape_hemispheres():

        # Initialize browser
        hemis_browser = init_browser()

        # Visit the Astrogeology site
        hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

        hemis_url1 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
        hemis_url2 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
        hemis_url3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
        hemis_url4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"

        #URL 1
        hemis_browser.visit(hemis_url1)

        # Scrape page into soup
        hemis_html1 = hemis_browser.html
        hemis_soup1 = BeautifulSoup(hemis_html1, "html.parser")

        # Find info
        hemis_photo1 = "https://www.jpl.nasa.gov/" + hemis_soup1.find(
            "img", class_="wide-image"
        )["src"]

        hemis_title1 = hemis_soup1.find(
            "h2", class_="title"
        ).text


        #URL 2
        hemis_browser.visit(hemis_url2)

        # Scrape page into soup
        hemis_html2 = hemis_browser.html
        hemis_soup2 = BeautifulSoup(hemis_html2, "html.parser")

        # Find info
        hemis_photo2 = "https://www.jpl.nasa.gov/" + hemis_soup2.find(
            "img", class_="wide-image"
        )["src"]

        hemis_title2 = hemis_soup2.find(
            "h2", class_="title"
        ).text


        #URL 3
        hemis_browser.visit(hemis_url3)

        # Scrape page into soup
        hemis_html3 = hemis_browser.html
        hemis_soup3 = BeautifulSoup(hemis_html3, "html.parser")

        # Find info
        hemis_photo3 = "https://www.jpl.nasa.gov/" + hemis_soup3.find(
            "img", class_="wide-image"
        )["src"]

        hemis_title3 = hemis_soup3.find(
            "h2", class_="title"
        ).text


        #URL 4
        hemis_browser.visit(hemis_url4)

        # Scrape page into soup
        hemis_html4 = hemis_browser.html
        hemis_soup4 = BeautifulSoup(hemis_html4, "html.parser")

        # Find info
        hemis_photo4 = "https://www.jpl.nasa.gov/" + hemis_soup4.find(
            "img", class_="wide-image"
        )["src"]

        hemis_title4 = hemis_soup4.find(
            "h2", class_="title"
        ).text



        # Store in dictionary
        hemisphere_image_urls = [
        {"title": hemis_title1, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": hemis_title2, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": hemis_title3, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": hemis_title4, "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        ]


        # Return results
        return hemisphere_image_urls

    mars_hemispheres = scrape_hemispheres()

    mars_dict = {
    "news_title" : news_title,
    "news_text" : news_p,
    "mars_image" : mars_imageurl,
    "mars_tweet" : mars_recent_tweet,
    "mars_facts" : mars_facts,
    "mars_hemispheres" : mars_hemispheres
    }

    return(mars_dict)
