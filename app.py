import numpy as np
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st 

def main():
    st.title("Covid-19 Visualizer")
    st.sidebar.text("Author: Harrison Hoffman")
    st.sidebar.info("https://github.com/hfhoffman1144")
    st.sidebar.info("https://www.linkedin.com/in/harrison-hoffman-utd/")
    st.sidebar.info('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
    data = get_timeseries_data()
    data_global = data.groupby('Date').sum()

    fig0 = go.Figure()
    fig0.add_trace(go.Line(x=data_global.index,y=data_global.Confirmed,name=f'Confirmed global cases'))
    fig0.add_trace(go.Line(x=data_global.index,y=data_global.Recovered,name=f'Recovered global cases'))
    fig0.add_trace(go.Line(x=data_global.index,y=data_global.Deaths,name=f'Global Deaths'))
    fig0.update_layout(title=f'Global Covid-19 Cases')
    st.plotly_chart(fig0)
    
    country = st.selectbox("Select a country",data.Country.unique())
    data_country = data[data['Country'] == country]

    fig = go.Figure()
    fig.add_trace(go.Line(x=data_country.Date,y=data_country.Confirmed,name=f'Confirmed {country} cases'))
    fig.add_trace(go.Line(x=data_country.Date,y=data_country.Recovered,name=f'Recovered {country} cases'))
    fig.add_trace(go.Line(x=data_country.Date,y=data_country.Deaths,name=f'Deaths {country}'))
    fig.update_layout(title=f'{country} Covid-19 Cases')
    st.plotly_chart(fig)

    fig1 = go.Figure()
    fig1.add_trace(go.Line(x=data_country.Date,y=np.diff(data_country.Confirmed),name=f'Confirmed {country} cases'))
    fig1.update_layout(title=f'Rate of Change {country} Covid-19 Cases')
    st.plotly_chart(fig1)


@st.cache(show_spinner=False,allow_output_mutation=True)
def get_timeseries_data():
    url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
    data = pd.read_csv(url, parse_dates=['Date'])
    return data


if __name__ == "__main__":
    main()