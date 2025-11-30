import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('final_best_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('P2P risk management',

                           ['Risk status classification'],
                           menu_icon='P2P risk management',
                           icons=['risk'],
                           default_index=0)


# Credit risk Prediction Page

if selected == 'Risk Prediction':

    # page title
    st.title('Risk Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        PC1 = st.text_input('PC1')

    with col2:
        PC2 = st.text_input('PC2')

    with col3:
        PC3 = st.text_input('PC3')

    with col1:
        PC4 = st.text_input('PC4')

    with col2:
        PC5 = st.text_input('PC5')

    with col3:
        PC6 = st.text_input('PC6')

    with col1:
        PC7 = st.text_input('PC7')

    with col2:
        PC8 = st.text_input('PC8')

    with col2:
        PC9 = st.text_input('PC9')


    # code for Prediction
    status_index = ''

    # creating a button for Prediction

    if st.button('Status Test Result'):

        user_input = [PC1,PC2,PC3,PC4,PC5,PC6,PC7,PC8,PC9]

        user_input = [float(x) for x in user_input]

        Risk_prediction = final_test_model.predict([user_input])

        if Risk_prediction[0] == 1:
            status_index = 'The status is default'
        else:
            status_index = 'The status is not default'

    st.success(status_index)



