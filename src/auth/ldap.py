import ldap

from config import DOMAIN_CONTROLLER, DOMAIN_AUTH_OU, \
                   DOMAIN_AUTH_FILTER, DOMAIN_USER_DOMAIN

class AuthLDAP:
    LDAP_SERVER = DOMAIN_CONTROLLER
    LDAP_PORT = 389
    LDAP_DN = DOMAIN_AUTH_OU
    ldap_obj = None
    ldap_user_attrs = ["SamAccountName"]
    ldap_filter = DOMAIN_AUTH_FILTER
    ldap_user_domain = DOMAIN_USER_DOMAIN

    def __init__(self) -> None:
        self.ldap_obj = ldap.initialize(f"ldap://{self.LDAP_SERVER}:{self.LDAP_PORT}")
        self.ldap_obj.protocol_version = ldap.VERSION3
        self.ldap_obj.set_option(ldap.OPT_REFERRALS, 0)
    
    def auth(self, username: str, password: str) -> dict:
        try:
            self.ldap_obj.simple_bind_s(
                username+self.ldap_user_domain,
                password
            )
            search = self.ldap_obj.search(
                base=self.LDAP_DN,
                filterstr=self.ldap_filter.format(username),
                scope=ldap.SCOPE_SUBTREE,
                attrlist=self.ldap_user_attrs
            )
            _, user = self.ldap_obj.result(search, 60)

            if len(user) > 0:
                return {'state': True}
            
            return {
                'state': False,
                'msg': 'Not have permisson'
            }
            
        except ldap.INVALID_CREDENTIALS:
            # invalid credentials
            return {
                'state': False,
                'msg': 'Invalid user/passwrod'
            }
        except ldap.LDAPError as e:
            # error connecting to the LDAP server
            return {
                'state': False,
                'msg': f'Error connecting to the LDAP server: {e}'
            }
