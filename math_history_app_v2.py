import streamlit as st
import webbrowser
from datetime import datetime

def month_to_number(month):
    months_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    return months_dict.get(month)


months_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December')

current_date = datetime.now()
default_month = current_date.strftime('%B')  # Get current month name (e.g., January)
default_day = current_date.day  # Get current day


def find_index(target_list, search_string):
    try:
        index = target_list.index(search_string)
        return index
    except ValueError:
        return -1


def main():
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.title('Mathematician Of The Day')
        # Add the image to the background
        image = st.image('fractal.jpg')
        st.markdown(f"""
        <style>
        body {{
        background-image: url({image});
        background-size: cover;
        }}
        </style>
        """, unsafe_allow_html=True)
        st.caption('Developed by: Al Yazdani')
        
    
    with col2:
                
        #month = st.selectbox('Month:', ('January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'))
        month = st.selectbox('Month:', options= months_list, index = find_index(months_list, default_month))
        day = st.selectbox('Day:', options=range(1,32), index = default_day-1)
        
        if st.button('Find a Mathematician'):
            month_number = month_to_number(month)
            url = f"https://mathshistory.st-andrews.ac.uk/OfTheDay/oftheday-{month_number}-{day:02d}/"
            st.write(f"The mathematicians who were born on {month} {day}")
            st.markdown(f"[{url}]({url})", unsafe_allow_html=True)
            webbrowser.open_new_tab(url)
            
        st.caption('Information courtesy of MacTutor Index, School of Mathematics and Statistics, University of St Andrews, Scotland')

if __name__ == "__main__":
    main()


