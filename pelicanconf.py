## GENERAL SETTINGS ##

AUTHOR = "Guillaume Jorandon"
SITENAME = "Guillaume Jorandon"
# SITESUBTITLE = ""
SITEURL = ""

# Jinja2 extensions
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.do", "jinja2.ext.i18n"]
}

# Plugins
PLUGIN_PATHS = ["plugin/pelican/plugins/"]
PLUGINS = ["pelican_renn_plugin", "i18n_subsites"]

# Extract some more metadata about the source file path, ie. the full path, directory, file name, and file name without the extension
PATH_METADATA = r"(?P<full_path>(?P<directory_path>.*)\/(?P<filename_full>(?P<filename_no_ext>.*)\..*))"

## URLs ##

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# /index.html is redefined as the lander page by the special page lander_enable.rst
# So the article list is set under posts/
INDEX_URL = "posts/"
INDEX_SAVE_AS = INDEX_URL + "index.html"

# Archives page is accessible under archives/
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = ARCHIVES_URL + "index.html"

# Period archives are accessible under archives/{yyyy}/ and archives/{yyyy}/{mm}/
YEAR_ARCHIVE_URL = "archives/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = YEAR_ARCHIVE_URL + "index.html"
MONTH_ARCHIVE_URL = "archives/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = MONTH_ARCHIVE_URL + "index.html"

# Authors page is accessible under authors/
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = "authors/index.html"

# Categories page is accessible under categories/
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"

# Tags page is accessible under tags/
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

# Articles are accessible under post/{yyyy}/{mm}/{dd}/{slug}/
ARTICLE_URL = ARTICLE_LANG_URL = "post/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = ARTICLE_LANG_SAVE_AS = ARTICLE_URL + "index.html"

# Pages are accessible under {path of the source file}/{slug}/
PAGE_URL = PAGE_LANG_URL = "{directory_path}/{slug}/"
PAGE_SAVE_AS = PAGE_LANG_SAVE_AS = PAGE_URL + "index.html"

# Authors are accessible under author/{slug}/
AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = AUTHOR_URL + "index.html"

# Categories are accessible under category/{slug}/
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = CATEGORY_URL + "index.html"

# Categories are accessible under tag/{slug}/
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = TAG_URL + "index.html"

## I18N/L10N SETTINGS ##

TIMEZONE = 'America/Montreal'
I18N_TEMPLATES_LANG = "fr"
DEFAULT_LANG = "fr"
I18N_SUBSITES = {
    "en": {
        "LOCALE": "en_US"
    }
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

# We put our articles in a subdirectory, for a clearer separation
ARTICLES_PATHS = [
    "articles"
]

# Source static files
STATIC_PATHS = [
    "images",
]

DEFAULT_ORPHANS = 3  # Minimum number of articles for the last page
DEFAULT_PAGINATION = 12  # Number of articles per page

# Access subsequent pages via <url>/<page number>/
PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{save_as}"),
    (2, "{base_name}/{number}/", "{base_name}/{number}/index.html"),
)

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
DISPLAY_SOCIALS_IN_FOOTER = True

## TAILWIND CSS ##

TAILWINDCSS_ENABLE = True
TAILWINDCSS_VERSION = "v4.1.18"
TAILWINDCSS_MINIFY = False
TAILWINDCSS_INPUT_FILES = [f"{THEME}/static/css/style.css"]