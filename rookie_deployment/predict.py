import pandas as pd
import numpy as np
import json
import pickle
import warnings 
warnings.filterwarnings('ignore')
import ast #to convert string to dictionary
from flask import Flask, request, jsonify,render_template,redirect ,url_for

predictors = ['MPpg', 'PTSpg', 'FGpg', '3Ppg', 'FTpg', 'ORBpg', 'DRBpg', 'TRBpg',
       'ASTpg', 'STLpg', 'BLKpg', 'TOVpg', 'PFpg', 'Age', 'Year_index',
       'Team_index', 'FT', 'FT%', 'Games', 'MP', 'FG%']

with open('team_mapper.json') as json_file:
    team_mapper = json.load(json_file)

models ={}
with open('rookie-models.bin', 'rb') as f_in:
    models['lr'],models['lgb'],models['xgb'],models['cats'],models['ada'],models['gbm'],models['rf'] = pickle.load(f_in)

def predict_single(feature_dict_list,models,predictors):
    #feature_dict['Year_index'] = feature_dict['Year'] - 1979
    #feature_dict['Team_index'] = team_mapper[feature_dict['Team']]
    df = pd.DataFrame.from_dict(feature_dict_list)
    df['Year_index'] = df['Year'] - 1979
    df['Team_index'] = df['Team'].map(team_mapper)
    df['TRBpg'] = df['ORBpg']+df['DRBpg']
    df['MP'] = df['MPpg']*df['Games']
    df['FT'] = df['FTpg']*df['Games']

    final_predictions = (
         (models['lr'].predict_proba(df[predictors])[:,1]) +
        (models['lgb'].predict_proba(df[predictors])[:,1]) +
        (models['xgb'].predict_proba(df[predictors])[:,1]) +
        (models['cats'].predict_proba(df[predictors])[:,1])+ 
        (models['ada'].predict_proba(df[predictors])[:,1])+
         (models['gbm'].predict_proba(df[predictors])[:,1])+
         (models['rf'].predict_proba(df[predictors])[:,1])
    )/7
    #final_preds = (final_predictions>=0.52)*1
    return final_predictions[0]#,final_preds



#print(predict_single(feature_dict_list=l,models=models,predictors=predictors))
app = Flask('rookie')
@app.route('/')
def welcome():
    return render_template('index.html') #homepage

@app.route('/submit',methods=['POST'])
def submit():
    #return " submit page"
    if request.method == 'POST':
        #gen = str(request.form['gender'])
        #fetching data from the form
   
        player = {'MPpg': float(request.form['MPpg']),
                'PTSpg': float(request.form['PTSpg']),
                'FGpg': float(request.form['FGpg']),
                '3Ppg': float(request.form['3Ppg']),
                'FTpg': float(request.form['FTpg']),
                'ORBpg': float(request.form['ORBpg']),
                'DRBpg': float(request.form['DRBpg']),
                'TRBpg': 2.9,
                'ASTpg': float(request.form['ASTpg']),
                'STLpg': float(request.form['STLpg']),
                'BLKpg': float(request.form['BLKpg']),
                'TOVpg': float(request.form['TOVpg']),
                'PFpg': float(request.form['PFpg']),
                'Age': float(request.form['Age']),
                'Year': float(request.form['Year']),
                'Team': str(request.form['Team']),
                'FT': 68.0,
                'FT%': float(request.form['FT%'])/100,
                'Games': float(request.form['Games']),
                'MP': 726.0,
                'FG%': float(request.form['FG%'])/100
                } 
    #return jsonify(customer)
    player = str(player) # convert dictionary to string

    return redirect(url_for('predict' , player = player)) # go to predict page and dump the str_dict

@app.route('/predict/<string:player>') # <string: str_dict>
def predict(player):
    player = ast.literal_eval(player) # str to dict

    
    prediction = predict_single(feature_dict_list=[player],models=models,predictors=predictors)

    #prediction = predict_single(customer, dv, model)
    target_5 = prediction >= 0.52
    
    result = {
        'rookie_career>=5 probability': float(np.round(prediction,3)),
        'career>=5': bool(target_5)
    }
    topk = ['Games','Age','MPpg','PTSpg','ASTpg','TRBpg']
    return render_template('result.html',player_passer = player , best_predictors_passer = topk , result_passer = result)#return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
