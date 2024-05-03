import streamlit as st
import matplotlib.pyplot as plt
import io
from datetime import datetime
import requests
import tempfile
import cdflib
from cal import *
from plotter import *


def get_selected_date(selected_date):
    return selected_date.strftime("%Y-%m-%d")

def generate_plot(selected_date):
    # Generate a simple plot based on the selected date
    dt = str(selected_date)
    yr = dt.split('-')[0]
    n = dt.replace('-','')
    name  = f'wi_h1_swe_{n}_v01.cdf'
    
    response = requests.get(f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1/{yr}/{name}')
    if response.status_code == 200:

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        cdf = cdflib.CDF(temp_file_path)
    time_range= cdflib.cdfepoch.to_datetime(cdf.varget('epoch'))


    BX,BY,BZ,b_mag = bmagnitude(cdf)
    p_density = thresold(cdf.varget('Proton_Np_moment'),1e4)
    vp = Vp_vec(cdf)
    temp = Temperature(cdf)
    p_beta = plasma_beta(p_density,b_mag,temp)
    tehta_angle,phi_angle = angels(BX,BY,BZ,b_mag)

    
  
    img_buffer = io.BytesIO()

    plot  = Plotting(name)

    plot.ipplot(img_buffer,time_range,b_mag,BX,BY,BZ,tehta_angle,phi_angle,vp,p_density,temp,p_beta)
    
    img_buffer.seek(0)
    return img_buffer

min_year = 2001
max_year = datetime.now().year  # Set the maximum year to the current year

# Display the date input with the calendar widget
selected_date = st.date_input("Select a Date", datetime.now(), min_value=datetime(min_year, 1, 1), max_value=datetime(max_year, 12, 31))

if st.button("Generate Plot"):
    selected_date_str = get_selected_date(selected_date)
    plot_img = generate_plot(selected_date)
    st.image(plot_img, caption='Generated Plot', use_column_width=True)
