# ======================================================================
# [PART_1_START] - Security Lock, Login Form & Main Configurations (PWA REFINED CLEAN UI)
# ======================================================================

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Factory ERP Pro", layout="wide", page_icon="🏭")
# =====================================================================
# 🎯 DATABASE MEMORY LOCK LAYER (RESTORE & INITIALIZE)
# =====================================================================
import os

FACTORY_DB_NAME = 'factory_management.db'

# 1. RESTORE: Agar session state me backup hai, toh use disk par write karein
if "persistent_factory_db_buffer" in st.session_state:
    with open(FACTORY_DB_NAME, "wb") as f_dst:
        f_dst.write(st.session_state["persistent_factory_db_buffer"])
# 2. FALLBACK: Agar disk par file hai par memory khali hai (first load), toh memory me seed karein
elif os.path.exists(FACTORY_DB_NAME):
    with open(FACTORY_DB_NAME, "rb") as f_src:
        st.session_state["persistent_factory_db_buffer"] = f_src.read()
# --- 📱 PWA MOBILE APPLICATION INJECTION LAYER (CLEAN NO-LEAK FIX) ---
st.components.v1.html("""
    <script>
        // Inline web manifest creation directly via JavaScript DOM to prevent Streamlit layout leaking
        var manifestElement = document.createElement('link');
        manifestElement.rel = 'manifest';
        manifestElement.href = 'data:application/json;base64,ewogICJhb縱9uYW1lIjogIk1hbm5hdCBGaXJlcGxhY2UgRVJQIFBybyIsCiAgInNob3J0X25hbWUiIjogIkZhY3RvcnkgRVJQIiwKICAic3RhcnRfdXJsIjogIi4vIiwK  ImRpc3BsYXkiOiAic3RhbmRhbG9uZSIsCiAgImJhY2tncm91bmRfY29sb3IiOiAiIzBmMTcyYSIsCiAgInRoZW1lX2NvbG9yIjogIiMxZTNhOGEiLAogICJpY29ucyI6IFsKICAgIHsKICAgICAgInNyYyI6ICJodHRwczovL2ltZy5pY29uczguY29tL2ZsdWVudC8xOTIvMDAwMDAwL2ZhY3RvcnkucG5nIiwKICAgIC2InNpemVzIjogIjE5MngxOTIiLAogICAgICAidHlwZSI6ICJpbWFnZS9wbmciCiAgICB9LAogICAgewogICAgICAic3JjIjogImh0dHBzOi8vaW1nLmljb25zOC5jb20vZmx1ZW50LzUxMi8wMDAwMDAvZmFjdG9yeS5wbmciLAogICAgICAic2l6ZXMiOiAiNTEyeDUxMiIsCiAgICAgICJ0eXBlIjogImltYWdlL3BuZyIKICAgIH0KICBdCn0=';
        window.parent.document.head.appendChild(manifestElement);

        // Responsive Viewport injection layer
        var metaViewport = window.parent.document.createElement('meta');
        metaViewport.name = 'viewport';
        metaViewport.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
        window.parent.document.head.appendChild(metaViewport);

        // Apple PWA meta tag configurations
        var appleWeb = window.parent.document.createElement('meta');
        appleWeb.name = 'apple-mobile-web-app-capable';
        appleWeb.content = 'yes';
        window.parent.document.head.appendChild(appleWeb);

        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('data:text/javascript;base64,c2VsZi5hZGRFdmVudExpc3RlbmVyKCdmZXRjaCcsIGZ1bmN0aW9uKGV2ZW50KSB7IH0pOw==');
        }
    </script>
""", height=0, width=0)

# --- 🔥 ULTRA-HIGH CONTRAST PREMIUM UI & LOGIN CSS ---
st.markdown("""
    <style>
        .company-header {
            font-size: 42px;
            font-weight: 900;
            color: #1e3a8a;
            letter-spacing: 2px;
            text-align: left;
            margin-bottom: 5px;
            text-transform: uppercase;
            font-family: 'Arial Black', Gadget, sans-serif;
        }
        .main-title {
            font-size: 22px;
            font-weight: 700;
            color: #4b5563;
            letter-spacing: 0.5px;
            padding-bottom: 12px;
            border-bottom: 3px solid #3b82f6;
            margin-bottom: 25px;
        }
        [data-testid="stSidebar"] {
            background-color: #0f172a !important; 
            border-right: 2px solid #1e293b !important;
            padding: 15px 10px !important;
        }
        .sidebar-brand-box {
            background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
            padding: 16px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            border: 1px solid #60a5fa;
        }
        .sidebar-brand-title { color: #ffffff !important; font-size: 16px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin: 0; }
        .sidebar-brand-subtitle { color: #bfdbfe !important; font-size: 11px; font-weight: 600; margin-top: 4px; }
        
        [data-testid="stSidebar"] div[role="radiogroup"] label {
            background-color: #1e293b !important; 
            color: #ffffff !important; 
            border: 1px solid #334155 !important;
            padding: 12px 16px !important;
            border-radius: 10px !important;
            margin-bottom: 12px !important;
            font-weight: 700 !important;
            font-size: 14px !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15) !important;
        }
        [data-testid="stSidebar"] div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] { color: #ffffff !important; }
        [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            border-color: #3b82f6 !important; background-color: #2563eb !important; color: #ffffff !important;
            transform: translateX(6px); box-shadow: 0 0 15px rgba(59, 130, 246, 0.6) !important;
        }
        div[data-testid="stMetric"] {
            background: #ffffff !important; border: 1px solid #e2e8f0 !important; border-left: 6px solid #2563eb !important;
            padding: 18px 22px !important; border-radius: 10px !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
        }
        @media (max-width: 768px) {
            .company-header { font-size: 26px !important; text-align: center !important; }
            .main-title { font-size: 16px !important; text-align: center !important; }
            div[data-testid="stMetric"] { padding: 10px 15px !important; margin-bottom: 10px !important; }
        }
    </style>
""", unsafe_allow_html=True)

# Database connection helper
def get_db_connection():
    return sqlite3.connect('factory_management.db')

# 🔥 AUTOMATIC DATABASE INITIALIZATION GENERATOR WITH HARD-PATCH COLUMNS
def ensure_payments_table_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Base table creation if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee_payments (
            pay_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            emp_name TEXT,
            amount_paid REAL DEFAULT 0.0,
            payment_mode TEXT,
            remarks TEXT
        )
    """)
    conn.commit()
    
    # 2. 🔥 HARD PATCH: Puraani file me agar column miss ho gaya hai toh explicitly inject karega
    try:
        cursor.execute("ALTER TABLE employee_payments ADD COLUMN given_by_supervisor INTEGER DEFAULT 0")
        conn.commit()
    except sqlite3.OperationalError:
        pass
        
    # 3. 🔥 HARD PATCH FOR SALES TABLE: Agar table mein phone number column missing hai toh use automatic add karega
    try:
        cursor.execute("ALTER TABLE sales_new ADD COLUMN party_phone TEXT DEFAULT ''")
        conn.commit()
    except sqlite3.OperationalError:
        pass # Column pehle se hi hai toh safe skip karega
        
    conn.close()

ensure_payments_table_exists()

# --- 🔐 SECURITY SYSTEM WITH SESSION STATE STORAGE ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown('<div style="text-align: center; margin-top: 30px;"><h1 style="color: #1e3a8a; font-weight:900; letter-spacing:1px; margin-bottom:5px;">🏭 MANNAT WIRE NETTING INDUSTRIES</h1><p style="color: #4b5563; font-weight:600;">Enterprise Resource Planning System Secure Gateway</p></div>', unsafe_allow_html=True)
    st.markdown("---")
    
    left_space, login_card, right_space = st.columns([1, 1.2, 1])
    
    with login_card:
        st.markdown("<h3 style='color: #1f2937; font-weight:700; margin-bottom:20px;'>🔒 System Operator Login</h3>", unsafe_allow_html=True)
        
        with st.form("secure_login_form"):
            username = st.text_input("Username / Login ID", placeholder="Enter Operator ID...", key="login_user_id")
            password = st.text_input("Password", type="password", placeholder="Enter Secure Password...", key="login_user_pass")
            
            st.markdown("<br>", unsafe_allow_html=True)
            login_clicked = st.form_submit_button("🔑 Login to System", use_container_width=True, type="primary")
            
            if login_clicked:
                user_clean = str(username).strip().upper()
                pass_clean = str(password).strip()
                
                if user_clean == "MWNI" and pass_clean == "MWNI@2026":
                    st.session_state['logged_in'] = True
                    st.success("✔️ Authorization Successful! Loading System...")
                    st.rerun()
                else:
                    st.error("❌ Invalid Username or Password! Access Denied.")
                
    st.stop()

# --- 🔓 CORE DASHBOARD LOAD (EXECUTES ONLY AFTER SUCCESSFUL LOGIN) ---

# Grand Brand Header Display
st.markdown('<div class="company-header">🏭 MANNAT WIRE NETTING INDUSTRIES</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Advanced Factory Core Management System</div>', unsafe_allow_html=True)

# Sidebar Header Branding & Logout System
st.sidebar.markdown("""
    <div class="sidebar-brand-box">
        <div class="sidebar-brand-title">⚙️ ENTERPRISE ERP</div>
        <div class="sidebar-brand-subtitle">MANNAT CORE UTILITY ENGINE</div>
    </div>
