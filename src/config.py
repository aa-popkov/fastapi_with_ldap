from dotenv import load_dotenv
from os import getenv

load_dotenv()

DOMAIN_CONTROLLER=getenv("DOMAIN_CONTROLLER")
DOMAIN_TECH_USER=getenv("DOMAIN_TECH_USER")
DOMAIN_TECH_PASS=getenv("DOMAIN_TECH_PASS")
DOMAIN_AUTH_OU=getenv("DOMAIN_AUTH_OU")
DOMAIN_AUTH_FILTER=getenv("DOMAIN_AUTH_FILTER")
