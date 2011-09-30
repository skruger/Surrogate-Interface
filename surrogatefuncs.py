import urllib, httplib, base64
from httplib import HTTP

#READ JSON
def list():
    h = HTTP('home.shaunkruger.com:8087')
    h.putrequest('GET','/module/mod_cluster_admin/vip')
    h.putheader('Authorization','Basic '+base64.standard_b64encode('skruger:testing'))
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        f = h.getfile()
        print f.read()
    return



##ADD NEW VIP
def create( vip ):
    h = HTTP('home.shaunkruger.com:8087')
    h.putrequest('PUT','/module/mod_cluster_admin/vip/'+vip)
    h.putheader('Authorization','Basic '+base64.standard_b64encode('skruger:testing'))
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
         f = h.getfile()
         print f.read()
    return         

##Disables VIP
def delete( vip ):
    h = HTTP('home.shaunkruger.com:8087')
    h.putrequest('DELETE','/module/mod_cluster_admin/vip/'+vip)
    h.putheader('Authorization','Basic '+base64.standard_b64encode('skruger:testing'))
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
         f = h.getfile()
         print f.read()
    return

##Modify VIP
def modify( vip, action ):
    h = httplib.HTTPConnection('home.shaunkruger.com:8087')
    modification = json.dumps({"action": action})
    #print modification
    header = {'Authorization':'Basic '+base64.standard_b64encode('skruger:testing')}
    h.request('PUT', "/module/mod_cluster_admin/vip/"+vip, modification, header)
    return