""", unsafe_allow_html=True)

# Session Logout Button
if st.sidebar.button("🚪 Secure Logout", use_container_width=True):
    st.session_state['logged_in'] = False
    st.rerun()

st.sidebar.markdown("---")

# Navigation System Menu WITH NEW WORKER & SUPERVISOR TABS
menu = st.sidebar.radio(
    "Navigation Menu", 
    [
        "🚨 Dashboard & Payment Alerts", 
        "📊 Production Reports (Analytics)",
        "🏗️ Log Daily Production Form", 
        "🧲 Raw Material Inward Purchase",
        "🧾 Sales & Weight Deduction",
        "👥 Workers Hisab-Kitab Ledger",
        "👑 Supervisor (Pappu Nishad)",
        "🛠️ Master Setup (Emp & Rates)"
    ],
    label_visibility="collapsed"
)

# ======================================================================
# [PART_1_END]
# ======================================================================
# ======================================================================
# [PART_2_A_START] - Configuration Setup Matrices & Raw Wire Initialization (WITH DATABASE DOWNLOAD DESK)
# ======================================================================

# --- MASTER SETUP (EMPLOYEE & ROLL RATES) ---
if menu == "🛠️ Master Setup (Emp & Rates)":
    st.subheader("Configuration Master Setup")
    
    # 🔥 NEW FEATURE: CLOUD DATABASE DOWNLOAD BACKUP CENTER
    st.markdown("### 💾 Cloud Data Safe Export Center (Offline Backup)")
    try:
        with open("factory_management.db", "rb") as db_file:
            st.download_button(
                label="📥 Download Live Database File (For Offline System)",
                data=db_file,
                file_name="factory_management.db",
                mime="application/x-sqlite3",
                use_container_width=True,
                type="primary"
            )
        st.caption("ℹ️ Tip: Jab bhi aap online kaam khatam karein, yahan click karke file download karein aur apne offline laptop ke folder me copy-paste kar dein.")
    except Exception as e:
        st.error(f"Database read fail: {str(e)}")
        
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Employees List")
        with st.form("emp_form", clear_on_submit=True):
            e_name = st.text_input("Naye Worker/Employee Ka Naam")
            if st.form_submit_button("Employee Add Karein") and e_name:
                conn = get_db_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO employees (emp_name) VALUES (?)", (e_name.strip(),))
                    conn.commit()
                    st.success(f"{e_name} add ho gaye!")
                except: st.error("Naam pehle se hai!")
                conn.close()
        
        conn = get_db_connection()
        df_emp = pd.read_sql_query("SELECT emp_name as 'Employee Name' FROM employees", conn)
        st.dataframe(df_emp, use_container_width=True)
        conn.close()

    with col2:
        st.markdown("### 🛞 Roll Varieties & Live Stock Configuration")
        with st.form("roll_form", clear_on_submit=True):
            r_name = st.text_input("Roll Ka Type Name (e.g., 50 F Roll)")
            l_rate = st.number_input("Per Roll Worker Ka Paisa (Salary Rate ₹)", min_value=0.0)
            avg_w = st.number_input("Ek Roll Ka Lagbhag Weight (Kg)", min_value=0.0)
            
            if st.form_submit_button("Roll Master Save") and r_name:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT roll_name FROM roll_types WHERE roll_name = ?", (r_name.strip(),))
                row = cursor.fetchone()
                
                if row:
                    cursor.execute("""
                        UPDATE roll_types 
                        SET labor_rate_per_roll = ?, approx_weight_kg = ? 
                        WHERE roll_name = ?
                    """, (l_rate, avg_w, r_name.strip()))
                    st.success(f"🔄 {r_name} ka Rate aur Weight successfully CHANGE ho gaya hai!")
                else:
                    cursor.execute("""
                        INSERT INTO roll_types (roll_name, labor_rate_per_roll, approx_weight_kg) 
                        VALUES (?, ?, ?)
                    """, (r_name.strip(), l_rate, avg_w))
                    st.success(f"✨ Naya Roll {r_name} configuration save ho gaya!")
                conn.commit(); conn.close(); st.rerun()

        st.markdown("---")
        st.markdown("### 🗑️ Delete Roll Variety")
        conn = get_db_connection()
        master_rolls_list = [row[0] for row in conn.execute("SELECT roll_name FROM roll_types").fetchall()]
        conn.close()
        
        if master_rolls_list:
            with st.form("delete_roll_form", clear_on_submit=True):
                roll_to_delete = st.selectbox("Kaun si Category Delete karni hai?", master_rolls_list)
                if st.form_submit_button("❌ Selected Roll Delete Karein"):
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM roll_types WHERE roll_name = ?", (roll_to_delete,))
                    conn.commit(); conn.close()
                    st.warning(f"🗑️ Category '{roll_to_delete}' ko database se delete kar diya gaya hai!")
                    st.rerun()
        
        st.markdown("---")
        st.markdown("### 📊 Active Registered Roll Types")
        conn = get_db_connection()
        df_rolls = pd.read_sql_query("SELECT roll_name as 'Roll Type', labor_rate_per_roll as 'Worker Rate/Roll (₹)', approx_weight_kg as 'Approx Weight (Kg)' FROM roll_types", conn)
        st.dataframe(df_rolls, use_container_width=True)
        conn.close()

# --- RAW MATERIAL INWARD PURCHASE HARD CONFIGURATION MATRIX ---
elif menu == "🧲 Raw Material Inward Purchase":
    st.subheader("Raw Material (Steel Wire Gauge-wise Stock System Hub)")
    conn_init = get_db_connection()
    cursor_init = conn_init.cursor()
    cursor_init.execute("CREATE TABLE IF NOT EXISTS wire_inward_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, date_logged TEXT, gauge_size TEXT, weight_added_kg REAL, timestamp TEXT)")
    cursor_init.execute("CREATE TABLE IF NOT EXISTS wire_sales_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, date_logged TEXT, invoice_no TEXT, party_name TEXT, gauge_size TEXT, weight_deducted_kg REAL, timestamp TEXT)")
    conn_init.commit()
    
    try:
        cursor_init.execute("SELECT invoice_no, party_name, bill_date, total_weight_sold_kg FROM sales_new")
        historical_unprocessed_bills = cursor_init.fetchall()
        for h_bill in historical_unprocessed_bills:
            h_inv, h_party, h_date, h_weight = h_bill
            if h_weight and float(h_weight) > 0.0:
                cursor_init.execute("SELECT COUNT(*) FROM wire_sales_logs WHERE invoice_no = ?", (str(h_inv),))
                if cursor_init.fetchone() == 0:
                    fallback_gauge_line = "24 Gauge"
                    h_timestamp = f"{h_date} 12:00:00"
                    cursor_init.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg - ? WHERE gauge_name = ?", (float(h_weight), fallback_gauge_line))
                    cursor_init.execute("""
                        INSERT INTO wire_sales_logs (date_logged, invoice_no, party_name, gauge_size, weight_deducted_kg, timestamp)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (str(h_date), str(h_inv), str(h_party), fallback_gauge_line, float(h_weight), h_timestamp))
        conn_init.commit()
    except Exception: pass
    conn_init.close()
