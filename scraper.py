class JobScrape():

    def __init__(self, site_name):
        """Having the job sites in a ist means we can check on initialisation and throw an error if the site is not available."""

        sites = [{"monster": {
                    "url": "https://www.monster.co.uk/jobs/search/",
                    "query_format": "?q={keywords}&where={city}&cy={country}",
                    "results": "#ResultsContainer",
        }}]

        """First property - list comprehension - need to google"""

        self.site_data = [site[site_name] for site in sites if site_name in site[0]]

        """Second property - site name variable that we passed in when we intialized the class"""

        self.site_name = site_name
        print(self.site_data)
        print(self.site_name)



    def _format_monster():
        pass

    def _get_description():
        pass

    def _scrape_site():
        pass

    def get_jobs():
        pass

    