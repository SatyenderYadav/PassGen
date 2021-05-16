from function.function import *

@app.route('/')
def index_route():
          
  session['password'] = ''

  return render_template("index.html")

@app.route('/generate', methods=['GET', 'POST'])
def gen_route():
 
  message=''
  iserror=0                         
  if request.method == 'POST':
    try:
      formdata=request.form
      reg1,err1=password_generation(data=formdata)
      return redirect(("/generate"))
      
    except Exception as e:

      
      message='Some error occured'
      iserror=1

  return render_template("generator.html", mssg=message, iserror=iserror)

 
@app.route('/strength', methods=['GET', 'POST'])
def strength_route():
 
  message=''
  iserror=0                         
  if request.method == 'POST':
    try:
      formdata=request.form
      reg1,err1=check_password_strength(data=formdata)
      return redirect(("/strength"))
      
    except Exception as e:

      
      message='Some error occured'
      iserror=1

  return render_template("passstrength.html", mssg=message, iserror=iserror) 

if __name__=='__main__': app.run(debug=True)