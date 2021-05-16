from flask import Flask, render_template, redirect,session,  request, Response
import re
import random
import string
from datetime import timedelta,datetime

app=Flask(__name__,static_url_path="/frontend/static/", static_folder="../frontend/static", template_folder='../frontend/templates')
app.secret_key = '3232bn3v232kmlfyh6778yr3njrnjuv78vdf8u9dwslcsmkcdjbvbhvgtfegyfy8e38u948294543d5bvhevdrsdfejgkem345kn3m5kn34n534n'
app.permanent_session_lifetime = timedelta(seconds=2)