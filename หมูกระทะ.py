import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 15%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.15
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 15%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นายปองพล เปาวะนานนท์ เลขที่ 21  ม.4/10")
