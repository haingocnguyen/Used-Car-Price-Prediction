import streamlit as st

st.set_page_config(layout="wide")
def wide_display():
    st.markdown("""
        <style>
        .reportview-container .main .block-container {
            max-width: 95%;
        }
        .reportview-container .main {
            color: #000000;
            background-color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            font-size: 20px;
            height: 3em; width: 100%;
            border-radius: 10px;
            border: 2px solid #FFD700;
            background-color: #FFD700;
            color: black;
        }
        .bigger-font {
            font-size: 18px;  /* Increase font size */
            text-align: center;  /* Center align the text */
        }
        .centered-text {
            text-align: center;
        }
        </style>""", unsafe_allow_html=True)
def apply_custom_styles():
    st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            font-weight: bold;
        }
        .custom-header {
            background-color: #f63366;
            color: white;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Home'
def home_page():
    st.title('CAR PRICE PREDICTION ANALYSIS')
    st.image(r'D:\DOWNLOADS\GIT Repo\Used-Car-Price-Prediction\lib\giphy(1).gif')
    
    st.header('Group Members')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Names**")
        st.write("""
                    1. Nguyen Hai Ngoc
                    2. Hoang Tuan Kiet
                    3. Phan Quoc Anh
                    4. Nguyen Trong Tien
                    5. Nguyen Trinh Phuong Nguyen""")
    with col2:
        st.markdown("**Student's ID**")
        st.write("""
                    - ITDSIU21057
                    - ITDSIU21055
                    - ITDSIU21001
                    - IELSIU21386
                    - IELSIU21337""")
    
    with col3:
        st.markdown("**Roles**")
        st.write("""
                    - EDA and report constructing
                    - Quantitative data processing
                    - Quantitative data processing
                    - Categorical data processing
                    - Data preprocessing and slides designing
                 """)


def data_preprocessing():
    st.header('Data Preprocessing')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Drop Columns**")
        if st.button('Drop car_ID'):
            st.write("car_ID dropped!")
    with col2:
        st.markdown("**Convert Data Types**")
        if st.button('Convert symboling'):
            st.write("symboling converted!")

def data_splitting():
    st.header('Data Splitting')
    st.write("This page lets you split the data into categorical and quantitative types.")
    # Example of using an expander
    with st.expander("See explanation"):
        st.write("""
            Here we divide the data based on the types of data in the columns. Categorical types are treated differently from quantitative types.
        """)

def main_content():
    st.title('MAIN CONTENTS')
    
    col1, col2, col3 = st.columns(3)

    # Section 1
    with col1:
        st.markdown('<h2 class="centered-text">Explanatory Data Analysis (EDA)</h2>', unsafe_allow_html=True)
        st.image(r'D:\DOWNLOADS\GIT Repo\Used-Car-Price-Prediction\lib\exploratory-data-analysis-900x615-1.png')
        st.markdown('<p class="bigger-font">Detailed exploration of data to understand insights and relationships.</p>', unsafe_allow_html=True)
    
    # Section 2
    with col2:
        st.markdown('<h2 class="centered-text">Categorical Data Processing</h2>', unsafe_allow_html=True)
        st.image(r'D:\DOWNLOADS\GIT Repo\Used-Car-Price-Prediction\lib\cate.png')
        st.markdown('<p class="bigger-font">Techniques to handle and process categorical variables.</p>', unsafe_allow_html=True)
    # Section 3
    with col3:
        st.markdown('<h2 class="centered-text">Quantitative Data Processing</h2>', unsafe_allow_html=True)
        st.image(r'D:\DOWNLOADS\GIT Repo\Used-Car-Price-Prediction\lib\quanti.png')
        st.markdown('<p class="bigger-font">Methods to analyze and manipulate quantitative data.</p>', unsafe_allow_html=True)
def outlier_detection():
    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        #### Display Text
        `st.text('Hello World')`
        """, unsafe_allow_html=True)
        st.code("st.text('Hello World')")

    with col2:
        st.markdown("""
        #### Display Data
        `st.dataframe(df)`
        """, unsafe_allow_html=True)
        st.code("st.dataframe(df)")

    with col3:
        st.markdown("""
        #### Interactive Widgets
        `st.slider('Select a range', 1, 100)`
        """, unsafe_allow_html=True)
        st.code("st.slider('Select a range', 1, 100)")

    # Row 2
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        #### Columns
        Organize content in columns.
        """, unsafe_allow_html=True)
        st.code("""
        col1, col2 = st.columns(2)
        with col1:
            st.text('Column 1')
        with col2:
            st.text('Column 2')
        """)

    with col2:
        st.markdown("""
        #### Tabs
        Use tabs to organize content.
        """, unsafe_allow_html=True)
        st.code("""
        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            st.text('Content 1')
        with tab2:
            st.text('Content 2')
        """)

    with col3:
        st.markdown("""
        #### Control Flow
        Manage the flow of apps.
        """, unsafe_allow_html=True)
        st.code("if st.button('Click me'): st.text('Hello')")
