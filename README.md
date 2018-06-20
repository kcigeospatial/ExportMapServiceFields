# ExportMapServiceFields
A script that exports an Esri ArcGIS Server map service schema in physical database diagram format.

The purpose of this script is to create as-built schema documents for map services. These are useful for modeling database diagrams, writing documentation, and proposing database changes. The CSV files can even be committed to Github periodically to track versioning changes.

## Instructions

To adjust the parameters, see the Settings/ExportMapServiceFields.ini file. If the fs_url service is secured, then you need to provide the token URL, the referrer, the username, and password. If the service is unsecured, then you should leave the token fields blank.

As an example, for AGOL, the following should be used:
-	token_url: https://www.arcgis.com/sharing/rest/generateToken
-	token_ref: http://www.arcgis.com
-	token_uname: AGOL username
-	token_pword: AGOL password 
