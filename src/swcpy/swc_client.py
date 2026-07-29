import httpx


class SwcClient:

    def __init__(self, swc_base_url: str):
        self.swc_base_url = swc_base_url

    def get_health_check(self):
        # make the API call to the health check endpoint
        with httpx.Client(base_url=self.swc_base_url) as client:
            return client.get("/")
