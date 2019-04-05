# ExportMapServiceFields
A script that exports an Esri ArcGIS Server map service schema in physical database diagram format.

The purpose of this script is to create as-built schema documents for map services. These are useful for modeling database diagrams, writing documentation, and proposing database changes. The CSV files can even be committed to Github periodically to track versioning changes.

## Instructions

1. Adjust the settings parameters
2. Run `ExportMapServiceFields.py`

## Settings Reference

The settings file is located in the Settings directory. It is called `ExportMapServiceFields.ini`

If the fs_url service is secured, then you need to provide the token URL, the referrer, the username, and password. If the service is unsecured, then you should leave the token fields blank.

### fs_url

The feature service URL.

Retrieve it by going to the feature's page on ArcGIS Online, and then copying the URL at the lower right corner. The token is not required.

Typical: `https://services.arcgis.com/n`...`W/arcgis/rest/services/`the feature name`/FeatureServer

### token_url

The URL to get a token

Typical: `https://www.arcgis.com/sharing/rest/generateToken`

### token_ref

The token referrer.

Typical: `http://www.arcgis.com` Note: non-secure url.

### token_uname

The ArcGIS user username for token generation. Must have access to the feature service.

### token_pword

The ArcGIS password for the user.
