import urllib, httplib, base64
from httplib import HTTP
import sys
import json
import surrogate_conf

#vip = sys.argv[2]
#action = sys.argv[3]


#READ JSON
def action_list():
    h = HTTP(surrogate_conf.get('hostname'))
    h.putrequest('GET','/module/mod_cluster_admin/vip')
    userpass = "%s:%s" % (surrogate_conf.get('username'),surrogate_conf.get('password'))
    h.putheader('Authorization','Basic '+base64.standard_b64encode(userpass))
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
    elif errcode == 401:
        print "Authentication error."
    else:
        print "HTTP %s: %s" % (errcode,errmsg)
    return


##ADD NEW VIP
def action_create():
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
def action_delete():
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
def action_modify():
    vip = sys.argv[3]
    action = sys.argv[4]
    h = httplib.HTTPConnection('home.shaunkruger.com:8087')
    modification = json.dumps({"action":action})
    header = {'Authorization':'Basic '+base64.standard_b64encode('skruger:testing')}
    h.request('PUT', "/module/mod_cluster_admin/vip/"+vip, modification, header)
    return

##nodes
def action_nodes():
    vip = sys.argv[3]
