import json
import pandas as pd
from flask import (Flask, flash, redirect, render_template,
                   request, session, abort)


data = json.load(open("playlist.json", "r"))
final_list = []

for i in range(0,len(data[next(iter(data))])):
    dict_ = {}
    dict_["index"] = i
    for k,v in data.items():        
        dict_[k] = v[str(i)]        
    final_list.append(dict_)
    
df = pd.DataFrame(final_list)


base_html = """
<!doctype html>
<html><head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.css">
<script type="text/javascript" src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.js"></script>
</head><body>%s<script type="text/javascript">$(document).ready(function(){$('table').DataTable({
    "pageLength": 10
});});</script>
</body></html>
"""

def df_html(df):
    """HTML table with pagination and other goodies"""
    df_html = df.to_html()
    return base_html % df_html

with open('templates/table.html', 'w', encoding="utf-8") as f:
    f.write(df_html(df))
    
    
app = Flask(__name__)


@app.route("/getTable", methods=("POST", "GET"))
def get_table():        
    return render_template("table.html")
    


if __name__ == "__main__":
    app.run() 
        