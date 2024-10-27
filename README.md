Several things are needed before accessing Files via API in google drive. 

1. Create a Project in the google cloud. 
2. Set up a service Account to manage access. 
3. Download the Service account json. It service as credential for accessing the data. Therefore it has to be kept secret. 
4. Add the client_email of the service account (found in the .json) to the permised list of viewers in the Google drive Data file(s). 

