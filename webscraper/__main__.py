import siteScripts.timeout.scraper as timeoutScraper


def main():
    timeoutScraper.scrape()


if __name__ == '__main__':
    # logging.config.fileConfig(fname="./logs/logging.conf",
    #                           disable_existing_loggers=False)
    # logger = logging.getLogger(__name__)
    # logger.info("Let's Begin")

    main()