# ==========================================
# [PART_2_A_END]
# ==========================================
# ==========================================
# [PART_2_B_START] - Manual Date Selection Inward Form & Modification Actions Center
# ==========================================
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📥 Naya Maal Aaya (Inward Form)")
        with st.form("rm_form", clear_on_submit=True):
            # 🔥 INJECTED MANUAL DATE SELECTION FIELD
            inward_user_date = st.date_input("Inward Date (Bill Date)", value=datetime.now().date())
            gauge = st.selectbox("Kaun sa Gauge Aaya?", ["24 Gauge", "25 Gauge", "26 Gauge", "27 Gauge", "Other"])
            custom_gauge = st.text_input("Agar Other hai toh Gauge likhein (Optional)")
            final_gauge = custom_gauge.strip() if gauge == "Other" else gauge
            weight_in = st.number_input("Kitne KG Weight Aaya?", min_value=0.01, step=1.0)
            
            if st.form_submit_button("Stock Me Add Karein") and final_gauge:
                current_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT current_stock_kg FROM raw_material WHERE gauge_name = ?", (final_gauge,))
                row = cursor.fetchone()
                if row:
                    cursor.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg + ? WHERE gauge_name = ?", (weight_in, final_gauge))
                else:
                    cursor.execute("INSERT INTO raw_material (gauge_name, current_stock_kg) VALUES (?, ?)", (final_gauge, weight_in))
                
                # 🔥 BACKFILLING EXPLICIT TARGET USER SELECTION DATE INTO LEDGER
                cursor.execute("INSERT INTO wire_inward_logs (date_logged, gauge_size, weight_added_kg, timestamp) VALUES (?, ?, ?, ?)", (str(inward_user_date), final_gauge, float(weight_in), current_time_stamp))
                conn.commit(); conn.close(); st.success(f"✔️ {weight_in} KG Steel Wire ({final_gauge}) stock me jod di gayi!"); st.rerun()

    with col2:
        st.markdown("### 📊 Current Available Steel Wire Stock")
        conn = get_db_connection()
        df_rm = pd.read_sql_query("SELECT gauge_name as 'Wire Gauge Size', current_stock_kg as 'Stock Available (KG)' FROM raw_material", conn)
        total_inward = float(df_rm['Stock Available (KG)'].sum()) if not df_rm.empty else 0.0
        conn.close()
        st.metric(label="🌟 TOTAL NET WIRE STOCK IN FACTORY (All Gauges Combined)", value=f"{total_inward:,.2f} KG")
        st.dataframe(df_rm, use_container_width=True, hide_index=True)
        
    st.write("---")
    st.markdown("### 📜 Date-Wise Raw Wire Inward Receipts Book")
    conn_df = get_db_connection()
    df_historical_logs = pd.read_sql_query("SELECT id AS 'Receipt ID', date_logged AS 'Date', gauge_size AS 'Gauge Size', weight_added_kg AS 'Received Weight (KG)', timestamp AS 'System Log Time' FROM wire_inward_logs ORDER BY id DESC", conn_df)
    
    if not df_historical_logs.empty:
        st.dataframe(df_historical_logs.style.format({"Received Weight (KG)": "{:,.2f}"}), use_container_width=True, hide_index=True)
        
        # 🔥 USER REQUESTED NEW FEATURE: EXPLICIT MAINTENANCE CENTER GATEWAY
        st.write("")
        st.markdown("### 🛠专 Inward Receipt Logs Edit / Delete Center")
        clean_inward_id_list = [str(i) for i in df_historical_logs['Receipt ID'].tolist()]
        selected_inward_id = st.selectbox("Select Inward Receipt ID to Modify", options=clean_inward_id_list, key="wire_inward_modify_id_dropdown")
        row_in_meta = conn_df.execute("SELECT date_logged, gauge_size, weight_added_kg FROM wire_inward_logs WHERE id=?", (int(selected_inward_id),)).fetchone()
        
        if row_in_meta:
            curr_log_dt_str, curr_log_gauge, curr_log_weight = row_in_meta
            parsed_log_dt = datetime.strptime(curr_log_dt_str, "%Y-%m-%d").date() if "-" in curr_log_dt_str else datetime.now().date()
            
            with st.form("inward_receipt_edit_sub_form_gate"):
                st.write(f"Modifying Inward Receipt ID Reference: **{selected_inward_id}**")
                col_sub_ed1, col_sub_ed2 = st.columns(2)
                with col_sub_ed1:
                    edit_in_date = st.date_input("Correct Inward Date", value=parsed_log_dt)
                    edit_in_gauge = st.text_input("Gauge Group Reference", value=curr_log_gauge, disabled=True)
                with col_sub_ed2:
                    edit_in_weight = st.number_input("Correct Weight Received (KG)", min_value=0.01, value=float(curr_log_weight), step=0.1)
                    
                save_in_changes_btn = st.form_submit_button("💾 Save Modified Inward Entry")
                delete_in_record_btn = st.form_submit_button("🗑️ DELETE THIS INWARD RECEIPT PERMANENTLY")
                
                if save_in_changes_btn:
                    cursor_df = conn_df.cursor()
                    cursor_df.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg - ? WHERE gauge_name = ?", (float(curr_log_weight), curr_log_gauge))
                    cursor_df.execute("UPDATE wire_inward_logs SET date_logged=?, weight_added_kg=? WHERE id=?", (str(edit_in_date), float(edit_in_weight), int(selected_inward_id)))
                    cursor_df.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg + ? WHERE gauge_name = ?", (float(edit_in_weight), curr_log_gauge))
                    conn_df.commit(); st.success("✔️ Inward receipt logs and stock balances successfully corrected!"); st.rerun()
                    
                if delete_in_record_btn:
                    cursor_df = conn_df.cursor()
                    cursor_df.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg - ? WHERE gauge_name = ?", (float(curr_log_weight), curr_log_gauge))
                    cursor_df.execute("DELETE FROM wire_inward_logs WHERE id=?", (int(selected_inward_id),))
                    conn_df.commit(); st.warning("❌ Inward entry destroyed! Balance deducted back."); st.rerun()
    else:
        st.caption("ℹ️ No historical inward entry logs found inside register books.")
    conn_df.close()

# ======================================================================
# [PART_2_B_END]
# ======================================================================
# ======================================================================
# [PART_3_A_NEW_START] - Daily Production Form & Grouping Summary Reports
# ======================================================================

# --- LOG DAILY PRODUCTION FORM ---
elif menu == "🏗️ Log Daily Production Form":
    st.subheader("Daily Employee-wise Production Entry")
    
    conn = get_db_connection()
    employees = [row[0] for row in conn.execute("SELECT emp_name FROM employees").fetchall()]
    rolls_data = conn.execute("SELECT roll_name, labor_rate_per_roll, approx_weight_kg FROM roll_types").fetchall()
    
    rolls_dict = {}
    for r in rolls_data:
        v_name, v_rate, v_weight = r
        rolls_dict[str(v_name).strip()] = {
            "rate": float(v_rate),
            "weight": float(v_weight)
        }
    conn.close()
    
    if not employees or not rolls_dict:
        st.warning("⚠️ Kripya pehle '🛠️ Master Setup (Emp & Rates)' module me jaakar Employees aur Roll Variety settings add karein!")
    else:
        p_date = st.date_input("Production Ki Tareeh", value=datetime.now().date())
        emp_sel = st.selectbox("Kis Employee Ne Kaam Kiya?", employees, key="prod_emp_select")
        roll_sel = st.selectbox("Kaun sa Roll Banaya?", list(rolls_dict.keys()), key="prod_roll_select")
        qty = st.number_input("Kitne Rolls Banaye? (Quantity)", min_value=1, step=1, key="prod_qty_input")
        
        per_roll_rate = rolls_dict[str(roll_sel).strip()]["rate"]
        per_roll_weight = rolls_dict[str(roll_sel).strip()]["weight"]
        
        st.info(f"💡 Info: Is Roll ka Labor Rate ₹{per_roll_rate}/Roll hai. Worker Ka Total Paisa apne aap calculate hoga.")
        
        if st.button("🏗️ Production Entry Lock Karein", type="primary", use_container_width=True):
            total_earned = float(qty * per_roll_rate)
            total_w_calc = float(qty * per_roll_weight)
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO production_new (date, emp_name, roll_name, quantity_produced, labor_earned, total_weight_kg)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (str(p_date), str(emp_sel), str(roll_sel), qty, total_earned, total_w_calc))
            
            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls + ? WHERE roll_name = ?", (qty, str(roll_sel)))
            conn.commit()
            conn.close()
            st.success(f"✔️ Successful! {emp_sel} ne {qty} rolls banaye. khaate me ₹{total_earned} jud gaye.")
            st.rerun()

