# A single source of truth for constant variables related to the exchange


EXCHANGE_NAME = "coindcx"
BASE_URL_API = "https://api.coindcx.com"
BASE_URL_PUBLIC = "https://public.coindcx.com"
WSS_URL = "wss://stream.coindcx.com"

ERROR_CODES = {
    400: "Bad Request -- Your request is invalid.",
    401: "Unauthorized -- Your API key is wrong.",
    404: "Not Found -- The specified link could not be found.",
    429: "Too Many Requests -- You're making too many API calls.",
    500: "Internal Server Error -- We had a problem with our server. Try again later.",
    503: "Service Unavailable -- We're temporarily offline for maintenance. Please try again later."
}
