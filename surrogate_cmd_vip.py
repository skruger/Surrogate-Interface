import urllib, httplib, base64
from httplib import HTTP
import sys
import json

#vip = sys.argv[2]
#action = sys.argv[3]


#READ JSON
def list():
    h = HTTP('home.shaunkruger.com:8087')
    h.putrequest('GET','/module/mod_cluster_admin/vip')
    h.putheader('Authorization','Basic '+base64.standard_b64encode('skruger:testing'))
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
        f = h.getfile()
        data= f.read()
        vip = json.loads(data)  # Convert json string to python array object
        formatstr = "%-35s %-8s %s"  # reusable format string for header and data output lines
        print formatstr % ("Address", "Status","Nodes")
        print "==============================================================================="
        for v in vip["items"]:
            print formatstr % (v["address"], v["status"],v["nodes"])
    return


##ADD NEW VIP
def create():
    vip = sys.argv[3]
    h = HTTP('home.shaunkruger.com:8087')
    h.putrequest('POST','/module/mod_cluster_admin/vip/'+vip)
    h.putheader('Authorization','Basic '+base64.standard_b64encode('skruger:testing'))
    h.endheaders()
    errcode, errmsg, headers = h.getreply()
    if errcode == 200:
         f = h.getfile()
         print f.read()
    else:
        print "fail"
    return         

##Disables VIP
def delete():
    vip = sys.argv[3]
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
def modify():
    vip = sys.argv[3]
    action = sys.argv[4]
    h = httplib.HTTPConnection('home.shaunkruger.com:8087')
    modification = json.dumps({"action":action})
    header = {'Authorization':'Basic '+base64.standard_b64encode('skruger:testing')}
    h.request('PUT', "/module/mod_cluster_admin/vip/"+vip, modification, header)
    return

##nodes
def nodes():
    vip = sys.argv[3]
