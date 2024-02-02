# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np

# # Title of the app
# st.title('Capacitance of Parallel Plate Capacitors with Dielectric Impurity')

# # Conversion factor from micrometers to meters
# um_to_m = 1e-6

# # Fixed permittivity of air (close to vacuum permittivity)
# epsilon_air = 8.854e-12  # in F/m

# # Sliders for the dimensions of the plates in micrometers, converting to meters for calculation
# length_um = st.slider('Length of the plates (l) in micrometers', 100.0, 5000.0, 1000.0)
# breadth_um = st.slider('Breadth of the plates (b) in micrometers', 100.0, 5000.0, 1000.0)
# # Calculate the area of the plates in meters^2
# area = (length_um * um_to_m) * (breadth_um * um_to_m)

# # Slider for the relative permittivity of the dielectric impurity
# relative_epsilon2 = st.slider('Relative Permittivity of Dielectric Impurity (εr2)', 1.0, 10.0, 2.0)
# # Calculate the absolute permittivity of the impurity
# epsilon2 = relative_epsilon2 * epsilon_air

# # Slider for the diameter of the impurity in micrometers, converting to meters for calculation
# impurity_diameter_um = st.slider('Diameter of Dielectric Impurity in micrometers', 10.0, 1000.0, 100.0)
# # Calculate the volume of the impurity in meters^3 assuming it's a sphere
# impurity_volume = (4/3) * np.pi * ((impurity_diameter_um * um_to_m) / 2) ** 3

# # Sliders for the distance between the plates in micrometers, converting to meters for calculation
# min_distance_um = st.slider('Minimum Distance (d) in micrometers', 10.0, 1000.0, 100.0)
# max_distance_um = st.slider('Maximum Distance (d) in micrometers', 100.0, 10000.0, 500.0)
# # Calculate the volume of the capacitor in meters^3 using the max distance
# capacitor_volume = area * (max_distance_um * um_to_m)
# # Calculate the volume fraction of the impurity
# fraction_of_impurity = impurity_volume / capacitor_volume

# # Generate values for distance in meters
# distances = np.linspace(min_distance_um * um_to_m, max_distance_um * um_to_m, 100)

# # Calculate effective permittivity with impurity
# effective_epsilon = (fraction_of_impurity * epsilon2) + ((1 - fraction_of_impurity) * epsilon_air)

# # Calculate capacitances with and without impurity
# capacitances_with_impurity = effective_epsilon * area / distances
# capacitances_without_impurity = epsilon_air * area / distances

# # Create the plot with both capacitances
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_without_impurity, mode='lines', name='With Air'))
# fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_with_impurity, mode='lines', name='With Impurity'))
# fig.update_layout(title='Capacitance vs. Distance between Plates',
#                   xaxis_title='Distance (µm)',
#                   yaxis_title='Capacitance (F)')

# # Show the plot
# st.plotly_chart(fig)

# latex_content = r'''
# ## Capacitance of a Parallel Plate Capacitor

# The equation for the capacitance \(C\) of a parallel plate capacitor is given by:

# $$ C = \frac{\varepsilon A}{d} $$

# Where:
# - \(C\) is the capacitance,
# - $$ (\varepsilon)$$ is the permittivity of the dielectric material,
# - \(A\) is the area of one of the plates,
# - \(d\) is the distance between the plates.
# '''

# # Display the LaTeX content in Streamlit
# st.write(latex_content)


# # LaTeX string for capacitor with impurity
# latex_content_impurity = r'''
# ## Capacitance of a Parallel Plate Capacitor with Dielectric Impurity

# The equation for the effective permittivity \( \varepsilon_{\text{eff}} \) when an impurity is present is given by:

# $$ \varepsilon_{\text{eff}} = f_1 \varepsilon_1 + f_2 \varepsilon_2 $$

# The equation for the capacitance \(C\) of a parallel plate capacitor with this effective permittivity is given by:

# $$ C = \frac{\varepsilon_{\text{eff}} A}{d} $$

# Where:
# - \(C\) is the capacitance,
# - $$ \varepsilon_{\text{eff}} $$ is the effective permittivity of the dielectric material with impurity,
# - $$(f_1)$$ is the volume fraction of the main dielectric material,
# - $$ (\varepsilon_1) $$ is the permittivity of the main dielectric material,
# - $$(f_2)$$ is the volume fraction of the impurity dielectric material,
# - $$ (\varepsilon_2) $$ is the permittivity of the impurity dielectric material,
# - \(A\) is the area of one of the plates,
# - \(d\) is the distance between the plates.
# '''

# # Display the LaTeX content in Streamlit
# st.write(latex_content_impurity)

##########################################

import streamlit as st
import plotly.graph_objects as go
import numpy as np



# Title of the app
st.title('Capacitance of Parallel Plate Capacitors with Dielectric Impurity')

# Conversion factor from micrometers to meters
um_to_m = 1e-6

# Fixed permittivity of air (close to vacuum permittivity)
epsilon_air = 8.854e-12  # in F/m

