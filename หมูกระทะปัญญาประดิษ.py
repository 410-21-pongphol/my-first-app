import streamlit as st

st.title("🥩 แอปพลิเคชั่นคำนวณราคาร้านหมูกระทะกินเอาตาย")

st.subheader("🛒 เลือกรายการอาหารและจำนวน")

set_eim = st.number_input("1. เซ็ตกินเอาอิ่ม (299 ฿):", min_value=0, value=0, step=1)
set_juk = st.number_input("2. เซ็ตกินเอาจุก (499 ฿):", min_value=0, value=0, step=1)
set_tai = st.number_input("3. เซ็ตกินเอาตาย (699 ฿):", min_value=0, value=0, step=1)
set_classic = st.number_input("4. เซ็ตบุฟเฟต์ Classic (169 ฿/ท่าน):", min_value=0, value=0, step=1)
set_premium = st.number_input("5. เซ็ตบุฟเฟต์ Premium (239 ฿/ท่าน):", min_value=0, value=0, step=1)

people_count = st.number_input("👥 จำนวนลูกค้าที่มาทาน (คน):", min_value=1, value=1, step=1)

total_price = (set_eim * 299) + (set_juk * 499) + (set_tai * 699) + (set_classic * 169) + (set_premium * 239)

if people_count >= 6:
    discount = 67.0
    discount_msg = "ได้รับส่วนลดพิเศษกลุ่มใหญ่ (มา 6 คนขึ้นไป)"
else:
    discount = 0.0
    discount_msg = "ไม่เข้าเงื่อนไขส่วนลด (ต้องมา 6 คนขึ้นไป)"

net_price = total_price - discount
if net_price < 0:
    net_price = 0.0

st.divider()

st.subheader("📊 สรุปยอดชำระเงิน")
st.header(f"• ราคารวมทั้งหมด: **{total_price:,.2f}** บาท")
st.write(f"📌 *{discount_msg}*")
st.header(f"• ส่วนลด: **-{discount:,.2f}** บาท")
st.header(f"• ราคาสุทธิที่ต้องชำระ: **{net_price:,.2f}** บาท")

st.divider()

st.write("👨‍💻 **กลุ่มที่ 4 - ใบงานที่ 2.3**")
st.write("1. ปองพล เปาวะนานนท์ เลขที่ 21 (หัวหน้ากลุ่ม)")
st.write("2. จิรัฏฐานันดร์ ธรรมสุ เลขที่ 10")
st.write("3. วัชรพงษ์ พลอยประเสริฐศรี เลขที่ 13")
