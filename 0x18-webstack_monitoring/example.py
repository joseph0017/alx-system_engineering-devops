from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)

# DD_SITE="datadoghq.com" DD_API_KEY="2928d3180a3b300bf77a3c36453449c9" DD_APP_KEY="c0e1588d7c30b14389e13fc8d60704070cd488bf" python3 "example.py"