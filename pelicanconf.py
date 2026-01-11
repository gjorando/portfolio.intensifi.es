import custom_parse

AUTHOR = "Guillaume Jorandon"
SITENAME = "Guillaume Jorandon"
# SITESUBTITLE = ""
SITEURL = ""

PATH = "./content"

# STATIC_PATHS = [
#     "css"
# ]

TIMEZONE = "America/Montreal"
DEFAULT_LANG = "fr"
I18N_TEMPLATES_LANG = "fr"
I18N_SUBSITES = {
    "en": dict()
}

THEME = "theme"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SOCIALS_IN_FOOTER = True
# MENUITEMS = [
#     ("FOO", "https://perdu.com")
# ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/guillaume-jorandon-b088a5116/"),
    ("GitHub", "https://github.com/gjorando"),
)

DEFAULT_PAGINATION = 10

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
