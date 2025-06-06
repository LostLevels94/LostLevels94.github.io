AUTHOR = 'Samuel'
SITENAME = 'Lycéens au cinéma'
SITEURL = ""

PATH = "content"
THEME = "themes/sam"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Cité scolaire Hector Berlioz", "http://www.cite-scolaire-berlioz.org/"),
    ("CNC", "https://www.cnc.fr/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False
PLUGINS = ['series']

SERIES_START_TEXT = "Début"
SERIES_CONTINUE_TEXT = "Suite"
SERIES_CONCLUDE_TEXT = "Fin"
SERIES_INDEX_SAVE_AS = 'series/series_index.html'
SERIES_INDEX_URL = 'series/series_index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