# --- PRODUCTION REPORTS (ANALYTICS WITH ADVANCED MODIFY CENTER) ---
elif menu == "📊 Production Reports (Analytics)":
    st.subheader("Production Analytics & Summary Dashboard")
    
    conn = get_db_connection()
    df_p = pd.read_sql_query("SELECT p_id as 'ID', date as 'Date', emp_name as 'Employee', roll_name as 'Roll Type', quantity_produced as 'Rolls Built', labor_earned as 'Labor Wages (₹)', total_weight_kg as 'Estimated Material Used (KG)' FROM production_new", conn)
    conn.close()
    
    if df_p.empty:
        st.info("Abhi tak koi production entry nahi ki gayi hai.")
    else:
        # 🔥 MONTH EXTRACTION LOGIC ATTACHED
        df_p['Month'] = pd.to_datetime(df_p['Date']).dt.strftime('%Y-%m')
        
        st.markdown("### 🔍 Search & Filter Control Panel")
        col_f1, col_f2, col_f3, col_f4 = st.columns(4) # 🔥 Split into 4 columns to fit Month
        
        with col_f1:
            unique_months = ["All Months"] + sorted(df_p['Month'].unique().tolist(), reverse=True)
            filter_month = st.selectbox("📅 Month Chunein (e.g., 2026-06)", unique_months)
            
        with col_f2:
            unique_dates = ["All Dates"] + sorted(df_p['Date'].unique().tolist(), reverse=True)
            filter_date = st.selectbox("📆 Date Chunein", unique_dates)
            
        with col_f3:
            unique_emps = ["All Employees"] + sorted(df_p['Employee'].unique().tolist())
            filter_emp = st.selectbox("👤 Employee Chunein", unique_emps)
            
        with col_f4:
            unique_rolls = ["All Rolls"] + sorted(df_p['Roll Type'].unique().tolist())
            filter_roll = st.selectbox("🛞 Roll Category Chunein", unique_rolls)
            
        df_filtered = df_p.copy()
        
        # 🔥 APPLY MONTH FILTER FIRST
        if filter_month != "All Months": 
            df_filtered = df_filtered[df_filtered['Month'] == filter_month]
        if filter_date != "All Dates": 
            df_filtered = df_filtered[df_filtered['Date'] == filter_date]
        if filter_emp != "All Employees": 
            df_filtered = df_filtered[df_filtered['Employee'] == filter_emp]
        if filter_roll != "All Rolls": 
            df_filtered = df_filtered[df_filtered['Roll Type'] == filter_roll]
            
        total_rolls_till_date = df_filtered['Rolls Built'].sum()
        total_wages_till_date = df_filtered['Labor Wages (₹)'].sum()
        
        st.markdown("---")
        kpi1, kpi2 = st.columns(2)
        kpi1.metric("📦 TOTAL PRODUCTION (FILTERED)", f"{total_rolls_till_date:,} Rolls")
        kpi2.metric("💰 WORKER WAGES PAYABLE (FILTERED)", f"₹{total_wages_till_date:,}")
        
        st.markdown("---")
        t1, t2, t3, t4 = st.tabs(["📅 Date-wise Production", "👤 Employee-wise Production", "📋 Full Detailed Ledger Data", "🛠️ Production Modify Center"])
        
        with t1:
            if not df_filtered.empty:
                df_date_wise = df_filtered.groupby('Date')[['Rolls Built', 'Labor Wages (₹)']].sum().reset_index()
                st.dataframe(df_date_wise, use_container_width=True)
            else: 
                st.write("No data available.")
                
        with t2:
            if not df_filtered.empty:
                df_emp_wise = df_filtered.groupby(['Employee', 'Roll Type'])[['Rolls Built', 'Labor Wages (₹)']].sum().reset_index()
                st.dataframe(df_emp_wise, use_container_width=True)
            else: 
                st.write("No data available.")
                
        with t3:
            st.dataframe(df_filtered.drop(columns=['ID', 'Month']), use_container_width=True)

# ======================================================================
# [PART_3_A_NEW_END]
# ======================================================================
# ======================================================================
# [PART_3_B_NEW_START] - Entry Modifications Gateway & Inventory Metrics
# ======================================================================

        # --- PRODUCTION ENTRY EDIT/MODIFY/DELETE TAB ---
        with t4:
            st.markdown("### 🛠️ Logged Worker Entry Modification System")
            conn = get_db_connection()
            all_entries = conn.execute("SELECT p_id, date, emp_name, roll_name, quantity_produced FROM production_new").fetchall()
            
            if not all_entries:
                st.info("Modify karne ke liye koi record nahi mila.")
            else:
                # 🔥 FIXED: Tuple elements ko sahi variable unpacker or index block (r[0], r[1]...) se map kiya hai
                entry_options = {
                    f"ID {r[0]} | Tarikh: {r[1]} | Worker: {r[2]} | {r[3]} ({int(r[4])} Roll)": r[0] 
                    for r in all_entries
                }
                selected_log_label = st.selectbox("Kaun si Entry Modify/Edit Karni Hai?", list(entry_options.keys()), key="select_prod_modify")
                selected_p_id = entry_options[selected_log_label]
                
                entry_meta = conn.execute("SELECT date, emp_name, roll_name, quantity_produced FROM production_new WHERE p_id=?", (selected_p_id,)).fetchone()
                
                if entry_meta:
                    curr_date, curr_emp, curr_roll, curr_qty = entry_meta
                    parsed_date = datetime.strptime(curr_date, "%Y-%m-%d").date() if curr_date else datetime.now().date()
                    
                    rolls_meta_data = conn.execute("SELECT labor_rate_per_roll, approx_weight_kg FROM roll_types WHERE roll_name=?", (curr_roll,)).fetchone()
                    item_rate = float(rolls_meta_data[0]) if rolls_meta_data else 0.0
                    item_weight = float(rolls_meta_data[1]) if rolls_meta_data else 0.0
                    
                    with st.form("modify_production_gate_form"):
                        st.markdown(f"#### Edit Entry Settings for ID Block: **{selected_p_id}**")
                        col_p_mod1, col_p_mod2 = st.columns(2)
                        
                        with col_p_mod1:
                            mod_p_date = st.date_input("Production Date", value=parsed_date)
                            mod_p_qty = st.number_input("Sahi Quantity (Rolls Count)", min_value=1, value=int(curr_qty), step=1)
                        with col_p_mod2:
                            st.text_input("Selected Worker Name", value=curr_emp, disabled=True)
                            st.text_input("Selected Roll Category", value=curr_roll, disabled=True)
                        
                        st.caption(f"💡 Info: Is variety ka rate ₹{item_rate}/roll hai. System wages automatic re-calculate kar dega.")
                        
                        col_p_btn1, col_p_btn2 = st.columns(2)
                        with col_p_btn1:
                            save_prod_changes = st.form_submit_button("💾 Save Updated Changes")
                        with col_p_btn2:
                            delete_prod_invoice = st.form_submit_button("🗑️ DELETE THIS ENTRY PERMANENTLY")
                            
                        if save_prod_changes:
                            cursor = conn.cursor()
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls - ? WHERE roll_name = ?", (float(curr_qty), str(curr_roll)))
                            
                            new_earned = float(mod_p_qty * item_rate)
                            new_w_calc = float(mod_p_qty * item_weight)
                            
                            cursor.execute("""
                                UPDATE production_new 
                                SET date=?, quantity_produced=?, labor_earned=?, total_weight_kg=? 
                                WHERE p_id=?
                            """, (str(mod_p_date), mod_p_qty, new_earned, new_w_calc, selected_p_id))
                            
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls + ? WHERE roll_name = ?", (float(mod_p_qty), str(curr_roll)))
                            conn.commit()
                            st.success("🎉 Worker production log entry details updated successfully!")
                            st.rerun()
                            
                        if delete_prod_invoice:
                            cursor = conn.cursor()
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls - ? WHERE roll_name = ?", (float(curr_qty), str(curr_roll)))
                            cursor.execute("DELETE FROM production_new WHERE p_id=?", (selected_p_id,))
                            conn.commit()
                            st.warning("🗑️ Worker log entry permanent database se hatayi gayi!")
                            st.rerun()
            conn.close()

        st.markdown("---")
        st.markdown("### 🗂️ Live Current Available Stock Summary (Net Production minus Net Sales)")
        
        conn = get_db_connection()
        master_varieties = [row[0] for row in conn.execute("SELECT roll_name FROM roll_types").fetchall()]
        prod_data = {row[0]: float(row[1]) for row in conn.execute("SELECT roll_name, SUM(quantity_produced) FROM production_new GROUP BY roll_name").fetchall()}
        sales_data = {row[0]: float(row[1]) for row in conn.execute("SELECT roll_name, SUM(quantity_sold) FROM sales_items GROUP BY roll_name").fetchall()}
        conn.close()
        
        filtered_varieties = [v for v in master_varieties if filter_roll == "All Rolls" or v == filter_roll]
        if filtered_varieties:
            box_cols = st.columns(len(filtered_varieties))
            for idx, r_name in enumerate(filtered_varieties):
                total_built = prod_data.get(r_name, 0.0)
                total_sold = sales_data.get(r_name, 0.0)
                live_available_stock = total_built - total_sold
                with box_cols[idx]:
                    st.metric(label=f"🛞 Live Stock: {r_name}", value=f"{int(live_available_stock)} Rolls", delta=f"Built: {int(total_built)} | Sold: {int(total_sold)}", delta_color="off")

# ======================================================================
# [PART_3_B_NEW_END]
# ======================================================================
# ======================================================================
# [PART_3_C_NEW_START] - Workers Personal Ledger, Month Filters & Tabs
# ======================================================================

