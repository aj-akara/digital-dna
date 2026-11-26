import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title='Digital DNA | Python Experience Lab', page_icon='🧬', layout='centered')
st.markdown('''<style>
.stApp {background: #0d1728; color: #e8f0ff;}
[data-testid="stHeader"] {background: transparent;}
.stApp h1,.stApp h2,.stApp h3,.stApp p,.stApp label {color:#e8f0ff;}
.hero {background:linear-gradient(120deg,#173b59,#37306d);padding:28px;border-radius:24px;border:1px solid #537da8;margin-bottom:20px;}
.hero h1 {font-size:2.4rem;margin:8px 0;line-height:1.15;}
.hero small {color:#8ce7ef;letter-spacing:2px;}
.result {background:linear-gradient(120deg,#164b58,#243269);padding:24px;border-radius:20px;margin:12px 0;}
.stButton button,.stFormSubmitButton button {border-radius:12px;min-height:48px;font-weight:700;}
</style>''', unsafe_allow_html=True)
roles = ['Data Analyst','Digital Creator','AI & Technology Developer','Information Specialist']
icons = ['📊','🎨','🤖','🔎']
profiles = [
 ('นักวิเคราะห์ข้อมูล','คุณสนใจการค้นหารูปแบบและใช้ข้อมูลเพื่อประกอบการตัดสินใจ','Python, Data Visualization, Statistics','Data Analyst, Business Intelligence Analyst'),
 ('นักสร้างสรรค์ดิจิทัล','คุณสนใจการออกแบบ การสื่อสาร และสร้างประสบการณ์ดิจิทัล','Digital Design, Creative Coding, UX/UI','Digital Content Creator, UX Designer'),
 ('นักพัฒนาเทคโนโลยี','คุณสนใจการแก้ปัญหาด้วยเทคโนโลยีและการสร้างเครื่องมือใหม่','Python, AI, Automation','Application Developer, AI Specialist'),
 ('นักจัดการสารสนเทศ','คุณสนใจการค้นคว้า ตรวจสอบ และจัดระบบข้อมูลให้เข้าถึงง่าย','Metadata, Search Systems, Information Management','Information Specialist, Digital Archivist')]
questions = [
 ('กิจกรรมใดที่คุณสนใจมากที่สุด?', ['ค้นหารูปแบบจากข้อมูล','ออกแบบสื่อให้โดดเด่น','ทดลองสร้างโปรแกรม','ค้นคว้าและจัดระเบียบข้อมูล']),
 ('เมื่อทำงานกลุ่ม คุณอยากรับหน้าที่ใด?', ['วิเคราะห์ผลและตัวเลข','ออกแบบสไลด์และการนำเสนอ','สร้างเครื่องมือช่วยทีม','รวบรวมและตรวจสอบแหล่งข้อมูล']),
 ('หากมีข้อมูลจำนวนมาก คุณอยากทำอะไร?', ['หาข้อสรุปจากข้อมูล','สร้างภาพเล่าเรื่องจากข้อมูล','เขียนโปรแกรมจัดการอัตโนมัติ','จัดหมวดหมู่เพื่อให้ค้นหาได้ง่าย']),
 ('แอปพลิเคชันใดที่คุณอยากสร้าง?', ['ระบบวิเคราะห์คะแนน','เครื่องมือสร้างโปสเตอร์','ผู้ช่วย AI','ระบบค้นหาหนังสือหรือเอกสาร']),
 ('คุณรู้สึกสนุกที่สุดเมื่อใด?', ['ค้นพบแนวโน้มที่ซ่อนอยู่','สร้างผลงานที่สวยงาม','แก้ปัญหาทางเทคนิคสำเร็จ','ค้นพบข้อมูลที่ถูกต้องและน่าเชื่อถือ']),
 ('ทักษะใดที่อยากเรียนรู้เพิ่มเติม?', ['การวิเคราะห์ข้อมูล','การออกแบบดิจิทัล','การเขียนโปรแกรมและ AI','การจัดการสารสนเทศ']),
 ('ถ้ามีเวลาหนึ่งวันสำหรับโปรเจกต์ คุณจะเลือกอะไร?', ['วิเคราะห์ข้อมูลการใช้ชีวิต','สร้างสื่อประชาสัมพันธ์','สร้างระบบทำงานอัตโนมัติ','สร้างคลังความรู้ดิจิทัล']),
 ('คุณอยากให้เทคโนโลยีช่วยเรื่องใดมากที่สุด?', ['ตัดสินใจจากข้อมูล','สื่อสารความคิดอย่างสร้างสรรค์','ลดงานซ้ำซ้อน','เข้าถึงความรู้ที่ต้องการ']),
 ('ผลงานใดที่คุณภูมิใจนำเสนอ?', ['แดชบอร์ดที่ให้ข้อค้นพบใหม่','เว็บไซต์ที่มีดีไซน์โดดเด่น','แอปที่แก้ปัญหาได้จริง','ระบบสารสนเทศที่ใช้งานสะดวก']),
 ('งานในอนาคตแบบใดที่ดึงดูดคุณ?', ['วิเคราะห์ข้อมูลเพื่อวางแผน','ผลิตสื่อและประสบการณ์ดิจิทัล','พัฒนาโปรแกรมและเทคโนโลยี','จัดการและให้บริการความรู้'])]

