#! /usr/bin/python
import simplejson as json
import urllib
import re
import sys

postcode = sys.argv[1]

data = urllib.urlopen("http://findyourmp.parliament.uk/api/search?q=%s&f=js" % postcode)
constituencies = json.load(data)['results']['constituencies']
if len(constituencies) != 1:
    print "Postcode %s is invalid or maps to multiple constituencies." % postcode
    sys.exit(1)
parsed_data = constituencies[0]

twfy_data = json.load(urllib.urlopen("http://www.theyworkforyou.com/api/getMP?postcode=%s&output=js&key=CqiGfBD4nmmDAFMRR8ETJ6jY" % postcode))

bio_data = urllib.urlopen(parsed_data["member_biography_url"]).read()
prog = re.compile("<strong>Constituency</strong>.*?<p>(.*?)</p>", flags=re.DOTALL)
prog_wm = re.compile("<strong>Westminster</strong>.*?<p>(.*?)</p>", flags=re.DOTALL)
prog_sc = re.compile("<h4>Select committees</h4>.*?<p>(.*?)</p>", flags=re.DOTALL)
def get_details(regexp, data):
    match_obj = regexp.search(data)
    details = re.sub("<.*?>", "", match_obj.group(1))
    details = re.sub("\n[ ]+", "\n", details)
    details = re.sub("^\s+", "", details)
    details = re.sub("\s+$", "", details)
    return details

constituency_details = get_details(prog, bio_data)
parliamentary_details = get_details(prog_wm, bio_data)
committee_details = get_details(prog_sc, bio_data)

print parsed_data["member_name"]
print parsed_data["member_party"]
print constituency_details
print parliamentary_details
print committee_details

if 'office' in twfy_data:
    print twfy_data['office'][0]['position']
else:
    print "! No position"
