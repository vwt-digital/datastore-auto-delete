# datastore-auto-delete

Function to auto-delete datastore entities based on a kind, field id and interval.

## Setup
1. Create a copy of the `create_datastore_autodelete_func.config.sh` file
2. Update the configuration with the correct variables
3. Add a cloudbuild step to clone this repository
```git clone https://github.com/vwt-digital/datastore-auto-delete.git```
4. Copy the build steps from the `cloudbuild.example.yaml` to your own cloudbuild
5. Make sure the correct config file will be called
