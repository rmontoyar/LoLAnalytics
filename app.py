import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output


#Data_to_be_plotted - imported manually due to time constraints
data_df_master=pd.DataFrame({"WinRate":[60.59, 58.83, 56.73, 50.68, 40.87, 87.47, 61.13, 53.96, 45.16, 31.69, 58.84, 58.04, 52.83, 50.11, 42.40, 57.27, 52.74, 50.94, 44.30, 44.06, 64.82, 62.82, 57.87, 42.79, 39.33],
                      "Role":["Top","Top","Top","Top","Top","Jungle","Jungle","Jungle","Jungle","Jungle","Mid","Mid","Mid","Mid","Mid","ADC","ADC","ADC","ADC","ADC","Support","Support","Support","Support","Support"],
                      "Skill": "Master",
                      "Name":["Riven","Fiora","Sylas","Camille","Aatrox","Kindred","Kha'Zix","Lee Sin","Viego","Graves","Yasuo","Veigar","Diana","Ekko","Ahri","Kai'Sa","Ezreal","Lucian","Jinx","Xayah","Senna","Soraka","Pyke","Nautilus","Karma"]
                      })
data_df_best_composition_master=pd.DataFrame({"WinRate":[60.59, 87.47, 58.84, 57.27, 64.82],
                      "Role":["Top","Jungle","Mid","ADC","Support"],
                      "Skill": "Master",
                      "Name":["Riven","Kindred","Yasuo","Kai'Sa","Senna"]
                      })

data_df_grandmaster=pd.DataFrame({"WinRate":[62.13,56.44,55.58,53.69,39.87,77.82,64.24,48.64,46.60,32.77,63.46,60.27,54.89,50.70,42.45,72.86,53.93,49.27,47.68,37.85,72.84,70.36,58.66,37.93,35.77],
                      "Role":["Top","Top","Top","Top","Top","Jungle","Jungle","Jungle","Jungle","Jungle","Mid","Mid","Mid","Mid","Mid","ADC","ADC","ADC","ADC","ADC","Support","Support","Support","Support","Support"],
                      "Skill":"GrandMaster", 
                      "Name":["Akali","Gangplank","Fiora","Camille","Aatrox","Kindred","Kha'Zix","Lee Sin","Viego","Graves","Talon","Qiyana","Veigar","Zed","Ahri","Jhin","Lucian","Ezreal","Jinx","Xayah","Senna","Soraka","Pyke","Nautilus","Karma"]
                      })
data_df_best_composition_grandmaster=pd.DataFrame({"WinRate":[62.13,77.82,63.46,72.86,72.84],
                      "Role":["Top","Jungle","Mid","ADC","Support"],
                      "Skill":"GrandMaster", 
                      "Name":["Akali","Kindred","Talon", "Jhin","Senna"]
                      })

data_df_challenger=pd.DataFrame({"WinRate":[59.61,54.73,49.73,44.78,38.79,85.89,62.29,50.60,48.07,34.76,82.24,65.02,60.07,38.06,37.88,73.15,50.99,45.80,44.30,39.39,72.10,69.28,68.58,40.08,35.76],
                      "Role":["Top","Top","Top","Top","Top","Jungle","Jungle","Jungle","Jungle","Jungle","Mid","Mid","Mid","Mid","Mid","ADC","ADC","ADC","ADC","ADC","Support","Support","Support","Support","Support"],
                      "Skill":"Challenger", 
                      "Name":["Gangplank","Camille","Akali", "Fiora","Aatrox","Lillia", "Kindred","Lee Sin","Viego","Graves", "Viktor","Veigar","Yasuo","Ahri","Zed","Miss Fortune","Jinx","Lucian","Ezreal","Xayah","Pyke","Soraka","Senna","Karma","Nautilus"]
                      })
data_df_best_composition_challenger=pd.DataFrame({"WinRate":[59.61,85.89,82.24,73.15,72.10],
                      "Role":["Top","Jungle","Mid","ADC","Support"],
                      "Skill":"Challenger", 
                      "Name":["Gangplank","Lillia", "Viktor","Miss Fortune","Pyke"]
                      })

data_df_all=pd.concat([data_df_master,data_df_grandmaster,data_df_challenger],ignore_index=True)
data_df_all_best_comps=pd.concat([data_df_best_composition_master, data_df_best_composition_grandmaster, data_df_best_composition_challenger])
 
