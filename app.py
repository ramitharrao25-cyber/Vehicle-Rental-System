import streamlit as st
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Vehicle Rental System",
    page_icon="🚗",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
}

h1,h2,h3{
    color:white;
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

.metric-box{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 0px 15px rgba(0,255,255,0.3);
}

.stButton button{
    width:100%;
    background:#2563EB;
    color:white;
    border-radius:10px;
    height:45px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATABASE CONNECTION
# =========================

def connect_db():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rammi@1968",
        database="VehicleRental"
    )

# =========================
# HEADER
# =========================

st.markdown("""
<h1 style='text-align:center'>
🚗 Vehicle Rental System
</h1>

<h4 style='text-align:center;color:#94A3B8'>
Modern Vehicle Rental Management Dashboard
</h4>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    selected = option_menu(
        "Navigation",
        [
            "Dashboard",
            "Customers",
            "Vehicles",
            "Bookings",
            "Reports"
        ],
        icons=[
            "house",
            "people",
            "car-front",
            "calendar-check",
            "bar-chart"
        ],
        default_index=0
    )

# =========================
# DASHBOARD
# =========================

if selected == "Dashboard":

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM Customer")
    total_customers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Vehicle")
    total_vehicles = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Booking")
    total_bookings = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM Rental")
    total_rentals = cur.fetchone()[0]

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Customers", total_customers)
    c2.metric("Vehicles", total_vehicles)
    c3.metric("Bookings", total_bookings)
    c4.metric("Rentals", total_rentals)

    st.divider()

    st.subheader("System Overview")

    chart_data = pd.DataFrame(
        {
            "Month":["Jan","Feb","Mar","Apr","May"],
            "Bookings":[15,20,30,25,40]
        }
    )

    st.line_chart(
        chart_data.set_index("Month")
    )

    cur.close()
    conn.close()

# =========================
# CUSTOMERS
# =========================

elif selected == "Customers":

    st.subheader("👥 Customer Management")

    tab1,tab2 = st.tabs(
        ["Add Customer","View Customers"]
    )

    with tab1:

        name = st.text_input("Customer Name")
        phone = st.text_input("Phone")
        license_no = st.text_input("License Number")

        if st.button("Add Customer"):

            conn = connect_db()
            cur = conn.cursor()

            sql = """
            INSERT INTO Customer
            (name,phone,license_number)
            VALUES(%s,%s,%s)
            """

            cur.execute(
                sql,
                (name,phone,license_no)
            )

            conn.commit()

            st.success("Customer Added Successfully")

            cur.close()
            conn.close()

    with tab2:

        conn = connect_db()

        query = """
        SELECT *
        FROM Customer
        """

        df = pd.read_sql(
            query,
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        conn.close()

# =========================
# VEHICLES
# =========================

elif selected == "Vehicles":

    st.subheader("🚙 Vehicle Management")

    tab1,tab2 = st.tabs(
        ["Add Vehicle","View Vehicles"]
    )

    with tab1:

        model = st.text_input("Model")

        vtype = st.selectbox(
            "Type",
            ["Car","Bike"]
        )

        price = st.number_input(
            "Rental Price Per Day"
        )

        if st.button("Add Vehicle"):

            conn = connect_db()
            cur = conn.cursor()

            sql = """
            INSERT INTO Vehicle
            (
                model,
                type,
                rental_price_per_day,
                status
            )
            VALUES
            (%s,%s,%s,%s)
            """

            cur.execute(
                sql,
                (
                    model,
                    vtype,
                    price,
                    "Available"
                )
            )

            conn.commit()

            st.success(
                "Vehicle Added Successfully"
            )

            cur.close()
            conn.close()

    with tab2:

        conn = connect_db()

        df = pd.read_sql(
            "SELECT * FROM Vehicle",
            conn
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        conn.close()

# =========================
# BOOKINGS
# =========================

elif selected == "Bookings":

    st.subheader("📅 Booking Management")

    customer_id = st.number_input(
        "Customer ID",
        step=1
    )

    vehicle_id = st.number_input(
        "Vehicle ID",
        step=1
    )

    booking_date = st.date_input(
        "Booking Date"
    )

    if st.button("Create Booking"):

        conn = connect_db()
        cur = conn.cursor()

        sql = """
        INSERT INTO Booking
        (
            customer_id,
            vehicle_id,
            booking_date
        )
        VALUES
        (%s,%s,%s)
        """

        cur.execute(
            sql,
            (
                customer_id,
                vehicle_id,
                booking_date
            )
        )

        conn.commit()

        st.success(
            "Booking Created Successfully"
        )

        cur.close()
        conn.close()

# =========================
# REPORTS
# =========================

elif selected == "Reports":

    st.subheader("📊 Reports")

    report = st.selectbox(
        "Choose Report",
        [
            "Available Vehicles",
            "Customer Rental Details",
            "Vehicle Rental Count"
        ]
    )

    conn = connect_db()

    if report == "Available Vehicles":

        query = """
        SELECT *
        FROM Vehicle
        WHERE status='Available'
        """

    elif report == "Customer Rental Details":

        query = """
        SELECT
        c.name,
        r.start_date,
        r.end_date,
        r.total_amount

        FROM Rental r

        JOIN Booking b
        ON r.booking_id=b.booking_id

        JOIN Customer c
        ON b.customer_id=c.customer_id
        """

    else:

        query = """
        SELECT
        v.type,
        COUNT(*) AS TotalRentals

        FROM Vehicle v

        JOIN Booking b
        ON v.vehicle_id=b.vehicle_id

        GROUP BY v.type
        """

    df = pd.read_sql(
        query,
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    conn.close()