# --- WORKERS HISAB-KITAB LEDGER ENGINE ---
elif menu == "👥 Workers Hisab-Kitab Ledger":
    st.subheader("👥 Workers Personal Kaam aur Jama-Udhaar Ledger")
    
    conn = get_db_connection()
    all_workers_tuples = conn.execute("SELECT emp_name FROM employees WHERE emp_name != 'PAPPU NISHAD'").fetchall()
    all_workers = [row[0] for row in all_workers_tuples]
    conn.close()
    
    if not all_workers:
        st.warning("⚠️ Kripya pehle Master Setup me jaakar Workers ke naam add karein!")
    else:
        col_w_sel1, col_w_sel2 = st.columns(2)
        with col_w_sel1:
            selected_worker = st.selectbox("👤 Kis Worker Ka Hisab Dekhna Hai?", all_workers)
        
        conn = get_db_connection()
        df_prod = pd.read_sql_query("SELECT date, roll_name, quantity_produced, labor_earned FROM production_new WHERE emp_name = ?", conn, params=(selected_worker,))
        df_pay = pd.read_sql_query("SELECT pay_id, date, amount_paid, payment_mode, remarks, given_by_supervisor FROM employee_payments WHERE emp_name = ?", conn, params=(selected_worker,))
        conn.close()
        
        if not df_prod.empty:
            df_prod['Month'] = pd.to_datetime(df_prod['date']).dt.strftime('%Y-%m')
        else:
            df_prod['Month'] = None
            
        if not df_pay.empty:
            df_pay['Month'] = pd.to_datetime(df_pay['date']).dt.strftime('%Y-%m')
        else:
            df_pay['Month'] = None
        
        all_months = sorted(list(set(
            (df_prod['Month'].dropna().tolist() if not df_prod.empty else []) + 
            (df_pay['Month'].dropna().tolist() if not df_pay.empty else [])
        )), reverse=True)
        
        with col_w_sel2:
            selected_month = st.selectbox("📅 Filter By Month", ["All Months"] + all_months)
            
        if selected_month != "All Months":
            if not df_prod.empty: 
                df_prod = df_prod[df_prod['Month'] == selected_month]
            if not df_pay.empty: 
                df_pay = df_pay[df_pay['Month'] == selected_month]
            
        total_wages_earned = df_prod['labor_earned'].sum() if not df_prod.empty else 0.0
        total_amount_paid = df_pay['amount_paid'].sum() if not df_pay.empty else 0.0
        net_balance_due = total_wages_earned - total_amount_paid
        
        st.markdown(f"### 📊 Live Summary ({selected_month}): {selected_worker}")
        kpi_w1, kpi_w2, kpi_w3 = st.columns(3)
        kpi_w1.metric("💰 Kul Kamai (Total Earned)", f"₹{total_wages_earned:,.2f}")
        kpi_w2.metric("💸 Kul Bhugtan / Deductions", f"₹{total_amount_paid:,.2f}")
        kpi_w3.metric("🔴 Outstanding Balance Due" if net_balance_due >= 0 else "🟢 Advance Balance", f"₹{abs(net_balance_due):,.2f}")
        
        st.markdown("---")
        t_hisab1, t_hisab2, t_hisab3, t_hisab4 = st.tabs(["🛞 Kaam Ka Breakdown", "💵 Diye Gaye Paise Ka Record", "➕ Direct Factory Se Payment/Deduction Entry", "🗑️ Entry Delete Center"])
        
        with t_hisab1:
            if df_prod.empty: 
                st.info("Is mahine koi production record nahi hai.")
            else:
                df_breakdown = df_prod.groupby('roll_name')[['quantity_produced', 'labor_earned']].sum().reset_index()
                df_breakdown.columns = ['Roll Type', 'Rolls Banaye', 'Labor Wages (₹)']
                st.dataframe(df_breakdown, use_container_width=True)
                st.markdown("**📋 Rozana Detailed List:**")
                st.dataframe(df_prod[['date', 'roll_name', 'quantity_produced', 'labor_earned']], use_container_width=True)
                
        with t_hisab2:
            if df_pay.empty: 
                st.info("Is mahine koi payment transaction nahi mila.")
            else:
                df_pay_display = df_pay.copy()
                df_pay_display['Source'] = df_pay_display['payment_mode'].apply(lambda x: "👑 Thekedar Commission Deduction" if x == "Thekedar Commission" else "🏭 Direct From Company")
                st.dataframe(df_pay_display[['date', 'amount_paid', 'payment_mode', 'Source', 'remarks']], use_container_width=True)
                
        with t_hisab3:
            with st.form("direct_worker_pay_form", clear_on_submit=True):
                p_date = st.date_input("Tarikh (Date)", value=datetime.now().date(), key="direct_w_pay_date")
                p_amt = st.number_input("Amount (₹)", min_value=1.0, step=100.0)
                p_mode = st.selectbox("Payment / Entry Type", ["Cash (Direct Factory)", "Online UPI", "Advance", "Thekedar Commission"])
                p_rem = st.text_input("Remarks / Detail (e.g., Pappu thekedar commission cut)")
                
                if st.form_submit_button("💾 Entry Lock Karein") and p_amt > 0:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    
                    # 1. Worker ke khaate me deduction chadhana
                    cursor.execute("""
                        INSERT INTO employee_payments (date, emp_name, amount_paid, payment_mode, remarks, given_by_supervisor) 
                        VALUES (?, ?, ?, ?, ?, 0)
                    """, (str(p_date), selected_worker, p_amt, p_mode, p_rem.strip()))
                    
                    # 2. 🔥 AGAR THEKEDAR COMMISSION HAI: Toh Pappu Nishad ki extra earning automatically insert ho jayegi
                    if p_mode == "Thekedar Commission":
                        commission_remark = f"Incentive/Commission from {selected_worker}: {p_rem.strip()}"
                        cursor.execute("""
                            INSERT INTO employee_payments (date, emp_name, amount_paid, payment_mode, remarks, given_by_supervisor) 
                            VALUES (?, 'PAPPU NISHAD', ?, 'Supervisor Commission Earning', ?, 0)
                        """, (str(p_date), p_amt, commission_remark))
                        
                    conn.commit()
                    conn.close()
                    st.success("Entry successfully mapped and locked!")
                    st.rerun()
                    
        with t_hisab4:
            if df_pay.empty: 
                st.info("Hataane ke liye koi transaction entry nahi hai.")
            else:
                with st.form("worker_pay_delete_gate_form", clear_on_submit=True):
                    delete_options = {f"ID: {r['pay_id']} | Date: {r['date']} | Amt: ₹{r['amount_paid']} | {r['remarks']}": r['pay_id'] for _, r in df_pay.iterrows()}
                    sel_pay_id = st.selectbox("Kaun si Entry Delete Karni Hai?", list(delete_options.keys()), key="del_worker_pay_box")
                    submit_delete = st.form_submit_button("❌ Selected Payment Permanently Delete Karein", type="primary", use_container_width=True)
                    
                    if submit_delete:
                        conn = get_db_connection()
                        cursor = conn.cursor()
                        # Main worker entry fetch karna remarks check karne ke liye
                        row_meta = cursor.execute("SELECT payment_mode, remarks, amount_paid FROM employee_payments WHERE pay_id = ?", (delete_options[sel_pay_id],)).fetchone()
                        
                        if row_meta and row_meta[0] == "Thekedar Commission":
                            # Agar worker se commission delete ho rahi hai, toh Pappu Nishad ke pass se bhi safety roll-back automatic ho jayega
                            opp_remark = f"Incentive/Commission from {selected_worker}: {row_meta[1]}"
                            cursor.execute("DELETE FROM employee_payments WHERE emp_name = 'PAPPU NISHAD' AND amount_paid = ? AND remarks = ?", (row_meta[2], opp_remark))
                            
                        cursor.execute("DELETE FROM employee_payments WHERE pay_id = ?", (delete_options[sel_pay_id],))
                        conn.commit()
                        conn.close()
                        st.warning("Entry hatayi gayi!")
                        st.rerun()

# ======================================================================
# [PART_3_C_NEW_END]
# ======================================================================
# ======================================================================
# [PART_3_D_NEW_START] - Supervisor Pappu Nishad Matrix Ledger & Action Desk
# ======================================================================

