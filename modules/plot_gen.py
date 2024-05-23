import requests
import tempfile
import cdflib
from modules.ip_calulator import *
import io
from modules.ip_plotter import *



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

    try:
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
    except Exception as e:
        return "NO SWE DATASET AVAILABLE TRY ANOTHER !!"