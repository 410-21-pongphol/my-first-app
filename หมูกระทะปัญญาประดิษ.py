import streamlit as st

st.title("🥩 แอปพลิเคชั่นคำนวณราคาร้านหมูกระทะกินเอาตาย")

people = st.number_input("กรอกจำนวนลูกค้า (ท่าน):", min_value=0, value=1, step=1)

price_per_person = 299

price_per_person = 499

price_per_person = 219

price_per_person = 219

price_per_person = 219

total_price = people * price_per_person

discount = total_price * 0.10

net_price = total_price - discount

st.header(f"• ราคารวม ({price_per_person} บาท/ท่าน): **{total_price:.2f}** บาท")
st.header(f"• ส่วนลดพิเศษ (10%): **{discount:.2f}** บาท")
st.header(f"• ราคาสุทธิ: **{net_price:.2f}** บาท")

st.divider()

st.write("นายสมชาย ใจดี เลขที่ 1 ม.4/1")
