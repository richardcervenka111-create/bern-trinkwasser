#!/usr/bin/env python3
"""Z data/fountains_raw.json (Overpass) vyrobí fountains.js pre mapu."""
import json, os
here=os.path.dirname(os.path.abspath(__file__)); d=json.load(open(os.path.join(here,'fountains_raw.json')))
out=[]
for x in d['elements']:
    t=x['tags']; am=t.get('amenity'); dw=t.get('drinking_water')
    if am=='drinking_water': kind='dw'; drink='yes' if dw!='no' else 'no'
    else: kind='ft'; drink=dw or 'unknown'
    out.append({'id':x['id'],'lat':round(x['lat'],6),'lon':round(x['lon'],6),'k':kind,'d':drink,'n':t.get('name',''),'l':t.get('location:description:de',''),'w':t.get('wheelchair',''),'b':t.get('bottle','')})
meta={'osm_base':d['osm3s']['timestamp_osm_base'],'bbox':[46.90,7.37,46.99,7.50],'count':len(out)}
open(os.path.join(here,'..','fountains.js'),'w').write('window.FOUNTAINS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\nwindow.FOUNTAINS_META='+json.dumps(meta)+';\n')
print(len(out),'bodov,',sum(1 for o in out if o['d']=='yes'),'pitných')
