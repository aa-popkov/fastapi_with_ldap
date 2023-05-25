from dotenv import load_dotenv
from os import getenv

load_dotenv()

DOMAIN_CONTROLLER=getenv("DOMAIN_CONTROLLER")
DOMAIN_TECH_USER=getenv("DOMAIN_TECH_USER")
DOMAIN_TECH_PASS=getenv("DOMAIN_TECH_PASS")