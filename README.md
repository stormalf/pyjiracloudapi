# pyjiracloudapi

python3 module to call jira cloud api in command line or inside a module.

# pyjiracloudapi.py

python3 pyjiracloudapi.py --help

    usage: pyjiracloudapi.py [-h] [-V] [-U USEREMAIL] [-t TOKEN] [-u URL] [-a API] [-m METHOD] [-J JSONFILE]

    pyjiracloudapi is a python3 program that call jiracloud apis in command line or imported as a module

    optional arguments:
    -h, --help            show this help message and exit
    -V, --version         Display the version of pyjiracloudapi
    -U USEREMAIL, --useremail USEREMAIL
                            jiracloud user email
    -t TOKEN, --token TOKEN
                            jiracloud token
    -u URL, --url URL     jiracloud url
    -a API, --api API     jiracloud api should start by a slash
    -m METHOD, --method METHOD
                            should contain one of the method to use : ['DELETE', 'GET', 'POST', 'PUT']
    -J JSONFILE, --jsonfile JSONFILE
                            json file needed for POST method

Examples:

    Get all application roles :  without any parameters returns the result of "/applicationrole"

    GET /applicationrole: Get all application roles

        python3 pyjiracloudapi.py -u https://{your_domain}.atlassian.net/rest/api/3

    POST /dashboard: Creates a dashboard.

        python3 pyjiracloudapi.py -u https://{your_domain}.atlassian.net/rest/api/3 -a /dashboard -m POST -J dashboard.json

    PUT /dashboard/{id}: Updates a dashboard, replacing all the dashboard details with those provided.

        python3 pyjiracloudapi.py -u https://{your_domain}.atlassian.net/rest/api/3 -a /dashboard/{id} -m PUT -J dashboard.json

    DELETE /dashboard/{id}: Deletes a dashboard.

        python3 pyjiracloudapi.py -u https://{your_domain}.atlassian.net/rest/api/3 -a /dashboard/{id} -m DELETE

# release notes

pyjiracloudapi.py

1.0.0 initial version
