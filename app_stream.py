import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
from modules.plot_gen import generate_plot
import time

def get_selected_date(selected_date):
    return selected_date.strftime("%Y-%m-%d")




# Define the Streamlit sidebar and its elements
with st.sidebar:
    st.markdown("*IP Plot of SWE H1 92 sec timeseries data*")

    st.markdown("Here's a bouquet For You Guys &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    
    st.header('SWE H1 Metadata and parameters')
    st.subheader('Choose operations:  Metdata for Info and PLotting to Visualize Data')
    selected_op= st.sidebar.selectbox('Choose your Operations', ['Metadata Info', 'IP PLOT BY DATE'], key='selected_op')

    st.write('This is Visualizer for SWE Expirement')
    
    st.success(' Disclaimer : Dataset Available it\'s Public', icon='✅')

    st.success(f"Selected OP : {selected_op}")



if selected_op == 'Metadata Info':
    st.subheader("WI_H1_SWE : Wind Solar Wind Experiment, 92-sec Solar Wind")
    st.markdown("**Description :**")
    st.markdown(''' 
                SWE, a comprehensive plasma instrument for the WIND spacecraft, K.W.
     Ogilvie, et al., Space Sci. Rev., 71, 55-77, 1995
                
     Solar wind proton parameters, including anisotropic temperatures, derived by
     non-linear fitting of the measurements and with moment techniques.
     Data reported within this file do not exceed the limits of various parameters
     listed in the following section.  There may be more valid data in the original
     dataset that requires additional work to interpret but was discarded due to the
     limits.  In particular we have tried to exclude non-solar wind data from these
     files. 
                
     We provide the one sigma uncertainty for each parameter produced by the
     non-linear curve fitting analysis either directly from the fitting or by
     propagating uncertainties for bulk speeds, flow angles or any other derived
     parameter.
                
     For the non-linear anisotropic proton analysis, a scalar thermal speed is
     produced by determining parallel and perpendicular temperatures, taking the
     trace, Tscalar = (2Tperp + Tpara)/3 and converting the result back to a thermal
     speed.  The uncertainties are also propagated through
     Notes: Data reported within this file do not exceed the limits of various
     paremeters listed in the following section.  There  may be more valid data in
     the original dataset that require  additional work to interpret but was
     discarded due to the limits.  In particular we have tried to exclude non-solar
     wind data and questionable alpha data from these files. 
                
     We provide the one sigma uncertainty for each parameter produced by the
     non-linear curve fitting analysis either directly from the fitting or by
     propagating uncertainties for bulk speeds, flow angles or any other derived
     parameter.  For the non-linear anisotropic proton analysis, a scalar thermal
     speed is produced by determining parallel and perpendicular tmperatures, taking
     the trace, Tscalar = (2Tperp + Tpara)/3 and converting the result back to a
     thermal speed.  The uncertainties are also.    propagated through  Limits:
     Minimum mach number: 1.5000000;
     Maximum chisq/dof:   100000.00;
     Minimum distance; to bow shock: 5.0000000 [Re]; Maximum
     uncertainty in any; parameter from non-linear;analysis: 70.0000[%].
                ''')
    
    st.markdown('**Parameters :**')
    st.code('''
                Proton_VX_moment ---> Proton velocity component Vx (GSE, km/s) from moment analysis [Proton_VX_moment] Statistical moments of the ion velocity distribution function (VDF) are
                estimated analytically from the  ion current distribution function (CDF).

                Proton_VY_moment ---> Proton velocity component Vy (GSE, km/s) from moment analysis [Proton_VY_moment] Statistical moments of the ion velocity distribution function (VDF) are
                estimated analytically from the  ion current distribution function (CDF).
                
                Proton_VZ_moment ---> Proton velocity component Vz (GSE, km/s) from moment analysis [Proton_VZ_moment] Statistical moments of the ion velocity distribution function (VDF) are
                estimated analytically from the  ion current distribution function (CDF).
                
                Proton_W_moment ---> Proton thermal speed W (km/s) from isotropic moment analysis [Proton_W_moment]
                Statistical moments of the ion velocity distribution function (VDF) are estimated analytically from the  ion current distribution function (CDF).

                Proton_NP_moment ---> Proton number density Np (n/cc) from moment analysis [Proton_Np_moment] Statistical moments of the ion velocity distribution function (VDF) are
                estimated analytically from the  ion current distribution function (CDF).
                
                BX ---> Magnetic field component Bx (GSE, nT) averaged over plasma measurement [BX]
                
                BY ---> Magnetic field component By (GSE, nT) averaged over plasma measurement [BY]
                
                BZ ---> Magnetic field component Bz (GSE, nT) averaged over plasma measurement [BZ]
                ''')

if selected_op=='IP PLOT BY DATE':

    st.markdown("**IP PLOTTING OF SWE H1 DATA**")
    st.markdown("The plotting is available for single day ata a time")
    st.write("Please have paitence it will take some min 😎 try old dates for fast processing !")
    min_year = 1998
    max_year = datetime.now().year  # Set the maximum year to the current year

    # Display the date input with the calendar widget
    selected_date = st.date_input("Select a Date", datetime.now(), min_value=datetime(min_year, 1, 1), max_value=datetime(max_year, 12, 31))


    


    if st.button("Generate Plot"):

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(10, text=progress_text)  
        time.sleep(2)
        my_bar.progress(30 , text=progress_text)
        

        selected_date_str = get_selected_date(selected_date)
        time.sleep(1)
        my_bar.progress(40 , text=progress_text)
        

        plot_img = generate_plot(selected_date)
        if plot_img == "NO SWE DATASET AVAILABLE TRY ANOTHER !!":
            time.sleep(1)
            my_bar.progress(20 , text=progress_text)
            my_bar.empty()

            st.write(plot_img)
        else:

            time.sleep(1)
            my_bar.progress(20 , text=progress_text)
            my_bar.empty()

            st.image(plot_img, caption='Generated Plot', use_column_width=True)
