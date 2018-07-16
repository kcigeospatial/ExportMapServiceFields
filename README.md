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

The feature service URL. Example: `https://services.arcgis.com/XXXXXXXXXXXXXXXXX/arcgis/rest/services/YYYYYYY/FeatureServer`

### token_url

The URL to get a token, typically: `https://www.arcgis.com/sharing/rest/generateToken`

### token_ref

The token referrer. Typically: `http://www.arcgis.com`

### token_uname

The ArcGIS user username for token generation. Must have access to the feature service.

### token_pword

The ArcGIS password for the user.