def section_11():
    st.markdown("""
        <style>
        .bigger-font {
            font-size: 18px;  /* Increase font size */
        }
        </style>""", unsafe_allow_html=True)
    st.title('Section 1.1: Understanding the dataset')
    st.markdown('----------')
    st.header('Dataset Overview: A dataset with 205 records and 26 attributes to examine factors influencing car price')

    import pandas as pd
    import requests
    from io import BytesIO

    url = 'https://github.com/haingocnguyen/Used-Car-Price-Prediction/raw/main/data/CarPrice_Assignment.xlsx'

    # Request the content of the file from the URL
    response = requests.get(url)
    file_content = BytesIO(response.content)

    # Read the content with pandas
    df = pd.read_excel(file_content)

    st.write(df.head())

    st.markdown('----------')
    st.header('The dataset has no missing values or duplicated rows, ensuring the data quality.')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        #### Data information
        """, unsafe_allow_html=True)
        st.code("df.info()")
        st.write(df.dtypes)

    with col2:
        st.markdown("""
        #### Checking missing values
        """, unsafe_allow_html=True)
        st.code("df.isna().sum()")
        st.write(df.isna().sum())
    with col3:
        st.markdown("""
        #### Check for duplicate values
        """, unsafe_allow_html=True)
        st.code("df.duplicated().sum()")
        st.write(df.duplicated().sum())
    
    st.markdown('<p class="bigger-font"></p>', unsafe_allow_html=True)

def section_12():
    st.markdown("""
        <style>
        .bigger-font {
            font-size: 18px;  /* Increase font size */
        }
        </style>""", unsafe_allow_html=True)
    st.title('Section 1.2')
    st.header('Understanding the dataset')

    
    st.markdown('<p class="bigger-font">Dataset Overview: A dataset with 205 records and 26 attributes to examine factors influencing car prices.</p>', unsafe_allow_html=True)

    st.markdown('----------')

def section_13():
    st.title('Section 1.3')

def section_31():
    st.title('Section 3.1')

def section_32():
    st.title('Section 3.2')

def section_33():
    st.title('Section 3.3')

def conclusion():
    st.title('Conclusion and Future work')

def end():
    st.title('The End')
def main():
    wide_display()
    st.sidebar.image(r'D:\DOWNLOADS\GIT Repo\Used-Car-Price-Prediction\lib\statlogo.png', width=300)

    # st.sidebar.subheader("*️⃣ Introduction")
    # choice1 = st.sidebar.radio("Go to", ('📋 Home', '📊 Main Contents',), key='main_nav') 

    # st.sidebar.subheader("1️⃣ Section 1: EDA")
    # choice2 = st.sidebar.radio("Go to", ('Section 1.1: Understanding the dataset', 
    #                                     'Section 1.2: Exploring Categorical Data', 
    #                                     'Section 1.3: Insight from data preprocessing',), key='section1')
    
    # st.sidebar.subheader("2️⃣ Section 2: ...")
    # choice3 = st.sidebar.radio("Go to",('Data Preprocessing', 'Data Splitting', 
    #                                     'Outlier Detection', 
    #                                     ), key='section2')
    
    # st.sidebar.subheader("3️⃣ Section 3: ...")
    # st.sidebar.subheader("4️⃣ Module 4 Analytics Engineering")
    # st.sidebar.subheader("5️⃣ Module 5 Batch Processing")
    # st.sidebar.subheader("⚙️ Workshop 2 Stream Processing")
    
    
    # if choice1 == '📋 Home':
    #     home_page()
    # elif choice1 == '📊 Main Contents':
    #     main_content()

    # if choice2 == 'Section 1.1: Understanding the dataset':
    #     section_11()
    # elif choice2 == 'Section 1.2: Exploring Categorical Data':
    #     section_12()
    # elif choice2 == 'Section 1.3: Insight from data preprocessing':
    #     section_13()

    # if choice3 == 'Data Preprocessing':
    #     data_preprocessing()
    # elif choice3 == 'Data Splitting':
    #     data_splitting()
    # elif choice3 == 'Outlier Detection':
    #     outlier_detection()

    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = None

    with st.sidebar:
        st.subheader("🏠 Home page")
        if st.button("*️⃣ **Introduction**"):
            st.session_state.current_page = home_page
        if st.button("📊 **Main Contents**"):
            st.session_state.current_page = main_content

        st.subheader("1️⃣ Section 1: EDA")
        if st.button("👀 **Understanding the dataset**"):
            st.session_state.current_page = section_11
        if st.button("🔎 **Exploring Categorical Data**"):
            st.session_state.current_page = section_12
        if st.button("🔍 **Exploring Quantitative Data**"):
            st.session_state.current_page = section_13

        st.subheader(" Section 2")
        if st.button(" Hi"):
            st.session_state.current_page = data_preprocessing
        if st.button(" Hii"):
            st.session_state.current_page = data_splitting
        if st.button(" Hiii"):
            st.session_state.current_page = outlier_detection

        st.subheader(" Section 3")
        if st.button(" Hi3"):
            st.session_state.current_page = data_preprocessing
        if st.button(" Hii3"):
            st.session_state.current_page = data_splitting
        if st.button(" Hiii3"):
            st.session_state.current_page = outlier_detection

        st.subheader(" Conclusion")
        if st.button(" Future work"):
            st.session_state.current_page = conclusion
        if st.button(" The end"):
            st.session_state.current_page = end

    # Display the selected page content
    if st.session_state.current_page:
        st.session_state.current_page()



if __name__ == '__main__':
    main()
