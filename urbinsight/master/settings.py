# -*- coding: utf-8 -*-

###############################################
# Geosite settings
###############################################

import os
from geonode.contrib import geosites

# Directory of master site - for GeoSites it's two up
GEOSITES_ROOT = os.path.dirname(geosites.__file__)
#PROJECT_ROOT = os.path.dirname(urbinsight.__file__)
SITE_ROOT = os.path.dirname(__file__)

#TEMPLATE_DIRS = (
#   os.path.join(SITE_ROOT, 'templates/'),
#   os.path.join(GEONODE_ROOT, 'templates/')
#)

#STATICFILES_DIRS = (
#    os.path.join(SITE_ROOT, 'static/'),
#    os.path.join(GEONODE_ROOT, 'static/')
#)

try:
    # read in project pre_settings
    execfile(os.path.join(SITE_ROOT, '../', 'pre_settings.py'))
except:
    # if not available, read in GeoSites pre_settings
    execfile(os.path.join(GEOSITES_ROOT, 'pre_settings.py'))


SITE_ID = 1
SITE_NAME = 'Master'
# Should be unique for each site
SECRET_KEY = "ebk3CC3N6jt1AU9mGIcI"

# site installed apps
SITE_APPS = ()

# Site specific databases
SITE_DATABASES = {}

##### Overrides
# Below are some common GeoNode settings that might be overridden for site

# admin email
#THEME_ACCOUNT_CONTACT_EMAIL = ''

# Have GeoServer use this database for this site
#DATASTORE = ''

# Allow users to register
#REGISTRATION_OPEN = True

# Read in GeoSites post_settings
try:
    # read in project pre_settings
    execfile(os.path.join(SITE_ROOT, '../', 'post_settings.py'))
except:
    # if not available, read in GeoSites pre_settings
    execfile(os.path.join(GEOSITES_ROOT, 'post_settings.py'))
