import streamlit as st

st.title('性格分析アプリ')

st.write("""
##### 10の質問に対し直感でお答えください。

###### 0:まったくあてはまらない, 1:ややあてはまらない, 2:どちらとも言えない, 3:まあまあ当てはまる, 4:完全にあてはまる
###### この5段階で点数をつけてください。
######
""")


# ------------ function ------------------
def point_to_num(point):
     if point == '0:まったくあてはまらない':
          a = 0
     elif point == '1:ややあてはまらない':
          a = 1
     elif point == '2:どちらとも言えない':
          a = 2
     elif point == '3:まあまあ当てはまる':
          a = 3
     elif point == '4:完全にあてはまる':
          a = 4
     return a
# ----------------------------------------

st.write('質問１')
point = st.select_slider(
     '私は、初めての人に会うのが好きで、会話をするのが好きで、人と会うのを楽しめる人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )
## st.write('You selected wavelengths between', start_color, 'and', end_color)

a1 = point_to_num(point)
# st.write(a1)
st.info(f'回答：{a1}')


st.write('質問２')
point = st.select_slider(
     '私は、人に対して思いやりがあり、その思いやりを行動に移し、他人を差別しない人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a2 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a2}')


###############################

st.write('質問３')
point = st.select_slider(
     '私は、きっちりと物事をこなし、手際よく行動し、適切に物事を行おうとする人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a3 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a3}')


st.write('質問４')
point = st.select_slider(
     '私は、いつも心配事が多く、不安になりやすく、気分の浮き沈みが多い人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a4 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a4}')


st.write('質問５')
point = st.select_slider(
     '私は、知的な活動が得意で、創造性が高くて好奇心があり、新たなことを探求する人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a5 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a5}')


st.write('質問６')
point = st.select_slider(
     '私は、恥ずかしがり屋で、物静かで、人が多いパーティなどは苦手な人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a6 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a6}')


st.write('質問７')
point = st.select_slider(
     '私は、すぐ思ったことを口にし、冷淡な面があり、他人に同情を感じることはめったにない人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a7 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a7}')


st.write('質問８')
point = st.select_slider(
     '私は、あまり考えずに行動し、さほどきっちりは行動せず、ギリギリまで物事に手を付けない人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a8 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a8}')


st.write('質問９')
point = st.select_slider(
     '私は、たいていリラックスしており、落ち着きがあり、めったに問題について悩まない人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a9 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a9}')


st.write('質問１０')
point = st.select_slider(
     '私は、物事を現実的に考え、伝統的な考え方を好み、めったに空想などで時間を浪費しない人間だ。',
     options=['0:まったくあてはまらない', '1:ややあてはまらない', '2:どちらとも言えない', '3:まあまあ当てはまる', '4:完全にあてはまる'],
     value=('2:どちらとも言えない')
     )

a10 = point_to_num(point)
# st.write(a2)
st.info(f'回答：{a10}')


extraversion = a1 + (4 - a6)
agreeableness = a2 + (4 - a7)
conscientiousness = a3 + (4 - a8)
neuroticism = a4 + (4 - a9)
openness = a5 + (4 - a10)

st.markdown("---") #区切り線
## if st.button('診断を開始する'):


# ============================================
# レーダーチャート ▶︎
# 空のGraph Objectsを作成
# ============================================
import plotly.express as px
import pandas as pd

data = [
     {"label": "外向性", "value": extraversion},
     {"label": "協調性", "value": agreeableness},
     {"label": "誠実性", "value": conscientiousness},
     {"label": "神経症的傾向", "value": neuroticism},
     {"label": "開放性", "value": openness},
]

df = pd.DataFrame({
     "label": [record["label"] for record in data],
     "value": [record["value"] for record in data],
})

print(df)

fig = px.line_polar(df, r='value', theta='label', line_close=True,height=500, width=500, title='診断結果')
st.plotly_chart(fig)
# ============================================

personality_list = ['外向性', '協調性', '誠実性', '神経症的傾向', '開放性']
choice = st.selectbox('各特性の特徴', personality_list)
## choice = st.multiselect('各特性の特徴', personality_list, default='外向性')

st.caption('基本的には各ポイントが、0から4の間はその特性は低め、5から8の間はその特性は高めと考えられます。')

if choice == '外向性':
     st.write(f'外向性：{extraversion}')
     if extraversion >= 5:
          st.write('＜外向性が高い人の特徴＞　コミュニケーション力に優れ、野心を持っている')
          ## st.markdown('コミュニケーション力に優れ、野心を持っている')
     elif extraversion <= 4:
          st.write('＜外向性が低い人の特徴＞　物事を冷静に考察する力に優れ、家庭の安定を求める')
          ## st.markdown('物事を冷静に考察する力に優れ、家庭の安定を求める')          

elif choice == '協調性':
     st.write(f'協調性：{agreeableness}')
     if agreeableness >=5:
          st.write('＜協調性が高い人の特徴＞　優しくて心が広い、他人に対しても親切で、協力的で素直。協力的で道徳的')
          ## st.markdown('優しくて心が広い、他人に対しても親切で、協力的で素直。協力的で道徳的')
     elif agreeableness <= 4:
          st.write('＜協調性が低い人の特徴＞　カリスマ性があり、孤立を恐れない')
          ## st.markdown('カリスマ性があり、孤立を恐れない')         

elif choice == '誠実性':
     st.write(f'誠実性：{conscientiousness}')
     if conscientiousness >=5:
          st.write('＜誠実性が高い人の特徴＞　コツコツと計画的に物事をこなす、几帳面で一生懸命働く。自己抑制が効き、集中力が高い')
          st.write('一点集中型で、目の前の問題の解決や目標の達成に向けて誠実に取り組む性質を持っている。長期的な計画を立てて遂行することも得意とし、公私共に安定感のある人として頼られる存在になるかも！')
          ## st.markdown('コツコツと計画的に物事をこなす、几帳面で一生懸命働く。自己抑制が効き、集中力が高い')
     elif conscientiousness <= 4:
          st.write('＜誠実性が低い人の特徴＞　アドリブ力に長け、行動力がある')
          st.write('注意散漫で飽きっぽい性質を持っている。ただし、衝動的な分、さまざまなものに興味を持ち、行動力を発揮する能力も兼ね備えているとも言える。')
          ## st.markdown('アドリブ力に長け、行動力がある')

elif choice == '神経症的傾向':
     st.write(f'神経症的傾向：{neuroticism}')
     if neuroticism >=5:
          st.write('＜神経症傾向の高い人の特徴＞　周囲の人の感情への感度が高く、空気を読むことができ、洞察力がある')
          st.write('人よりも優れた感受性を備えているため、ネガティブな出来事に遭遇した際、動揺しやすい傾向あり。独特の発想力、繊細な気配りのできる性質とも言える。')
          ## st.markdown('周囲の人の感情への感度が高く、空気を読むことができ、洞察力がある')
     elif neuroticism <= 4:
          st.write('＜神経症的傾向が低い人の特徴＞　恐怖心に囚われることなく頼れる存在で、温和')
          st.write('物事に動じず、冷静に判断を下すことができる。一方で、自分に近づく危険に気づくのが遅いという面もあり。')
          ## st.markdown('恐怖心に囚われることなく頼れる存在で、温和')

elif choice == '開放性':
     st.write(f'開放性：{openness}')
     if openness >=5:
          st.write('＜開放性が高い人の特徴＞　好奇心が強く、新しいことに挑戦してオリジナリティも持っている、創造力を発揮できる、芸術的センスもある、芸術性、知性に優れ、改革を好む')
          st.write('常識にとらわれず革新的な言動で周囲の人を惹きつけるが、時として独善的になってしまい、和を乱す傾向も。')
          ## st.markdown('好奇心が強く、新しいことに挑戦してオリジナリティも持っている、創造力を発揮できる、芸術的センスもある、芸術性、知性に優れ、改革を好む')
     elif openness <= 4:
          st.write('＜開放性が低い人の特徴＞　問題解決能力に優れ、形式的な思考を求める')
          st.write('手堅い選択でグループを安定的に機能させるが、メンバーは刺激の少なさに不満を感じるかも。')
          ## st.markdown('問題解決能力に優れ、形式的な思考を求める')
          
## c = st.container()
## st.write("This will show last")
## c.write("This will show first")
## c.write("This will show second")

