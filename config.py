from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 25769451
    API_HASH = "7827c57f6d763352104eac8b58d93744"
    # the name to display in your alive message
    ALIVE_NAME = "LegendBoy"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hwffqxra:LZ0wJmLXRv9rCsgTJf5Cnp-i1lqU2YCl@mahmud.db.elephantsql.com/hwffqxra"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "BQAAHmJ14H_E4V1LsGV4hTCjLiN6jqkJp7ndnKkuExuaFOXECEImAj2XXz8qk6ozm684Nj-WMLP_gfoO4CvHko_k77UH25B8pTqpdXEkHFlqS1V-JEeWyRpEbZCaNKIroj9NNKCa0ypCWQLesxWqG084yt3_trPwAEsHgsPScKSlyuCON7mwywfkvIZd6CaWKjuOWjueJV320Id8AF-P665IrQjiSxTiQ6AwNfCxLfRoBi-8bQ5lx0-Q7JTAWiDywugpJLEw8uPvcXd9OiZkFoetslDc5Y_bQXN8d0Qw3lNCdFY1zB2YBIlJPEvjD9zelvGz_s1KvbbWcpUo6d0AffUOAAAAAVpJUgMA"
    BOT_TOKEN = "5813854974:AAGk1ZVF8tGuDigs47Cx_pArPggz1cl7Po8"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/LEGEND-AI/PLUGINS"
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    VCMODE = True
    VC_SESSION = "BQAAHmJ14H_E4V1LsGV4hTCjLiN6jqkJp7ndnKkuExuaFOXECEImAj2XXz8qk6ozm684Nj-WMLP_gfoO4CvHko_k77UH25B8pTqpdXEkHFlqS1V-JEeWyRpEbZCaNKIroj9NNKCa0ypCWQLesxWqG084yt3_trPwAEsHgsPScKSlyuCON7mwywfkvIZd6CaWKjuOWjueJV320Id8AF-P665IrQjiSxTiQ6AwNfCxLfRoBi-8bQ5lx0-Q7JTAWiDywugpJLEw8uPvcXd9OiZkFoetslDc5Y_bQXN8d0Qw3lNCdFY1zB2YBIlJPEvjD9zelvGz_s1KvbbWcpUo6d0AffUOAAAAAVpJUgMA"    # Your City's TimeZone
    TZ = "Asia/Kolkata"