# Sliders for the dimensions of the plates in micrometers, converting to meters for calculation
length_um = st.slider('Length of the plates (l) in micrometers', 10.0, 15.0, 10.0)
breadth_um = st.slider('Breadth of the plates (b) in micrometers', 2.0, 5.0, 2.0)
# Calculate the area of the plates in meters^2
area = (length_um * um_to_m) * (breadth_um * um_to_m)

# Slider for the relative permittivity of the dielectric impurity
relative_epsilon2 = st.slider('Relative Permittivity of Dielectric Impurity (εr2)', 2.0, 25.0, 15.0)
# Calculate the absolute permittivity of the impurity
epsilon2 = relative_epsilon2 * epsilon_air

# Slider for the diameter of the impurity in micrometers, converting to meters for calculation
impurity_diameter_um = st.slider('Diameter of Dielectric Impurity in micrometers', 0.25, 2.5, 1.50)
# Calculate the volume of the impurity in meters^3 assuming it's a sphere
impurity_volume = (4/3) * np.pi * ((impurity_diameter_um * um_to_m) / 2) ** 3

# Sliders for the distance between the plates in micrometers, converting to meters for calculation
min_distance_um = st.slider('Minimum Distance (d) in micrometers', 1.0, 10.0, 1.0)
max_distance_um = st.slider('Maximum Distance (d) in micrometers', 10.0, 15.0, 10.0)
# Calculate the volume of the capacitor in meters^3 using the max distance
capacitor_volume = area * (max_distance_um * um_to_m)
# Calculate the volume fraction of the impurity
fraction_of_impurity = impurity_volume / capacitor_volume

# Generate values for distance in meters
distances = np.linspace(min_distance_um * um_to_m, max_distance_um * um_to_m, 100)

# Calculate effective permittivity with impurity
effective_epsilon = (fraction_of_impurity * epsilon2) + ((1 - fraction_of_impurity) * epsilon_air)

# Calculate capacitances with and without impurity
capacitances_with_impurity = effective_epsilon * area / distances
capacitances_without_impurity = epsilon_air * area / distances

# Calculate change in capacitance
delta_capacitances = capacitances_with_impurity - capacitances_without_impurity

# Create the plot with both capacitances and change in capacitance
fig = go.Figure()
fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_without_impurity, mode='lines', name='Capacitance without Impurity'))
fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_with_impurity, mode='lines', name='Capacitance with Impurity'))
fig.add_trace(go.Scatter(x=distances * 1e6, y=delta_capacitances, mode='lines', name='Change in Capacitance'))
fig.update_layout(title='Capacitance and Change in Capacitance vs. Distance',
                  xaxis_title='Distance (µm)',
                  yaxis_title='Capacitance (F)',
                  legend_title='Legend')

# Show the plot
st.plotly_chart(fig)



# # Create the plot with both capacitances
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_without_impurity, mode='lines', name='With Air'))
# fig.add_trace(go.Scatter(x=distances * 1e6, y=capacitances_with_impurity, mode='lines', name='With Impurity'))
# fig.update_layout(title='Capacitance vs. Distance between Plates',
#                   xaxis_title='Distance (µm)',
#                   yaxis_title='Capacitance (F)')

# # Show the plot
# st.plotly_chart(fig)

latex_content = r'''
## Capacitance of a Parallel Plate Capacitor

The equation for the capacitance \(C\) of a parallel plate capacitor is given by:

$$ C = \frac{\varepsilon A}{d} $$

Where:
- \(C\) is the capacitance,
- $$ (\varepsilon)$$ is the permittivity of the dielectric material,
- \(A\) is the area of one of the plates,
- \(d\) is the distance between the plates.
'''

# Display the LaTeX content in Streamlit
st.write(latex_content)


# LaTeX string for capacitor with impurity
latex_content_impurity = r'''
## Capacitance of a Parallel Plate Capacitor with Dielectric Impurity

The equation for the effective permittivity \( \varepsilon_{\text{eff}} \) when an impurity is present is given by:

$$ \varepsilon_{\text{eff}} = f_1 \varepsilon_1 + f_2 \varepsilon_2 $$

Relative permittivity for various matrials :"https://en.wikipedia.org/wiki/Relative_permittivity"

The equation for the capacitance \(C\) of a parallel plate capacitor with this effective permittivity is given by:

$$ C = \frac{\varepsilon_{\text{eff}} A}{d} $$

Where:
- \(C\) is the capacitance,
- $$ \varepsilon_{\text{eff}} $$ is the effective permittivity of the dielectric material with impurity,
- $$(f_1)$$ is the volume fraction of the main dielectric material,
- $$ (\varepsilon_1) $$ is the permittivity of the main dielectric material,
- $$(f_2)$$ is the volume fraction of the impurity dielectric material,
- $$ (\varepsilon_2) $$ is the permittivity of the impurity dielectric material,
- \(A\) is the area of one of the plates,
- \(d\) is the distance between the plates.
'''

# Display the LaTeX content in Streamlit
st.write(latex_content_impurity)
