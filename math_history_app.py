import streamlit as st

def month_to_number(month):
    months_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    return months_dict.get(month)

def main():
    st.title('Mathematician Of The Day')
    month = st.selectbox('Birth Month:', ('January', 'February', 'March', 'April', 'May', 'June', 'July',
                                           'August', 'September', 'October', 'November', 'December'))
    #day = st.number_input('Birth Day:', min_value=1, max_value=31, value=1)
    day = st.selectbox('Birth Day:', options=range(1,32))

    if st.button('Find a Mathematician'):
        month_number = month_to_number(month)
        url = f"https://mathshistory.st-andrews.ac.uk/OfTheDay/oftheday-{month_number}-{day:02d}/"
        st.write(f"Look here for mathematicians born on {month} {day}")
        st.markdown(f"[{url}]({url})")

if __name__ == "__main__":
    main()
