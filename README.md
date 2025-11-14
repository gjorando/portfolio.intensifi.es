# Just my personal portfolio, nothing to see here

## Install

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then cp `portfolio/settings.py_sample` as well as `portfolio_main/app_settings.py_sample` and set the various parameters.

Then generate the locales.

```
./manage.py makemessages -a ## only if you updated your translations
./manage.py compilemessages
```
