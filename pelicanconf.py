## GENERAL SETTINGS ##

AUTHOR = "Guillaume Jorandon"
SITENAME = "Guillaume Jorandon"
# SITESUBTITLE = ""
SITEURL = ""

# Jinja2 extensions
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# Docutils configuration
DOCUTILS_SETTINGS = {
    "initial_header_level": 3
}

PLUGIN_PATHS = ["pelican-renn-plugin/pelican/plugins/"]
PLUGINS = ["pelican_renn_plugin", "i18n_subsites"]

## URLs ##

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

## I18N/L10N SETTINGS ##

TIMEZONE = 'America/Montreal'
I18N_TEMPLATES_LANG = "fr"
DEFAULT_LANG = "fr"
I18N_SUBSITES = {
    "en": dict()
}
LOCALE = "fr_CA"

## FEED GENERATION ##

# Disabled for development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## CONTENT ##

# Source files
PATH = "content"

DEFAULT_PAGINATION = 10

# Lander page only
DIRECT_TEMPLATES = []

# Social links
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/guillaume-jorandon-b088a5116/"),
    ("GitHub", "https://github.com/gjorando"),
)

## THEME ##

THEME = "theme"
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
LANDER_DISPLAY_SOCIALS_IN_FOOTER = True