def empty_figure():
    df = data_df_all
    mask = df["Skill"] == "None"  
    fig = px.bar(df[mask],x="Name", y="WinRate", template="plotly_dark",
            color="Role", barmode="group",
            labels={"Name":"Champion name","WinRate":"Win Rate (%)"})
    return fig 

styles={
    'pre':{
        'border':'thin lightgrey solid',
        'overflowX':'scroll'
    }
}

app = dash.Dash(__name__)
app.layout = html.Div([
    
    html.Div([
        html.Img(src='assets/icon.png'),
        html.H1('League of Legends Analytics'),
        html.Img(src='assets/icon.png')
    ], className = 'banner'),

    html.Div([
        dcc.Dropdown(   
                    id="dropdown",
                    options=[
                        {"label":"Challenger","value":"Challenger"},
                        {"label":"GrandMaster","value":"GrandMaster"},
                        {"label":"Master","value":"Master"}              
                        ],
                        multi=False,
                        placeholder="Pick the skill rating to visualize"
                    )
    ], className="dropdown-container"),
    html.Div([
        html.Div([
            dcc.Graph(id = 'graph_1', figure=empty_figure())
        ], className = 'create_container2 seven columns'),

        html.Div([
            html.Img(id = 'card_showcase', className='card_format', src="assets/champions/None.png")
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

    html.Div([
        html.Span(id='roster_title',children="", className="roster-title"),
        html.Div([
            html.Img(id='top_card',className='card_format',src="assets/champions/None.png"),
            html.Img(id='jungle_card',className='card_format',src="assets/champions/None.png"),
            html.Img(id='mid_card',className='card_format',src="assets/champions/None.png"),
            html.Img(id='ADC_card',className='card_format',src="assets/champions/None.png"),
            html.Img(id='support_card',className='card_format',src="assets/champions/None.png")],
         className="roster-card-container")
         
    ], className='create_container2 eleven columns')

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output("graph_1", "figure"), 
    Input("dropdown", "value")
)
def update_bar_chart(skill):
    
    df = data_df_all
    mask = df["Skill"] == skill   
    if str(skill)!="None":
        fig = px.bar(df[mask], x="Name", y="WinRate", template="plotly_dark",
                    color="Role", barmode="group",
                    labels={
                        "Name": "Champion name",
                        "WinRate": "Win Rate (%)"
                    })
        fig.update_layout(title={'text':str("Win Rate per champion and role for "+str(skill)),'x':0.5})
        fig.update_traces(width=0.5)
        return fig
    else:
        return empty_figure()
    
@app.callback(
    Output("top_card","src"),
    Output("jungle_card","src"),
    Output("mid_card","src"),
    Output("ADC_card","src"),
    Output("support_card","src"),
    Output("roster_title","children"),
    Input("dropdown", "value")
)
def update_composition_cards(skill):
    df=pd.DataFrame()
    if str(skill)!="None":
        if str(skill)=="Master":
            df=data_df_best_composition_master
        elif str(skill)=="GrandMaster":
            df=data_df_best_composition_grandmaster
        else:
            df=data_df_best_composition_challenger
        return ("assets/champions/"+str(df['Name'][0])+".png", 
                "assets/champions/"+str(df['Name'][1])+".png", 
                "assets/champions/"+str(df['Name'][2])+".png",
                "assets/champions/"+str(df['Name'][3])+".png",
                "assets/champions/"+str(df['Name'][4])+".png",
                "Best Win Rate Roster in "+str(skill)
                )
    else:
        return ("assets/champions/None.png", 
                "assets/champions/None.png", 
                "assets/champions/None.png",
                "assets/champions/None.png",
                "assets/champions/None.png",
                "")     
               
@app.callback(
    Output('card_showcase','src'),
    [Input('graph_1','hoverData')]
)
def update_card_image(hoverData):
    if str(hoverData)==None:
        return "assets/champions/None.png"
    try:
        champion_name=str(hoverData['points'][0]['x'])  
        return "assets/champions/"+champion_name+".png"
    except:
        return "assets/champions/None.png"
    
if __name__ == ('__main__'):
    app.run_server(debug=False)