# --- SUPERVISOR (PAPPU NISHAD) SPECIAL MODULE ---
elif menu == "👑 Supervisor (Pappu Nishad)":
    st.subheader("👑 Supervisor Petty Cash & Commission Desk: Pappu Nishad")
    
    conn = get_db_connection()
    # 1. Company se jo cash mila ya external salary mili
    df_sup_received = pd.read_sql_query("SELECT pay_id, date, amount_paid, payment_mode as 'Mode', remarks FROM employee_payments WHERE emp_name = 'PAPPU NISHAD' AND payment_mode != 'Supervisor Commission Earning'", conn)
    # 2. 🔥 Workers se jo actual commission earning aayi (Suraj ya baki team se debit hoke)
    df_sup_earnings = pd.read_sql_query("SELECT pay_id, date, amount_paid, remarks FROM employee_payments WHERE emp_name = 'PAPPU NISHAD' AND payment_mode = 'Supervisor Commission Earning'", conn)
    # 3. Jo cash Pappu ne workers ko baanta
    df_sup_distributed = pd.read_sql_query("SELECT pay_id, date, emp_name, amount_paid, remarks FROM employee_payments WHERE given_by_supervisor = 1", conn)
    conn.close()
    
    if not df_sup_received.empty: df_sup_received['Month'] = pd.to_datetime(df_sup_received['date']).dt.strftime('%Y-%m')
    else: df_sup_received['Month'] = None
        
    if not df_sup_earnings.empty: df_sup_earnings['Month'] = pd.to_datetime(df_sup_earnings['date']).dt.strftime('%Y-%m')
    else: df_sup_earnings['Month'] = None
        
    if not df_sup_distributed.empty: df_sup_distributed['Month'] = pd.to_datetime(df_sup_distributed['date']).dt.strftime('%Y-%m')
    else: df_sup_distributed['Month'] = None
    
    sup_months = sorted(list(set(
        (df_sup_received['Month'].dropna().tolist() if not df_sup_received.empty else []) + 
        (df_sup_earnings['Month'].dropna().tolist() if not df_sup_earnings.empty else []) +
        (df_sup_distributed['Month'].dropna().tolist() if not df_sup_distributed.empty else [])
    )), reverse=True)
    
    col_s_f1, col_s_f2 = st.columns(2)
    with col_s_f1:
        s_month = st.selectbox("📅 Month Selector Desk", ["All Months"] + sup_months, key="sup_month_filter")
        
    if s_month != "All Months":
        if not df_sup_received.empty: df_sup_received = df_sup_received[df_sup_received['Month'] == s_month]
        if not df_sup_earnings.empty: df_sup_earnings = df_sup_earnings[df_sup_earnings['Month'] == s_month]
        if not df_sup_distributed.empty: df_sup_distributed = df_sup_distributed[df_sup_distributed['Month'] == s_month]
        
    total_received_from_company = df_sup_received['amount_paid'].sum() if not df_sup_received.empty else 0.0
    total_commission_wages = df_sup_earnings['amount_paid'].sum() if not df_sup_earnings.empty else 0.0
    total_paid_to_workers = df_sup_distributed['amount_paid'].sum() if not df_sup_distributed.empty else 0.0
    
    # Live Matrix Calculations
    pappu_net_earnings_total = total_received_from_company + total_commission_wages
    pappu_cash_in_hand = total_received_from_company - total_paid_to_workers
    
    st.markdown(f"### 📋 Cash & Commission Matrix Account ({s_month})")
    kpi_s1, kpi_s2, kpi_s3, kpi_s4 = st.columns(4)
    kpi_s1.metric("📥 Cash from Company", f"₹{total_received_from_company:,.2f}")
    kpi_s2.metric("📈 Total Commission Earned", f"₹{total_commission_wages:,.2f}")
    kpi_s3.metric("📤 Distributed to Team", f"₹{total_paid_to_workers:,.2f}")
    kpi_s4.metric("🟢 Cash Balance In Hand", f"₹{pappu_cash_in_hand:,.2f}")
        
    st.markdown("---")
    ts1, ts2, ts3, ts4, ts5 = st.tabs(["📥 Company Cash", "📈 Workers Commission Logs", "📤 Distributed Cash", "➕ Naye Len-Den Entry", "🗑️ Delete Room"])
    
    with ts1:
        st.markdown("#### 📂 Ledger: Company se mila cash")
        if df_sup_received.empty: st.info("Is timeframe koi cash receive nahi hua.")
        else: st.dataframe(df_sup_received[['date', 'amount_paid', 'Mode', 'remarks']], use_container_width=True)
        
    with ts2:
        st.markdown("#### 📈 Workers ke kaam se bani Pappu ki total earning list:")
        if df_sup_earnings.empty: st.info("Abhi tak koi commission earning record nahi hui.")
        else: st.dataframe(df_sup_earnings[['date', 'amount_paid', 'remarks']], use_container_width=True)
        
    with ts3:
        st.markdown("#### 👤 Employee-wise Distribution Breakdown Summary")
        if df_sup_distributed.empty: st.info("Workers ko abhi tak koi paisa nahi baanta gaya.")
        else:
            df_grouped_emp = df_sup_distributed.groupby('emp_name')['amount_paid'].sum().reset_index()
            df_grouped_emp.columns = ['Employee Name', 'Total Amount Given By Pappu (₹)']
            for _, row_emp in df_grouped_emp.iterrows():
                with st.expander(f"👉 {row_emp['Employee Name']} (Total Distributed: ₹{row_emp['Total Amount Given By Pappu (₹)']:,.2f})"):
                    df_individual_details = df_sup_distributed[df_sup_distributed['emp_name'] == row_emp['Employee Name']]
                    st.dataframe(df_individual_details[['date', 'amount_paid', 'remarks']], use_container_width=True)
                    
    with ts4:
        st.markdown("#### ➕ Add New Transaction Entry")
        sub_action_mode = st.radio("Kya Record Karna Hai?", ["1. Company Se Pappu Nishad Ko Cash Mila", "2. Pappu Nishad Ne Employee Ko Cash Diya"], horizontal=True, key="sup_desk_radio_action")
        
        if "1." in sub_action_mode:
            with st.form("sup_rec_form", clear_on_submit=True):
                r_date = st.date_input("Date", value=datetime.now().date(), key="r_d_sup")
                r_amt = st.number_input("Kitna Cash Mila? (₹)", min_value=1.0, step=500.0)
                r_rem = st.text_input("Voucher Details (e.g., Office safe se nikala)")
                if st.form_submit_button("🔒 Log Cash Received Entry"):
                    conn = get_db_connection()
                    conn.execute("INSERT INTO employee_payments (date, emp_name, amount_paid, payment_mode, remarks, given_by_supervisor) VALUES (?, 'PAPPU NISHAD', ?, 'Cash', ?, 0)", (str(r_date), r_amt, r_rem.strip()))
                    conn.commit()
                    conn.close()
                    st.success("Entry Saved!")
                    st.rerun()
        else:
            conn = get_db_connection()
            workers_list_for_sup = [r[0] for r in conn.execute("SELECT emp_name FROM employees WHERE emp_name != 'PAPPU NISHAD'").fetchall()]
            conn.close()
            with st.form("sup_dis_form", clear_on_submit=True):
                d_worker = st.selectbox("Kis Worker Ko Diya?", workers_list_for_sup)
                d_date = st.date_input("Date", value=datetime.now().date(), key="d_d_sup")
                d_amt = st.number_input("Kitna Amount Diya? (₹)", min_value=1.0, step=100.0)
                d_rem = st.text_input("Remarks (e.g., Hafte ka kharcha distributed)")
                if st.form_submit_button("🔒 Log Cash Distributed Entry"):
                    conn = get_db_connection()
                    conn.execute("INSERT INTO employee_payments (date, emp_name, amount_paid, payment_mode, remarks, given_by_supervisor) VALUES (?, ?, ?, 'Cash', ?, 1)", (str(d_date), d_worker, d_amt, d_rem.strip()))
                    conn.commit()
                    conn.close()
                    st.success("Worker distribution successfully saved!")
                    st.rerun()
                    
    with ts5:
        st.markdown("#### 🗑️ Master Delete Gate for Supervisor Workspace")
        del_selector_category = st.radio("Kaun si table se entry hatani hai?", ["Received Cash Ledger", "Distributed Cash Ledger"], horizontal=True, key="sup_del_category_radio")
        
        if del_selector_category == "Received Cash Ledger":
            if df_sup_received.empty: st.info("Receive ledger section me data khali hai.")
            else:
                with st.form("sup_rec_delete_form", clear_on_submit=True):
                    rec_del_map = {f"Date: {r['date']} | Amt: ₹{r['amount_paid']} | {r['remarks']}": r['pay_id'] for _, r in df_sup_received.iterrows()}
                    sel_rec_id = st.selectbox("Kaun si Receive Entry Delete Karni Hai?", list(rec_del_map.keys()), key="sel_rec_del_box")
                    submit_rec_del = st.form_submit_button("🗑️ Delete Selected Receive Entry", type="primary", use_container_width=True)
                    if submit_rec_del:
                        conn = get_db_connection()
                        conn.execute("DELETE FROM employee_payments WHERE pay_id = ?", (rec_del_map[sel_rec_id],))
                        conn.commit()
                        conn.close()
                        st.warning("Receive entry database se saaf!")
                        st.rerun()
                
        elif del_selector_category == "Distributed Cash Ledger":
            if df_sup_distributed.empty: st.info("Distribution ledger section me data khali hai.")
            else:
                with st.form("sup_dis_delete_form", clear_on_submit=True):
                    dis_del_map = {f"To: {r['emp_name']} | Date: {r['date']} | Amt: ₹{r['amount_paid']}": r['pay_id'] for _, r in df_sup_distributed.iterrows()}
                    sel_dis_id = st.selectbox("Kaun si Distribution Entry Delete Karni Hai?", list(dis_del_map.keys()), key="sel_dis_del_box")
                    submit_dis_del = st.form_submit_button("🗑️ Delete Selected Distribution Entry", type="primary", use_container_width=True)
                    if submit_dis_del:
                        conn = get_db_connection()
                        conn.execute("DELETE FROM employee_payments WHERE pay_id = ?", (dis_del_map[sel_dis_id],))
                        conn.commit()
                        conn.close()
                        st.warning("Distribution entry successfully rolled back!")
                        st.rerun()

# ======================================================================
# [PART_3_D_NEW_END]
# ======================================================================
# ======================================================================
# [PART_4_A_START] - Sales Entry Form with Auto Weight Deduction & Running Ledger
# ======================================================================

