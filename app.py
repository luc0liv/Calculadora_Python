from flask import Flask, render_template, request
#criação de caixa de alerta -->> import easygui <<--


app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["input1"] != "" and request.form["input2"] != ""):
            num1=request.form["input1"]
            num2=request.form["input2"]
            opera=request.form["opera"]
       
            soma = int(num1) + int(num2)
            sub = int(num1) - int(num2)
            multi = int(num1) * int(num2)
            divisao=int(num1) / int(num2)

            if(opera == "soma"):    
               return str(soma)

            elif(opera == "sub"):
               return str(sub)

            elif(opera == "multi"):
                return str(multi)
                #return easygui.msgbox(str(multi), title="Resultado")
               
            else:
                return str(divisao)
               #return easygui.msgbox(str(divisao), title="Resultado")
            
        else:
            return render_template("empty.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=8080, debug=True)