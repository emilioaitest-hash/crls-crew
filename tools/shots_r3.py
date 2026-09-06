import cdp, json, sys

cdp.launch(2560, 1440)
ws = cdp.connect()
print("href:", cdp.new_page(ws, 'http://localhost:4188/crls-crew/', 2560, 1440))

def snap(sel, name, pad=40):
    box = cdp.ev(ws, f"""(()=>{{const e=document.querySelector({sel!r});
      if(!e)return null;const r=e.getBoundingClientRect();
      window.scrollTo(0, window.scrollY + r.top - {pad});
      return true;}})()""")
    if not box:
        print("MISSING", sel); return
    import time; time.sleep(0.9)
    p = f"/Users/AISandbox/crls-crew/renders/r3-{name}.png"
    cdp.shot(ws, p)
    print("shot", name, p)

snap('.timeline', 'timeline')
snap('.hinge--minor', 'revival')
snap('#chart', 'chart')
snap('.foot', 'footer')
snap('.heat', 'heat')
snap('#gap .silence-count, .silence-count', 'silence')
snap('#field', 'field')