# --- SALES & WEIGHT DEDUCTION ---
elif menu == "🧾 Sales & Weight Deduction":
    st.subheader("Customer Bill Entry, Modification & Dynamic Stock Ledger")
    tab1, tab2, tab3 = st.tabs(["➕ Invoice Chadayein", "📋 Bills Record & Breakdown", "🛠️ Bill Modify / Delete Center"])
    
    conn = get_db_connection()
    roll_varieties = [(row[0], row[1]) for row in conn.execute("SELECT roll_name, current_stock_rolls FROM roll_types").fetchall()]
    
    # 🔥 EXTRACT DYNAMIC WIRE GAUGES FROM REPOSITORY
    cursor_g = conn.cursor()
    cursor_g.execute("SELECT DISTINCT gauge_name FROM raw_material")
    active_gauge_options_list = [r[0] for r in cursor_g.fetchall() if r and r[0]]
    if not active_gauge_options_list:
        active_gauge_options_list = ["24 Gauge", "25 Gauge", "26 Gauge", "27 Gauge"]
    conn.close()
    
    with tab1:
        with st.form("sales_new_form_multi"):
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                inv_no = st.text_input("Invoice Number (Unique Bill No)")
                party = st.text_input("Party Ka Naam")
                p_phone = st.text_input("Party Ka WhatsApp Number (e.g., 9876543210)")
                b_date = st.date_input("Bill Date")
            with col_b2:
                amt = st.number_input("Bill Value Amount (₹)", min_value=0.0, step=100.0)
                allowed_d = st.number_input("Credit Allowed Days", min_value=0, value=30)
                weight_sold = st.number_input("Bikri Ka Total Weight (KG - Wire Stock Se Minus Hoga)", min_value=0.0)
                
                # 🔥 NEW GAUGE SELECTION DROPDOWN
                target_deduction_gauge = st.selectbox("🎯 Select Wire Gauge for Material Deduction", options=active_gauge_options_list, key="sales_invoice_gauge_deduct_dropdown")
            
            st.markdown("---")
            st.markdown("### 📦 Inventory Items Dispatch")
            input_quantities = {}
            col_items = st.columns(len(roll_varieties) if len(roll_varieties) > 0 else 1)
            
            for idx, item in enumerate(roll_varieties):
                v_name, current_stk = item
                with col_items[idx % len(col_items)]:
                    input_quantities[v_name] = st.number_input(
                        f"🛞 {v_name} Qty (Stock: {int(current_stk)})", 
                        min_value=0, value=0, step=1, key=f"ins_qty_{v_name}"
                    )
            
            if st.form_submit_button("Full Bill & Stock Changes Lock Karein") and inv_no and party:
                conn = get_db_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO sales_new (invoice_no, party_name, bill_date, bill_amount, allowed_days, total_weight_sold_kg, party_phone) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                   (inv_no.strip(), party.strip(), str(b_date), amt, allowed_d, weight_sold, p_phone.strip()))
                    
                    for v_name, qty_to_deduct in input_quantities.items():
                        if qty_to_deduct > 0:
                            cursor.execute("INSERT INTO sales_items (invoice_no, roll_name, quantity_sold) VALUES (?, ?, ?)", (inv_no.strip(), v_name, qty_to_deduct))
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls - ? WHERE roll_name = ?", (qty_to_deduct, v_name))
                    
                    # 🔥 AUTOMATED REAL TIME WEIGHT DEDUCTION PIPELINE
                    if weight_sold > 0.0:
                        current_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        current_date_stamp = datetime.now().strftime("%Y-%m-%d")
                        
                        # 1. Deduct exact material amount from wire stock
                        cursor.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg - ? WHERE gauge_name = ?", (float(weight_sold), target_deduction_gauge))
                        
                        # 2. Log trace inside sales register
                        cursor.execute("""
                            INSERT INTO wire_sales_logs (date_logged, invoice_no, party_name, gauge_size, weight_deducted_kg, timestamp) 
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (current_date_stamp, inv_no.strip(), party.strip(), target_deduction_gauge, float(weight_sold), current_time_stamp))
                    
                    conn.commit()
                    st.success(f"🎉 Bill No {inv_no} save ho gaya aur Raw Stock minus ho gaya!")
                except sqlite3.IntegrityError: st.error("❌ Unique Bill Number Already Exists!")
                conn.close()
                st.rerun()

    with tab2:
        conn = get_db_connection()
        df_s = pd.read_sql_query("SELECT invoice_no as 'Bill No', party_name as 'Party Name', party_phone as 'Phone Number', bill_date as 'Date', bill_amount as 'Amount (₹)', allowed_days as 'Allowed Days', total_weight_sold_kg as 'Weight Dispatched (KG)', payment_status as 'Status' FROM sales_new", conn)
        if not df_s.empty:
            st.markdown("### 📋 All Invoices Ledger Summary")
            st.dataframe(df_s, use_container_width=True, hide_index=True)
            st.markdown("---")
            bill_options = ["All Bills Data"] + df_s['Bill No'].tolist()
            selected_bill_look = st.selectbox("Kis Particular Bill Ke Details Dekhne Hain?", bill_options)
            if selected_bill_look == "All Bills Data":
                df_breakdown = pd.read_sql_query("SELECT invoice_no as 'Bill No', roll_name as 'Roll Type', quantity_sold as 'Sold Quantity' FROM sales_items", conn)
            else:
                df_breakdown = pd.read_sql_query("SELECT invoice_no as 'Bill No', roll_name as 'Roll Type', quantity_sold as 'Sold Quantity' FROM sales_items WHERE invoice_no = ?", conn, params=(selected_bill_look,))
            st.dataframe(df_breakdown, use_container_width=True, hide_index=True)
        else: st.info("Khaate me koi bill nahi mila.")
        conn.close()

    # 🔥 NEW LIVE INTERFACE LAYER: Date-wise dynamic combined Aaya/Gaya Ledger Book
    st.write("---")
    st.markdown("### 📜 Date-Wise Comprehensive Steel Wire Stock Movements Ledger (Aaya/Gaya)")
    conn_ledger = get_db_connection()
    try:
        df_in_raw = pd.read_sql_query("SELECT date_logged, gauge_size, weight_added_kg, 'INWARD (Maal Aaya)' AS 'Movement Type', timestamp FROM wire_inward_logs", conn_ledger)
        df_in_raw.columns = ['Date', 'Gauge Size', 'Weight (KG)', 'Movement Type', 'System Log Time']
    except Exception:
        df_in_raw = pd.DataFrame(columns=['Date', 'Gauge Size', 'Weight (KG)', 'Movement Type', 'System Log Time'])
        
    try:
        df_out_raw = pd.read_sql_query("SELECT date_logged, gauge_size, (-1 * weight_deducted_kg) AS 'Weight (KG)', f'OUTWARD (Sales Bill: ' || invoice_no || ' - ' || party_name || ')' AS 'Movement Type', timestamp FROM wire_sales_logs", conn_ledger)
        df_out_raw.columns = ['Date', 'Gauge Size', 'Weight (KG)', 'Movement Type', 'System Log Time']
    except Exception:
        df_out_raw = pd.DataFrame(columns=['Date', 'Gauge Size', 'Weight (KG)', 'Movement Type', 'System Log Time'])
    conn_ledger.close()
    
    df_consolidated_movement_ledger = pd.concat([df_in_raw, df_out_raw], ignore_index=True)
    if not df_consolidated_movement_ledger.empty:
        df_consolidated_movement_ledger = df_consolidated_movement_ledger.sort_values(by='System Log Time', ascending=False)
        st.dataframe(df_consolidated_movement_ledger.style.format({"Weight (KG)": "{:+,.2f}"}), use_container_width=True, hide_index=True)
    else:
        st.caption("ℹ️ No material stock logs recorded yet.")

# ======================================================================
# [PART_4_A_END]
# ======================================================================
# ==========================================
# [PART_4_B1_START] - Bill Modification Engine With Dynamic Raw Stock Reversal & Log Mapping
# ==========================================
    with tab3:
        st.markdown("### 🛠️ Bill Edit or Permanent Delete System")
        conn = get_db_connection()
        all_bills = [row[0] for row in conn.execute("SELECT invoice_no FROM sales_new").fetchall()]
        if not all_bills: st.info("No saved invoices found.")
        else:
            clean_bill_options = [str(b) for b in all_bills]
            select_modify_bill = st.selectbox("Kaun Sa Bill Edit / Modify Karna Hai?", clean_bill_options)
            
            bill_meta = conn.execute("SELECT party_name, bill_date, bill_amount, allowed_days, total_weight_sold_kg, payment_status, party_phone FROM sales_new WHERE invoice_no=?", (str(select_modify_bill),)).fetchone()
            
            # 🔥 CORRECT UNPACKING: Tuple elements ko clear index se fetch kiya taaki data parsing completely accurate ho
            purane_sold_items = {r[0]: r[1] for r in conn.execute("SELECT roll_name, quantity_sold FROM sales_items WHERE invoice_no=?", (str(select_modify_bill),)).fetchall()}
            available_master_rolls = [r[0] for r in conn.execute("SELECT roll_name FROM roll_types").fetchall()]
            
            cursor_g = conn.cursor()
            cursor_g.execute("SELECT DISTINCT gauge_name FROM raw_material")
            active_gauge_options_list = [r[0] for r in cursor_g.fetchall() if r and r[0]]
            if not active_gauge_options_list:
                active_gauge_options_list = ["24 Gauge", "25 Gauge", "26 Gauge", "27 Gauge"]
                
            if bill_meta:
                p_name_curr, b_date_curr, amt_curr, allow_curr, weight_curr, status_curr, phone_curr = bill_meta
                b_date_parsed = datetime.strptime(b_date_curr, "%Y-%m-%d").date() if b_date_curr else datetime.now().date()
                
                row_log_meta = conn.execute("SELECT gauge_size FROM wire_sales_logs WHERE invoice_no = ?", (str(select_modify_bill),)).fetchone()
                default_gauge_idx = 0
                if row_log_meta and str(row_log_meta[0]) in active_gauge_options_list:
                    default_gauge_idx = active_gauge_options_list.index(str(row_log_meta[0]))
                
                with st.form("modify_form_gate_with_rolls"):
                    col_m1, col_m2 = st.columns(2)
                    with col_m1:
                        m_party = st.text_input("Party Name", value=p_name_curr)
                        m_phone = st.text_input("Party Phone", value=phone_curr if phone_curr else "")
                        m_date = st.date_input("Bill Date", value=b_date_parsed)
                        m_status = st.selectbox("Payment Status", ["Pending", "Paid"], index=0 if status_curr == "Pending" else 1)
                    with col_m2:
                        m_amt = st.number_input("Bill Amount (₹)", min_value=0.0, value=float(amt_curr))
                        m_allow = st.number_input("Allowed Days", min_value=0, value=int(allow_curr))
                        m_weight = st.number_input("Total Weight (KG)", min_value=0.0, value=float(weight_curr))
                        mod_target_gauge = st.selectbox("🎯 Target Gauge for Stock Reversal / Update", options=active_gauge_options_list, index=default_gauge_idx)
                    
                    modify_quantities = {}
                    col_mod_items = st.columns(len(available_master_rolls) if len(available_master_rolls) > 0 else 1)
                    for idx, r_name in enumerate(available_master_rolls):
                        default_qty = int(purane_sold_items.get(r_name, 0))
                        with col_mod_items[idx % len(col_mod_items)]:
                            # 🔥 STREAMLIT CACHE FIX: key ke sath invoice_no laga diya taaki dropdown badalne par quantity automatic sahi load ho
                            modify_quantities[r_name] = st.number_input(f"🛞 {r_name} Qty", min_value=0, value=default_qty, step=1, key=f"edit_qty_{str(select_modify_bill)}_{r_name}")
                    
                    save_changes = st.form_submit_button("💾 Save Updated Changes")
                    delete_invoice = st.form_submit_button("🗑️ DELETE THIS INVOICE PERMANENTLY")
                    
                    if save_changes:
                        cursor = conn.cursor()
                        for roll_type, old_qty in purane_sold_items.items():
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls + ? WHERE roll_name = ?", (int(old_qty), roll_type))
                        
                        # 🔥 RESTORE WIRE WEIGHT BEFORE NEW ENTRY
                        if float(weight_curr) > 0.0:
                            cursor.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg + ? WHERE gauge_name = ?", (float(weight_curr), mod_target_gauge))
                        
                        cursor.execute("UPDATE sales_new SET party_name=?, bill_date=?, bill_amount=?, allowed_days=?, total_weight_sold_kg=?, payment_status=?, party_phone=? WHERE invoice_no=?", (m_party.strip(), str(m_date), m_amt, m_allow, m_weight, m_status, m_phone.strip(), str(select_modify_bill)))
                        cursor.execute("DELETE FROM sales_items WHERE invoice_no=?", (str(select_modify_bill),))
                        
                        for roll_type, new_qty in modify_quantities.items():
                            if new_qty > 0:
                                cursor.execute("INSERT INTO sales_items (invoice_no, roll_name, quantity_sold) VALUES (?, ?, ?)", (str(select_modify_bill), roll_type, int(new_qty)))
                                cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls - ? WHERE roll_name = ?", (int(new_qty), roll_type))

                        # 🔥 DEDUCT NEW WEIGHT & FRESH LOG
                        if float(m_weight) > 0.0:
                            current_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            current_date_stamp = datetime.now().strftime("%Y-%m-%d")
                            cursor.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg - ? WHERE gauge_name = ?", (float(m_weight), mod_target_gauge))
                            cursor.execute("DELETE FROM wire_sales_logs WHERE invoice_no = ?", (str(select_modify_bill),))
                            cursor.execute("""
                                INSERT INTO wire_sales_logs (date_logged, invoice_no, party_name, gauge_size, weight_deducted_kg, timestamp) 
                                VALUES (?, ?, ?, ?, ?, ?)
                            """, (current_date_stamp, str(select_modify_bill), m_party.strip(), mod_target_gauge, float(m_weight), current_time_stamp))
                        else:
                            cursor.execute("DELETE FROM wire_sales_logs WHERE invoice_no = ?", (str(select_modify_bill),))
                            
                        conn.commit()
                        st.success("✔️ Successfully updated invoice parameters and wire stock balances!")
                        st.rerun()
                        
                    if delete_invoice:
                        cursor = conn.cursor()
                        for roll_type, old_qty in purane_sold_items.items():
                            cursor.execute("UPDATE roll_types SET current_stock_rolls = current_stock_rolls + ? WHERE roll_name = ?", (int(old_qty), roll_type))
                        
                        # 🔥 FULL ROLLBACK WIRE RESTORATION ON PERMANENT DELETE
                        if float(weight_curr) > 0.0:
                            cursor.execute("UPDATE raw_material SET current_stock_kg = current_stock_kg + ? WHERE gauge_name = ?", (float(weight_curr), mod_target_gauge))
                        
                        cursor.execute("DELETE FROM sales_items WHERE invoice_no=?", (str(select_modify_bill),))
                        cursor.execute("DELETE FROM sales_new WHERE invoice_no=?", (str(select_modify_bill),))
                        cursor.execute("DELETE FROM wire_sales_logs WHERE invoice_no = ?", (str(select_modify_bill),))
                        
                        conn.commit()
                        st.warning("❌ Invoice Deleted permanently! Raw wire weight credited back.")
                        st.rerun()
        conn.close()
# ==========================================
# [PART_4_B1_END]
# ==========================================
# ======================================================================
# [PART_4_B2_START] - Dashboard & Professional Outstanding English WhatsApp Alert Engine
# ==========================================
elif menu == "🚨 Dashboard & Payment Alerts":
    st.subheader("🚨 Live Payment Outstanding Overdue Alerts")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT invoice_no, party_name, bill_date, bill_amount, allowed_days, party_phone FROM sales_new WHERE payment_status = 'Pending'")
    pending_bills = cursor.fetchall()
    conn_close_fixed = conn.close()
    
    current_date = datetime.now().date()
    alert_count = 0
    if pending_bills:
        for bill in pending_bills:
            inv, party, b_date_str, amount, allowed_days, phone = bill
            bill_date = datetime.strptime(b_date_str, "%Y-%m-%d").date()
            days_passed = (current_date - bill_date).days
            if days_passed > allowed_days:
                alert_count += 1
                overdue_days = days_passed - allowed_days
                
                # 🔥 UPGRADED FORMAL ENGLISH WHATSAPP TEMPLATE ENGINE (COMPACT WRAPPED)
                raw_msg = (
                    f"Dear {party},\n\n"
                    f"This is a formal reminder regarding your outstanding "
                    f"Invoice No: {inv}. An amount of Rs. {amount:,.2f} "
                    f"is currently overdue by {overdue_days} day(s).\n\n"
                    f"We kindly request you to clear the outstanding dues "
                    f"at your earliest convenience. If the payment has already "
                    f"been processed, please ignore this message.\n\n"
                    f"Regards,\n"
                    f"Mannat Wealth / Factory ERP"
                )
                
                # Safe operational string string replacements to handle spaces cleanly
                encoded_msg = raw_msg.replace("\n", "%0A").replace(" ", "%20")
                
                clean_phone = str(phone).strip()
                if clean_phone and not clean_phone.startswith("91") and len(clean_phone) == 10:
                    clean_phone = "91" + clean_phone
                
                whatsapp_desktop_url = f"whatsapp://send?phone={clean_phone}&text={encoded_msg}"
                
                st.error(f"🔴 **ALERT:** Party Name: **{party}** (Bill: {inv}) | Overdue by **{overdue_days} day(s)** | Amount: **₹{amount:,}**")
                if phone:
                    st.markdown(f"👉 [💬 Open in WhatsApp Desktop App for {party}]({whatsapp_desktop_url})")
                else:
                    st.caption(f"⚠️ Note: {party} ka phone number billing section me chada nahi mila, kripya edit tab me phone jodein.")
                    
        if alert_count == 0: st.success("👍 Sabhi pending bills credit limit ke andar hain!")
    else: st.info("Khaate me koi pending bill nahi hai.")
# ======================================================================
# [PART_4_B2_END]
# ======================================================================
# =====================================================================
# 💾 DATABASE BACKUP LAYER (SAVE TO MEMORY AT THE END OF RUN)
# =====================================================================
if os.path.exists(FACTORY_DB_NAME):
    with open(FACTORY_DB_NAME, "rb") as f_src:
        st.session_state["persistent_factory_db_buffer"] = f_src.read()