if 'orders' not in st.session_state:
    rng = random.Random()
    st.session_state.orders = [rng.sample(range(4),4) for _ in questions]

st.markdown('''<div class="hero"><small>PYTHON EXPERIENCE LAB · 01</small><h1>🧬 Discover Your<br>Digital DNA</h1><p>ค้นหาตัวตนของคุณในโลกดิจิทัล ผ่านคำถาม 10 ข้อ</p><p>Programming in Information Work</p></div>''', unsafe_allow_html=True)
st.caption('ใช้เวลาประมาณ 2–3 นาที • ไม่ต้องเข้าสู่ระบบ • ไม่มีคำตอบถูกหรือผิด')
with st.form('quiz'):
    nickname = st.text_input('ชื่อเล่น (ไม่บังคับ)', max_chars=40)
    answers = []
    for i,(question,options) in enumerate(questions):
        answers.append(st.radio(f'{i+1}. {question}', st.session_state.orders[i], format_func=lambda j, opts=options: opts[j], index=None, key=f'q{i}'))
    submitted = st.form_submit_button('✨ Analyze My Digital DNA', type='primary', use_container_width=True)

if submitted:
    if any(a is None for a in answers):
        st.warning('กรุณาตอบคำถามให้ครบทั้ง 10 ข้อ')
        st.session_state.pop('result', None)
    else:
        scores = [answers.count(i) * 10 for i in range(4)]
        st.session_state.result = (nickname.strip() or 'คุณ', scores)
        st.balloons()

if 'result' in st.session_state:
    name,scores = st.session_state.result
    winners = [i for i,s in enumerate(scores) if s == max(scores)]
    st.divider()
    st.subheader('YOUR DIGITAL PROFILE')
    st.write(f'ผลการสำรวจความสนใจของ {name}')
    report = [f'DIGITAL DNA — {name}']
    for i in winners:
        st.markdown(f'### {icons[i]} {roles[i]}')
        thai,desc,skills,careers = profiles[i]
        st.success(f'{thai} — {desc}')
        st.write(f'**ทักษะที่น่าสนใจ:** {skills}')
        st.write(f'**ตัวอย่างอาชีพ:** {careers}')
        report.extend([roles[i],thai,desc,f'ทักษะ: {skills}',f'อาชีพ: {careers}'])
    if len(winners)>1:
        st.info('คุณมีความสนใจเด่นหลายด้านที่ได้คะแนนเท่ากัน')
    fig = go.Figure(go.Scatterpolar(r=scores+[scores[0]],theta=['Data','Creativity','Technology','Information','Data'],fill='toself',line=dict(color='#63e6e2',width=3),fillcolor='rgba(99,230,226,0.28)'))
    fig.update_layout(polar=dict(bgcolor='#18263c',radialaxis=dict(visible=True,range=[0,100],tickvals=[0,25,50,75,100],gridcolor='#51647c',tickfont=dict(color='#c1cde0')),angularaxis=dict(tickfont=dict(color='#e8f0ff'),gridcolor='#51647c')),paper_bgcolor='#0d1728',font=dict(color='#e8f0ff'),margin=dict(l=55,r=55,t=25,b=25),height=340,showlegend=False)
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
    for i,role in enumerate(roles):
        st.write(f'{icons[i]} {role} — {scores[i]}%')
        st.progress(scores[i]/100)
        report.append(f'{role}: {scores[i]}%')
    note = 'ผลเป็นสัดส่วนคำตอบที่เลือกแต่ละด้าน ไม่ใช่ระดับความสามารถหรือแบบประเมินบุคลิกภาพมาตรฐาน'
    st.caption(note)
    report.append(note)
    st.download_button('📥 บันทึกผลของฉัน', '\n'.join(report).encode('utf-8-sig'), file_name='my_digital_dna.txt', mime='text/plain', use_container_width=True)
    with st.expander('🔓 Reveal the Python behind this app'):
        st.write('Input: คำตอบ 10 ข้อ → Process: นับและเปรียบเทียบคะแนน → Output: บทบาทและกราฟ')
        st.code('scores = [answers.count(i) * 10 for i in range(4)]\nwinners = [i for i, s in enumerate(scores)\n           if s == max(scores)]',language='python')
    st.markdown('### Powered by Python — Your Journey Starts Here.')
st.caption('กิจกรรมเพื่อการเรียนรู้ • ไม่ส่งคำตอบไปยังฐานข้อมูลหรือ API ภายนอก')
